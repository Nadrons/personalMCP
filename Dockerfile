FROM python:3.14-slim

WORKDIR /app

COPY personal_mcp.py ./
COPY general_info ./general_info
COPY employment_projects ./employment_projects

RUN pip install --no-cache-dir "mcp[cli]>=1.26.0" "httpx>=0.28.1"

ENV MCP_TRANSPORT=streamable-http
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8000

EXPOSE 8000

CMD ["python", "personal_mcp.py"]
