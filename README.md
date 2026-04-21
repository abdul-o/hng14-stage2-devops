
# Job Processor System (Stage 2 DevOps Task)

## Overview

This project is a **multi-service job processing system** built using Docker and container orchestration.

It allows users to:
- Submit jobs from a frontend interface
- Queue jobs using Redis
- Process jobs asynchronously using a worker
- Track job status in real time

---

## 🧠 Architecture
  Browser → Nginx → Frontend → API → Redis → Worker


## Components

- **Frontend (Node.js / Express)**  
  Handles user interaction and communicates with the API

- **API (FastAPI)**  
  Receives job requests and stores them in Redis

- **Redis**  
  Acts as a message queue

- **Worker**  
  Processes jobs asynchronously from Redis

- **Nginx**  
  Acts as a reverse proxy and entry point

- **Docker Compose**  
  Orchestrates all services

---

## Technologies Used

- Docker
- Docker Compose
- Nginx
- FastAPI (Python)
- Redis
- Node.js (Express)

---

##  How to Run the Project
## To clone the project repository open a Terminal and run

``git clone https://github.com/abdul-o/hng14-stage2-devops.git
``cd hng14-stage2-devops

# Start all services
``docker-compose up --build

## Access the application
-Open your browser:
-http://localhost

## How to Use
- Click "Submit New Job"
- A job ID will be generated
- The job is added to a Redis queue
- The worker processes the job
- Status updates to completed

## How It Works (Step-by-Step)
- User submits a job via frontend
- Frontend sends request to API through Nginx
- API pushes job into Redis queue
- Worker pulls job from Redis
- Worker processes job and updates status
- Frontend polls API for job status

## Project Structure
.
├── api/            # FastAPI service
├── worker/         # Background worker
├── frontend/       # Node.js frontend
├── nginx/          # Nginx configuration
├── docker-compose.yml
└── README.md


## Environment Variables

Create a `.env` file in the root directory and add:

REDIS_HOST=redis
REDIS_PORT=6379
API_URL=http://nginx/api 


## Key Features
- Multi-container architecture
- Asynchronous job processing
- Reverse proxy with Nginx
- Service orchestration using Docker Compose
- Real-time job status tracking

## Final Notes
- All services run in isolated containers
- Communication is handled via Docker network
- System is accessible via a single entry point (Nginx)