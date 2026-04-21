# 🛠️ Fixes and Debugging Log

This document outlines the issues encountered during the Stage 2 DevOps task and how they were resolved.

---

## 1. Python not recognized

File: Local Machine (Terminal)  
Line: N/A  
Issue: `python` and `pip` commands not found  
Cause: Python not installed or not added to PATH  
Fix: Installed Python and added it to system PATH  

---

## 2. Uvicorn command not found

File: api (Terminal)  
Line: N/A  
Issue: `uvicorn: command not found`  
Cause: Python scripts directory not in PATH  
Fix: Used module execution instead:  
```bash
python -m uvicorn main:app --reload


3. Redis connection failed in API

File: api/main.py
Line: Redis connection initialization
Issue: API failed to connect to Redis at localhost:6379
Cause: Redis running inside Docker container, not on localhost
Fix: Updated Redis host to use Docker service name

host=os.getenv("REDIS_HOST", "redis")


4. Worker unable to connect to Redis

File: worker/worker.py
Line: Redis connection initialization
Issue: Worker failed with connection refused error
Cause: Worker was trying to connect to localhost instead of Redis container
Fix: Updated connection to use environment variables

host=os.getenv("REDIS_HOST", "redis")

5. Worker not processing jobs

File: worker/worker.py
Line: Job processing loop
Issue: Worker showed no logs and appeared inactive
Cause: Logs were buffered and not flushed
Fix: Added logging and ensured output visibility

print("Processing job", flush=True)


6. Jobs not reaching worker

File: api/main.py
Line: Job creation endpoint
Issue: Jobs were not being processed by worker
Cause: Job was not pushed into Redis queue
Fix: Added queue push operation

r.lpush("job", job_id)


7. Multiple Docker containers conflict

File: Docker environment
Line: N/A
Issue: Old containers interfered with new setup
Cause: Previously running containers not removed
Fix: Stopped and removed all containers

docker stop $(docker ps -q)
docker rm $(docker ps -aq)

8. Docker build failure

File: Docker build process
Line: N/A
Issue: failed to prepare extraction snapshot
Cause: Corrupted Docker cache
Fix: Cleared Docker cache

docker system prune -a
docker builder prune -a

9. Worker failed due to Redis not ready

File: worker/worker.py
Line: Before Redis usage
Issue: Worker crashed during startup
Cause: Redis service not ready when worker started
Fix: Added retry logic

while True:
    try:
        r.ping()
        break
    except:
        time.sleep(2)


10. Frontend unable to call API (Docker networking)

File: frontend/app.js
Line: API_URL definition
Issue: Frontend could not reach API
Cause: Used localhost instead of Docker service name
Fix: Updated API URL

const API_URL = "http://api:8000";

11. Nginx integration broke API calls

File: frontend/app.js
Line: API_URL definition
Issue: API returned undefined and 500 errors
Cause: Frontend server used incorrect API route after Nginx setup
Fix: Updated API URL to route through Nginx

const API_URL = "http://nginx/api";

12. Frontend displayed "undefined"

File: frontend (UI logic)
Line: Job status display
Issue: UI showed undefined for job status
Cause: API request failed and response was not handled
Fix: Ensured correct API routing and response handling

13. Duplicate Redis service in docker-compose

File: docker-compose.yml
Line: Redis service definition
Issue: Validation error and unexpected behavior
Cause: Redis service defined twice
Fix: Removed duplicate definition and kept a single service

14. Incorrect restart configuration

File: docker-compose.yml
Line: Top-level configuration
Issue: restart:always caused invalid configuration
Cause: Restart policy placed outside service block
Fix: Moved restart policy inside each service

restart: always

15. Missing environment variable configuration

File: docker-compose.yml
Line: Service environment section
Issue: Hardcoded values reduced flexibility
Cause: Environment variables not properly used
Fix: Added environment variables for Redis and API communication

📌 Conclusion

During this task, several real-world DevOps challenges were encountered and resolved:

Container networking issues
Service dependency timing problems
Reverse proxy routing errors
Logging and debugging challenges
Docker configuration mistakes

Each issue was identified, analyzed, and resolved systematically, resulting in a fully functional multi-service system.