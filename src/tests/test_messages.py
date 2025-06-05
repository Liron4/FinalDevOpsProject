from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_post_message():
    response = client.post("/messages/", json={"msg_content": "test"})
    assert response.status_code == 200
    data = response.json()
    assert "msg_content" in data
    assert data["msg_content"] == "test"
    assert "msg_id" in data
    assert isinstance(data["msg_id"], int)
    assert "date" in data
    assert isinstance(data["date"], str)


def test_get_all_messages():
    response = client.get("/messages/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        message = data[0]
        assert "msg_id" in message
        assert "msg_content" in message
        assert "date" in message


def test_get_message_by_id():
    post_response = client.post(
        "/messages/",
        json={
            "msg_content": "test message"})
    post_data = post_response.json()
    msg_id = post_data["msg_id"]

    get_response = client.get(f"/messages/{msg_id}")
    assert get_response.status_code == 200
    get_data = get_response.json()
    assert get_data["msg_id"] == msg_id
    assert get_data["msg_content"] == "test message"
    assert "date" in get_data
