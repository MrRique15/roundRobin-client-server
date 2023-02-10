from utils.messages import MessagesContainer
import socket
import json
from pprint import pprint
message_1 = {
    "id": 1,
    "protocol": "http",
    "content": "sample message used to test http connection on S1",
    "database": "MongoDB",
    "token": "7a1nsç%$9187AnAH864AHjdn*&6snABAP*¨!$53271",
    "usedServerMustBe": "S1",
    "processedBy": "Not processed yet"
}
message_2 = {
    "id": 2,
    "protocol": "udp",
    "content": "sample message used to test udp connection on S2",
    "database": "MongoDB",
    "token": "7a1nsç%$9187AnAH864AHjdn*&6snABAP*¨!$53271",
    "usedServerMustBe": "S2",
    "processedBy": "Not processed yet"
}
message_3 = {
    "id": 3,
    "protocol": "udp",
    "content": "sample message used to test udp connection on S3",
    "database": "MongoDB",
    "token": "7a1nsç%$9187AnAH864AHjdn*&6snABAP*¨!$53271",
    "usedServerMustBe": "S3",
    "processedBy": "Not processed yet"
}

def client_program():
    host = socket.gethostname()  # as both code is running on same pc, change if server is on another host
    port = 5000  # socket server port number, the exactly port number from the server
    messages = MessagesContainer()

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    messages.add_message(message_1)
    messages.add_message(message_2)
    messages.add_message(message_3)

    content = messages.get_messages()
    print("------------------------------[Inital Data]---------------------------------")
    for indx,message in content.items():
        print("------------------[Sending]------------------")
        pprint(f"Sending message [{indx + 1}]:\n {message}")
        str_message = json.dumps(message)
        encoded_message = str_message.encode()
        client_socket.send(encoded_message)

        raw_data = client_socket.recv(1024)  # receive response

        decoded_data = raw_data.decode()
        dict_data = json.loads(decoded_data)
        print("------------------[Receiving]------------------")
        print(f'Message [{indx + 1}] Received from server:\n {dict_data}')  # show in terminal the dict data received

        content[indx].update(dict_data)

    client_socket.close()  # close the connection

    print("------------------------------[Processed Data]---------------------------------")
    for indx,message in content.items():
        pprint(f"Final Processed message [{indx + 1}]: {message}")


if __name__ == '__main__':
    client_program()