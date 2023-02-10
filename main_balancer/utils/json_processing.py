import json

# encodding method that receives a python dict and return a json string
def message_encoder(message) -> str:
    encoded_message_str = json.dumps(message)
    return encoded_message_str

# decodding method that receives a json string and return a python dict
def message_decoder(message) -> dict:
    decoded_message_dict = json.loads(message)
    return decoded_message_dict