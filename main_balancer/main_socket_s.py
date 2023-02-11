import socket
import asyncio
from utils.data_processing import DataProcessing
from utils.json_processing import message_decoder, message_encoder


# Main function to receive connections, verify data and call the right server to process it.
# receive encoded message in bytes, decode it to json string and convert to python dict
# for response, it convert a python dict to json string, encode it in bytes and send to client
async def main_socket_s():
    host = socket.gethostname()
    port = 5000
    last_socket = None

    main_socket = socket.socket()
    main_socket.bind((host, port))
    print("Starting main server on " + str(host) + ":" + str(port))
    main_socket.listen(3)

    data_processing = DataProcessing(host=host)

    conn, address = main_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024)
        decoded_data = data.decode()
        dict_data = message_decoder(message=decoded_data)
        if dict_data:
            print(f"from connected user [{address}]: {dict_data}")

            processed_data, last_socket = await data_processing.process_data(
                data=dict_data, last_socket=last_socket
            )

            print(f"Received from processing server: {processed_data}")

            if processed_data:
                str_message = message_encoder(message=processed_data)
                encoded_data = str_message.encode()
            else:
                encoded_data = None

            conn.send(encoded_data)
        else:
            print("Error: data not received")
            break

    conn.close()
    data_processing.close_sockets()


def main():
    asyncio.run(main_socket_s())


if __name__ == "__main__":
    main()
