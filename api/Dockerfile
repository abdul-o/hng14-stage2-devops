# -------- Stage 1: Build --------
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# -------- Stage 2: Runtime --------
FROM python:3.12-slim

WORKDIR /app

# Install curl with version pinning
RUN apt-get update && \
    apt-get install -y curl=7.88.* && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m appuser

# Copy installed dependencies
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy app code
COPY . .

# Switch to non-root user
USER appuser

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8000/docs || exit 1

# Run app
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
