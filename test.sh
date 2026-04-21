#!/bin/bash

set -e

echo "Starting services..."
docker compose up -d

echo "Waiting for services..."
sleep 10

echo "Testing API..."
curl -f http://localhost/api/jobs || exit 1

echo "Stopping services..."
docker compose down