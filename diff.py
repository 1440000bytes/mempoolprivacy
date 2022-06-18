import requests
import json
import jsondiff as jd
from jsondiff import diff


def get_mempool(node):

    url = "https://spkreuse.fun/mempool?node=" + node

    payload={}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    mempool = json.loads(response.text)

    return mempool['result']

if __name__=="__main__":
    print(get_mempool('1'))
    print(get_mempool('2'))
    difference = diff(get_mempool('1'), get_mempool('2'))
    print(difference)
