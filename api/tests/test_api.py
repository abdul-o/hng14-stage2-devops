from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_job():
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()

def test_get_job():
    response = client.post("/jobs")
    job_id = response.json()["job_id"]

    res = client.get(f"/jobs/{job_id}")
    assert res.status_code == 200