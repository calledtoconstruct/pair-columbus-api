
import requests
import json

def get_maltese():
    text = '{"message":"https://images.dog.ceo/breeds/maltese/asdf.jpg"}'
    data = json.loads(text)
    message = data["message"]
    status_code = 200
    return status_code, message