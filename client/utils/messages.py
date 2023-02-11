import json
import time
from pprint import pprint


class MessagesContainer:
    messages = {}

    def __init__(self) -> None:
        self.messages = {}

    def add_message(self, message) -> None:
        self.messages[self.messages.__len__()] = message

    def get_message_by_id(self, id) -> dict:
        return self.messages[id]

    def get_messages(self) -> dict:
        return self.messages

    def collect_new_message(self) -> dict:
        message_body = {}

        message_body["id"] = int(input("Insert message ID:"))
        message_body["protocol"] = input("Insert message protocol:")
        message_body["content"] = input("Insert message content:")
        message_body["database"] = input("Insert used database or None:")
        message_body["token"] = input("Insert api token:")
        message_body["usedServerMustBe"] = input("Insert server name or None:")
        message_body["processedBy"] = "Not processed yet"

        self.add_message(message_body)
        return self.messages[self.messages.__len__() - 1]

    def process_and_send_message(self, message_body, client_socket) -> None:
        str_message = json.dumps(message_body)
        encoded_message = str_message.encode()
        client_socket.send(encoded_message)

    def process_received_message(self, raw_message) -> dict:
        decoded_data = raw_message.decode()
        dict_message = json.loads(decoded_data)

        return dict_message

    def full_message_process(self, indx, message_body, client_socket) -> dict:
        initial_time = time.time()
        print("------------------[Sending]------------------")
        print(f"Sending message [{indx + 1}]:")
        pprint(message_body)

        self.process_and_send_message(
            message_body=message_body, client_socket=client_socket
        )

        raw_data = client_socket.recv(1024)  # receive response

        dict_message = self.process_received_message(raw_message=raw_data)
        end_time = time.time()
        print("------------------[Receiving]------------------")
        print(f"Message [{indx + 1}] received from server:")
        pprint(dict_message)  # show in terminal the dict message received
        print(
            f"Time to process message [{indx + 1}]: {round((end_time - initial_time) * 1000, 2)} ms"
        )

        return dict_message

    def get_messages_len(self) -> int:
        return self.messages.__len__()
