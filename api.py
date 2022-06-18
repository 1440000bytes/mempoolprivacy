import requests
from flask import Flask, request
import json


app = Flask(__name__)

@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/mempool")
def getrawmempool():
    if (request.args.get('node') == '1'):

        url = 'http://127.0.0.1:5555' 
    elif (request.args.get('node') == '2'):
        url = 'http://127.0.0.1:7777'

    payload = "{\"jsonrpc\": \"1.0\", \"id\": \"txid\", \"method\": \"getrawmempool\"}"
    headers = {
        'Authorization': 'Basic cmFuZG9tcGFzc3dvcmQ=',
        'Content-Type': 'applications/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)     
    transactions = json.loads(response.text)

    return transactions['result'].json()

if __name__ == "__main__":
    app.run()
