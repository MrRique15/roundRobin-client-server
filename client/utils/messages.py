class MessagesContainer():
    messages = {}

    def __init__(self) -> None:
        self.messages = {}

    def add_message(self, message) -> None:
        self.messages[self.messages.__len__()] = message

    def get_message_by_id(self, id) -> dict :
        return self.messages[id]

    def get_messages(self) -> dict:
        return self.messages