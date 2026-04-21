# -------- Stage 1 --------
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# -------- Stage 2 --------
FROM python:3.12-slim

WORKDIR /app

# Create non-root user
RUN useradd -m workeruser

# Copy dependencies
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

USER workeruser

# Healthcheck (basic process check)
HEALTHCHECK CMD pgrep -f worker.py || exit 1

CMD ["python", "worker.py"]