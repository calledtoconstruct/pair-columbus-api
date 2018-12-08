
import requests
import json

def get_maltese():
    text = '{"message":"https://images.dog.ceo/breeds/maltese"}'
    data = json.loads(text)
    status_code = 200
    return status_code, data["message"]