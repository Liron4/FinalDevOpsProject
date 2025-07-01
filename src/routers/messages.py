from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from .metrics import REQUEST_COUNT, REQUEST_LATENCY, MESSAGES_CREATED
from datetime import datetime, timezone
import json
import os
from typing import List

router = APIRouter()
DATA_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'messages.json')


def load_messages():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_messages(messages):
    os.makedirs(DATA_FOLDER, exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(messages, f, indent=2)


class MessageIn(BaseModel):
    msg_content: str


class MessageOut(BaseModel):
    msg_id: int
    msg_content: str
    date: str


@router.post("/", response_model=MessageOut)
def add_msg(msg: MessageIn):
    start = datetime.now(timezone.utc)
    REQUEST_COUNT.labels(method="POST", endpoint="/messages/").inc()
    messages = load_messages()
    msg_id = messages[-1]['msg_id'] + 1 if messages else 0
    now = datetime.now(timezone.utc).isoformat()
    msg_obj = {
        "msg_id": msg_id,
        "msg_content": msg.msg_content,
        "date": now
    }
    messages.append(msg_obj)
    save_messages(messages)
    MESSAGES_CREATED.inc()
    latency = (datetime.now(timezone.utc) - start).total_seconds()
    REQUEST_LATENCY.labels(
        method="POST",
        endpoint="/messages/").observe(latency)
    return msg_obj


@router.get("/", response_model=List[MessageOut])
def get_all_messages():
    start = datetime.now(timezone.utc)
    REQUEST_COUNT.labels(method="GET", endpoint="/messages/").inc()
    messages = load_messages()
    latency = (datetime.now(timezone.utc) - start).total_seconds()
    REQUEST_LATENCY.labels(
        method="GET",
        endpoint="/messages/").observe(latency)
    return messages


@router.get("/{msg_id}", response_model=MessageOut)
def get_message(msg_id: int):
    start = datetime.now(timezone.utc)
    REQUEST_COUNT.labels(method="GET", endpoint="/messages/{msg_id}").inc()
    messages = load_messages()
    message_dict = {msg["msg_id"]: msg for msg in messages}
    latency = (datetime.now(timezone.utc) - start).total_seconds()
    REQUEST_LATENCY.labels(
        method="GET",
        endpoint="/messages/{msg_id}").observe(latency)
    if msg_id in message_dict:
        return message_dict[msg_id]
    raise HTTPException(
        status_code=404,
        detail=f"Message with ID {msg_id} not found")
