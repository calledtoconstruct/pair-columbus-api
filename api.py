
import requests
import json

def get_random_maltese():
    response = requests.get('https://dog.ceo/api/breed/maltese/images/random')
    text = response.text
    data = json.loads(text)
    message = data["message"]
    status_code = 200
    return status_code, message