from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_post_message():
    response = client.post("/messages/", json={"msg_name": "test"})
    assert response.status_code == 200
    data = response.json()
    assert "msg_name" in data
    assert data["msg_name"] == "test"
    assert "msg_id" in data
    assert isinstance(data["msg_id"], int)
    assert "date" in data
    assert isinstance(data["date"], str)