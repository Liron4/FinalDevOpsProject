class MsgPayload:
    def __init__(self, msg_id: int, msg_name: str):
        self.msg_id = msg_id
        self.msg_name = msg_name

    def __repr__(self):
        return f"MsgPayload(msg_id={self.msg_id}, msg_name='{self.msg_name}')"