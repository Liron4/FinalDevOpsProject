from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_post_message():
    response = client.post("/messages/", json={"msg_name": "test"})
    assert response.status_code == 200
    assert "msg_name" in response.json()