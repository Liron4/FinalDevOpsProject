from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import json
import os

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
    msg_name: str


class MessageOut(BaseModel):
    msg_id: int
    msg_name: str
    date: str


@router.post("/", response_model=MessageOut)
def add_msg(msg: MessageIn):
    messages = load_messages()
    msg_id = messages[-1]['msg_id'] + 1 if messages else 0
    now = datetime.utcnow().isoformat()
    msg_obj = {
        "msg_id": msg_id,
        "msg_name": msg.msg_name,
        "date": now
    }
    messages.append(msg_obj)
    save_messages(messages)
    return msg_obj
