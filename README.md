# Personal MCP Server

A simple fastMCP example for a personal MCP server. Uses a set of documentation files (not included in repo) to allow agents to build targetted profiles of employment and project history.

## Public URI

The live MCP server can be accessed at [hjhero.com/mcp](https://www.hjhero.com/mcp)

This MCP server can run as:

- `streamable-http` (default) for hosted/network deployment
- `stdio` for local desktop MCP clients

## Run locally (HTTP)

```bash
python personal_mcp.py
```

By default this starts:

- Transport: `streamable-http`
- Host: `0.0.0.0`
- Port: `PORT` (if set), otherwise `MCP_PORT` (default `8000`)
- MCP path: `/mcp`

### Configure via environment variables

- `MCP_TRANSPORT` = `streamable-http` | `sse` | `stdio`
- `MCP_HOST` (default `0.0.0.0`)
- `PORT` (cloud platform runtime port; preferred if set)
- `MCP_PORT` (default `8000`; used when `PORT` is not set)
- `MCP_STREAMABLE_HTTP_PATH` (default `/mcp`)
- `MCP_MOUNT_PATH` (optional; SSE mount path)
- `MCP_API_KEY` (optional; if set, HTTP requests require `Authorization: Bearer <key>` or `x-api-key: <key>`)
- `MCP_HEALTH_PATH` (default `/healthz`)
- `MCP_LOG_LEVEL` (default `info`)

Example:

```bash
MCP_HOST=0.0.0.0 MCP_PORT=8080 MCP_TRANSPORT=streamable-http python personal_mcp.py
```

## Run locally (stdio)

```bash
python personal_mcp.py --transport stdio
```

## Docker

Build image:

```bash
docker build -t personal-mcp:latest .
```

Run container:

```bash
docker run --rm -p 8000:8000 \
	-e MCP_TRANSPORT=streamable-http \
	-e MCP_HOST=0.0.0.0 \
	-e MCP_PORT=8000 \
	personal-mcp:latest
```

## Managed hosting options

This container can be deployed to platforms like Render, Railway, Fly.io, Azure Container Apps, or ECS/Fargate.

Recommended production settings:

- Keep `MCP_TRANSPORT=streamable-http`
- Bind `MCP_HOST=0.0.0.0`
- Use `PORT` from the platform runtime (or `MCP_PORT` fallback)
- Set `MCP_API_KEY` so public HTTP requests require authentication
- Keep health checks on `GET /healthz` (or override with `MCP_HEALTH_PATH`)
- Put TLS and auth in front of the service before exposing it publicly

## Security notes

- If `MCP_API_KEY` is set, unauthenticated HTTP requests are rejected with `401`.
- The health endpoint remains open by default for platform health probes.
- For internet exposure, still prefer placing this behind a managed API gateway/reverse proxy for rate limiting and audit logging.

