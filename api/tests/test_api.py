from fastapi.testclient import TestClient
from unittest.mock import patch
from api.main import app

client = TestClient(app)


@patch("api.main.redis_client")
def test_create_job(mock_redis):
    mock_redis.lpush.return_value = True
    mock_redis.hset.return_value = True

    response = client.post("/jobs")

    assert response.status_code == 200
    assert "job_id" in response.json()


@patch("api.main.redis_client")
def test_get_job_found(mock_redis):
    mock_redis.hget.return_value = b"completed"

    response = client.get("/jobs/test-id")

    assert response.status_code == 200
    assert response.json()["status"] == "completed"


@patch("api.main.redis_client")
def test_get_job_not_found(mock_redis):
    mock_redis.hget.return_value = None

    response = client.get("/jobs/test-id")

    assert response.status_code == 200
    assert response.json()["error"] == "not found"
