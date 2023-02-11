import socket
import json
import time


def s1_socket_s():
    host = socket.gethostname()
    port = 5001

    server_socket = socket.socket()
    print("Starting server S1 on " + str(host) + ":" + str(port))
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        raw_data = conn.recv(1024)
        decoded_data = raw_data.decode()
        dict_data = json.loads(decoded_data)

        print(f"Original data from connected user: {dict_data}")
        time.sleep(5.54)  # simulate processing delay
        dict_data["processedBy"] = "Processed by S1"
        print(f"Processed data: {dict_data}")

        str_message = json.dumps(dict_data)
        encoded_message = str_message.encode()
        conn.send(encoded_message)

    conn.close()  # close the connection


if __name__ == "__main__":
    s1_socket_s()
