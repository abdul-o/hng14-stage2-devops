# import redis
# import time
# import os
# import signal

# r = redis.Redis(
#     host=os.getenv("REDIS_HOST", "redis"),
#     port=int(os.getenv("REDIS_PORT", 6379))
# )

# def process_job(job_id):
#     print(f"Processing job {job_id}")
#     time.sleep(2)  # simulate work
#     r.hset(f"job:{job_id}", "status", "completed")
#     print(f"Done: {job_id}")

# while True:
#     print("Worker waiting for job...")
#     job = r.brpop("job", timeout=5)
#     if job:
#         _, job_id = job
#         process_job(job_id.decode())



import os
import redis
import time

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379))
)

print("Worker started...")

while True:
    print("Waiting for job...")

    job = r.brpop("job", timeout=5)

    if job:
        _, job_id = job
        job_id = job_id.decode()

        print(f"Processing job {job_id}", flush=True)

        time.sleep(2)

        r.hset(f"job:{job_id}", "status", "completed")

        print(f"Done: {job_id}", flush=True)