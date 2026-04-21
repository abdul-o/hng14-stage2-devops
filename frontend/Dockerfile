# -------- Stage 1 --------
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# -------- Stage 2 --------
FROM node:18-alpine

WORKDIR /app

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy built app
COPY --from=builder /app /app

USER appuser

# Healthcheck
HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1

EXPOSE 3000

CMD ["npm", "start"]