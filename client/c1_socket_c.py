from utils.messages import MessagesContainer
import socket
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
    continue_messages = "y"

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    # adding inital messages to process
    messages.add_message(message_1)
    messages.add_message(message_2)
    messages.add_message(message_3)

    content = messages.get_messages()
    print("------------------------------[Inital Data]---------------------------------")
    for indx,message in content.items():
        dict_message = messages.full_message_process(indx=indx, message_body=message, client_socket=client_socket)

        content[indx].update(dict_message)

    while continue_messages == "y":
        continue_messages = input("Do you want to send another message? (y/n): ")
        if continue_messages == "y":
            message_body = messages.collect_new_message()
        
            messages.full_message_process(indx=messages.get_messages_len()-1, message_body=message_body, client_socket=client_socket)
        
    print("Finished processing messages...")
    client_socket.close()  # close the connection

    print("------------------------------[Processed Data]---------------------------------")
    for indx,message in content.items():
        print("------------------------------------")
        print(f"Final Processed message [{indx + 1}]:")
        pprint(message)

if __name__ == '__main__':
    client_program()