from mcp.server.fastmcp import FastMCP
import argparse
import json
import os
from pathlib import Path
from typing import Optional

# Initialize FastMCP server
BASE_DIR = Path(__file__).resolve().parent
PROJECTS_DIR = BASE_DIR / "employment_projects"
PROJECT_LIST_PATH = PROJECTS_DIR / "project_list.json"
CV_PATH = BASE_DIR / "general_info" / "fullCV.md"


def _get_host() -> str:
    return os.getenv("MCP_HOST", "0.0.0.0")


def _get_port() -> int:
    port_value = os.getenv("PORT") or os.getenv("MCP_PORT") or "8000"
    return int(port_value)


def _get_log_level() -> str:
    return os.getenv("MCP_LOG_LEVEL", "info").lower()

mcp = FastMCP(
    "personal_mcp",
    host=_get_host(),
    port=_get_port(),
    streamable_http_path=os.getenv("MCP_STREAMABLE_HTTP_PATH", "/mcp"),
)

# Constants


## Helper functions
# make some helper functions to make requests if needed

@mcp.tool()
async def get_full_cv() -> str:
    """Return a full, Markdown formatted CV/resume for Tim Cave, including work experience, education, skills, and any other relevant information."""
    cv_path = CV_PATH
    if not cv_path.exists():
        return "CV file not found, bad luck."

    try:
        with cv_path.open("r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading CV file: {str(e)}"

@mcp.tool()
async def get_project_list(id_only: bool = False) -> str:
    """Get a list of projects working on by Tim Cave, including descriptions, status and key skills.

    Args:
        id_only: If True, only return project IDs. Otherwise, include full descriptions and status.
    """
    with PROJECT_LIST_PATH.open("r") as f:
        projects = json.load(f)

    if not projects:
        return "Unable to fetch project list or no projects found."

    if id_only:
        return "\n".join([f"{project['name']}\nProject ID: {project['id']}" for project in projects])

    return "\n---\n".join([f"Name: {project['name']}\nProject ID: {project['id']}\nDescription: {project['description']}\nStatus: {project['status']}\nEmployer: {project['employer']}\nKey Words: {', '.join(project['key_words'])}" for project in projects])

@mcp.tool()
async def get_project_info(project_id: str, outcomes_only: bool = False) -> str:
    """Get detailed information about a specific project. Returns full contents of the associated info file if it exists.
    Use get_project_list with id_only=True to get a list of project IDs to use as input for this function.
    

    Args:
        project_id: The ID of the project to retrieve information for.
        outcomes_only: If True, only return the key outcomes of the project. Otherwise, include all available information.
    """
    with PROJECT_LIST_PATH.open("r") as f:
        projects = json.load(f)

    # This should probably be a rag function in case the info files get too long, but for now we'll just return the full contents.

    for project in projects:
        if project["id"].lower() == project_id.lower():
            info_file = project.get("info_file")
            if info_file:
                try:
                    with (PROJECTS_DIR / info_file).open("r") as info_f:
                        return info_f.read()
                except Exception as e:
                    return f"Error reading project info file: {str(e)}"
            else:
                return "No additional information available for this project."

    return "Project not found. Please check the project ID and try again."

def main():
    parser = argparse.ArgumentParser(description="Run personal MCP server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default=os.getenv("MCP_TRANSPORT", "streamable-http"),
        help="Transport to run: stdio, sse, or streamable-http",
    )
    parser.add_argument(
        "--mount-path",
        default=os.getenv("MCP_MOUNT_PATH"),
        help="Optional mount path for SSE transport",
    )
    args = parser.parse_args()

    if args.transport == "stdio":
        mcp.run(transport="stdio")
        return

    import uvicorn

    api_key = os.getenv("MCP_API_KEY")
    health_path = os.getenv("MCP_HEALTH_PATH", "/healthz")

    if args.transport == "streamable-http":
        app = mcp.streamable_http_app()
    else:
        app = mcp.sse_app(args.mount_path)

    app = HTTPApp(
        app=app,
        api_key=api_key,
        health_path=health_path,
    )
    uvicorn.run(
        app,
        host=_get_host(),
        port=_get_port(),
        log_level=_get_log_level(),
    )


class HTTPApp:
    def __init__(self, app, api_key: Optional[str], health_path: str = "/healthz"):
        self.app = app
        self.api_key = api_key
        self.health_path = health_path
        self.index_path = BASE_DIR / "index.html"

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "")
        method = scope.get("method", "GET")

        # Serve the HTML setup guide at root path
        if path == "/" and method == "GET":
            await self._send_html(send)
            return

        if path == self.health_path and method == "GET":
            await self._send_json(send, 200, '{"status":"ok"}')
            return

        if self.api_key and not self._is_authorized(scope):
            await self._send_json(send, 401, '{"error":"unauthorized"}')
            return

        await self.app(scope, receive, send)

    def _is_authorized(self, scope) -> bool:
        headers = {
            key.decode("latin-1").lower(): value.decode("latin-1")
            for key, value in scope.get("headers", [])
        }

        provided_api_key = headers.get("x-api-key")
        if provided_api_key == self.api_key:
            return True

        authorization = headers.get("authorization", "")
        if authorization.startswith("Bearer "):
            bearer_token = authorization[7:].strip()
            return bearer_token == self.api_key

        return False

    async def _send_html(self, send):
        if not self.index_path.exists():
            # Fallback if index.html doesn't exist
            html_content = "<html><body><h1>Personal MCP Server</h1><p>Server is running at <code>/mcp</code></p></body></html>"
            payload = html_content.encode("utf-8")
        else:
            with self.index_path.open("r", encoding="utf-8") as f:
                payload = f.read().encode("utf-8")
        
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"text/html; charset=utf-8"],
                    [b"content-length", str(len(payload)).encode("utf-8")],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": payload,
            }
        )

    async def _send_json(self, send, status_code: int, body: str):
        payload = body.encode("utf-8")
        await send(
            {
                "type": "http.response.start",
                "status": status_code,
                "headers": [
                    [b"content-type", b"application/json"],
                    [b"content-length", str(len(payload)).encode("utf-8")],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": payload,
            }
        )


if __name__ == "__main__":
    main()