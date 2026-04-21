# -------- Stage 1: Build --------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install dependencies safely
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------- Stage 2: Runtime --------
FROM python:3.12-slim

WORKDIR /app

# Install curl safely (fix hadolint warning)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m appuser

# Copy installed dependencies from builder
COPY --from=builder /usr/local /usr/local

# Copy app code
COPY . .

# Change ownership (IMPORTANT)
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8000/docs || exit 1

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]