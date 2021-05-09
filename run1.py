from settings import config
import requests
import asyncio
import aiohttp
import hashlib
import hmac
import json
from urllib.parse import urlencode
import time

API_KEY = config.API_KEY
SECRET = config.SECRET_KEY
BASE_URL = config.API

'''Instead of creating session per request, 
    we should create one session per project 
    and run all requests in it'''

session = aiohttp.ClientSession()
session.headers.update({
    'Content-Type': 'application/json;charset=utf-8',
    'X-MBX-APIKEY': API_KEY
    })


def hashing(query_string):
    return hmac.new(SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def get_timestamp():
    return int(time.time() * 1000)

def dispatch_request(http_method):

    return {
        'GET': session.get,
        'DELETE': session.delete,
        'PUT': session.put,
        'POST': session.post,
    }.get(http_method, 'GET')
    

    # async with aiohttp.ClientSession() as session:
    #     async with session.get('http://python.org') as response:

    #         print("Status:", response.status)
    #         print("Content-type:", response.headers['content-type'])

    #         html = await response.text()===
    #         print("Body:", html[:15], "...")


def dispatch_request1(http_method):
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json;charset=utf-8',
        'X-MBX-APIKEY': API_KEY
    })
    return {
        'GET': session.get,
        'DELETE': session.delete,
        'PUT': session.put,
        'POST': session.post,
    }.get(http_method, 'GET')

async def send_signed_request(http_method, url_path, payload={}):
    query_string = urlencode(payload, True)
    if query_string:
        query_string = "{}&timestamp={}".format(query_string, get_timestamp())
    else:
        query_string = 'timestamp={}'.format(get_timestamp())

    url = BASE_URL + url_path + '?' + query_string + '&signature=' + hashing(query_string)
    print("{} {}".format(http_method, url))
    params = {'url': url, 'params': {}}
    response = dispatch_request(http_method)(**params)
    return response.json()


def send_public_request(url_path, payload={}):
    query_string = urlencode(payload, True)
    url = BASE_URL + url_path
    if query_string:
        url = url + '?' + query_string
    print("{}".format(url))
    response = dispatch_request('GET')(url=url)
    return response.json()

# params = {
#     "symbol": "BNBUSDT",
#     "side": "BUY",
#     "type": "LIMIT",
#     "timeInForce": "GTC",
#     "quantity": 1,
#     "price": "20"
# }

response = send_signed_request('GET', '/v3/account')
print(response)


