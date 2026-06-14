# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for faida-mcp
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/faida-mcp"
LABEL org.opencontainers.image.description="faida-mcp — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir faida-mcp

CMD ["faida-mcp"]
