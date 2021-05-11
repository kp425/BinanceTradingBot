import aiohttp
import asyncio
import argparse
import hashlib
import hmac
import json
from urllib.parse import urlencode
import time
from settings import config
import logging

API_KEY = config.API_KEY
SECRET = config.SECRET_KEY
BASE_URL = config.API_URL

import functools
def print_fn(func):
    @functools.wraps(func)
    async def _print_fn(*args, **kwargs):
        response = await func(*args, **kwargs)
        print(response)
        print(response.status)
    return _print_fn

def hashing(query_string):
    return hmac.new(SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def get_timestamp():
    return int(time.time() * 1000) 


def dispatch_request(session, http_method):
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

@print_fn
async def send_signed_request(session, http_method, url_path, payload={}):
    query_string = urlencode(payload, True)
    if query_string:
        query_string = "{}&timestamp={}".format(query_string, get_timestamp())
    else:
        query_string = 'timestamp={}'.format(get_timestamp())
    url = BASE_URL + url_path + '?' + query_string + '&signature=' + hashing(query_string)
    # print("{} {}".format(http_method, url))
    params = {'url': url, 'params': {}}
    response = await dispatch_request(session, http_method)(**params)
    # print(f"{url_path}          {response.status}")
    return response

@print_fn
async def send_public_request(session, url_path, payload={}):
    query_string = urlencode(payload, True)
    url = BASE_URL + url_path
    if query_string:
        url = url + '?' + query_string
    # print("{}".format(url))
    response = await dispatch_request(session, 'GET')(url=url)
    # print(f"{url_path}          {response.status}")
    return response

async def test_signed_request():
    params = {  "symbol":"BNBUSDT", 
                "side":"BUY",
                "type":"LIMIT",
                "quantity":"1",
                "timeInForce":"GTC",
                "price":"200"
            }
    async with aiohttp.ClientSession() as session:
        resp = await send_signed_request(session, "POST", "/api/v3/order", params)
        print(resp.status)
        print(resp)
        return resp

async def test_public_request():
    pass

def test():

    coroutines = []
    session = aiohttp.ClientSession()
    # get klines
    klines = send_public_request(session, '/api/v3/klines' , {"symbol": "BTCUSDT", "interval": "1d"})
    # print(response)


    ### USER_DATA endpoints, call send_signed_request #####
    # get account informtion
    # if you can see the account details, then the API key/secret is correct
    account = send_signed_request(session, 'GET', '/api/v3/account')
    # print(response)


    # # place an order
    # if you see order response, then the parameters setting is correct
    params = {
    "symbol": "BNBUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 1,
    "price": "200"
    }
    order = send_signed_request(session, 'POST', '/api/v3/order', params)
    # print(response)


    # transfer funds
    params = {
    "fromEmail": "",
    "toEmail": "",
    "asset": "USDT",
    "amount": "0.1"
    }
    sub_transfer = send_signed_request(session, 'POST', '/wapi/v3/sub-account/transfer.html', params)
    # print(response)


    # New Future Account Transfer (FUTURES)
    params = {
    "asset": "USDT",
    "amount": 0.01,
    "type": 2
    }
    transfer = send_signed_request(session, 'POST', '/sapi/v1/futures/transfer', params)
    
    # await asyncio.sleep(0.5)
    coroutines = [klines, account, order, sub_transfer, transfer]
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*coroutines))
    
    session.close()
    


if __name__ == '__main__':
    test()
    # parser = argparse.ArgumentParser()
    # parser.add_argument('url', type=str)
    # args = parser.parse_args()
    # print(args.url)
    
    




