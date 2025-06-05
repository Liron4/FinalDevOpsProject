from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_metrics_endpoint():
    client.post("/messages/", json={"msg_content": "test"})
    client.get("/messages/")
    client.get("/messages/0")
    response = client.get("/metrics/")
    assert response.status_code == 200
    assert "http_requests_total" in response.text
    assert "messages_created_total" in response.text
    assert "http_request_latency_seconds" in response.text
