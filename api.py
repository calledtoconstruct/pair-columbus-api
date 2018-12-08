
import requests
import json

from flask import Flask

def get_random_maltese():
    response = requests.get('https://dog.ceo/api/breed/maltese/images/random')
    text = response.text
    data = json.loads(text)
    message = data["message"]
    status_code = 200
    return status_code, message

app = Flask(__name__)

@app.route("/")
def index():

    status_code, response = get_random_maltese()

    img = '<img src="' + response + '" />'

    body = '<body>' + img + '</body>'
    head = '<head>' + '</head>'
    html = '<html>' + head + body + '</html>'
    
    return html