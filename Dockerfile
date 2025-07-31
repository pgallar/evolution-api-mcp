FROM python:3.11-slim as builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies with all dependencies
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

# Final stage
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 mcp && \
    chown -R mcp:mcp /app

# Create logs directory and set permissions
RUN mkdir -p /app/logs && \
    chown -R mcp:mcp /app/logs

# Copy wheels from builder
COPY --from=builder /app/wheels /wheels

# Switch to non-root user
USER mcp

# Install dependencies
COPY --chown=mcp:mcp requirements.txt .
RUN pip install --no-cache-dir /wheels/*

# Copy source code
COPY --chown=mcp:mcp . .

# Make scripts executable
RUN chmod +x /app/healthcheck.sh /app/check-env.sh

# Set environment variables
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8002

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD ["bash", "/app/healthcheck.sh"]

# Command to run the application
CMD ["python", "src/main.py"] 