from utils.json_processing import message_encoder, message_decoder
import asyncio
import socket


# Main processing unit, responsable to verify and convert data to send to other servers
# round robin method applied to check what server does it will send to procces data
class DataProcessing:
    s1_socket = None
    s2_socket = None
    s3_socket = None

    def __init__(self, host):
        self.s1_socket = socket.socket()
        self.s2_socket = socket.socket()
        self.s3_socket = socket.socket()

        self.s1_socket.connect((host, 5001))
        self.s2_socket.connect((host, 5002))
        self.s3_socket.connect((host, 5003))

    async def generate_response(self, data, used_socket=None) -> dict:
        str_message = message_encoder(message=data)  # transform dict -> str
        encoded_message = str_message.encode()  # encode str -> bytes

        used_socket.send(encoded_message)
        raw_data = used_socket.recv(1024)

        decoded_data = raw_data.decode()  # decode bytes -> str
        dict_data = message_decoder(message=decoded_data)  # transform str -> dict

        return dict_data

    async def process_data(self, data, last_socket=None):
        used_socket = None

        if type(data) != dict:
            print("Wrong message type received, returning...")
            return None, last_socket

        if data:
            if data["protocol"] == "http":
                print("Sending traffic to S1")
                used_socket = self.s1_socket
                last_socket = last_socket
            elif data["protocol"] == "udp":
                if last_socket == "S2":
                    print("Sending traffic to S3")
                    used_socket = self.s3_socket
                    last_socket = "S3"
                else:
                    print("Sending traffic to S2")
                    used_socket = self.s2_socket
                    last_socket = "S2"
            else:
                print(
                    "Invalid request protocol, exiting connection without response..."
                )
                return None, last_socket

            dict_data = await self.generate_response(data=data, used_socket=used_socket)
            return dict_data, last_socket
        else:
            print("No data received, returning...")
            return None

    def close_sockets(self):
        self.s1_socket.close()
        self.s2_socket.close()
        self.s3_socket.close()

        self.s1_socket = None
        self.s2_socket = None
        self.s3_socket = None
