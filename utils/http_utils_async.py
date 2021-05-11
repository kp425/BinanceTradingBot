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

level = logging.DEBUG
logging.basicConfig(level=level)
logger = logging.getLogger(__name__)


def _hashing(query_string):
    return hmac.new(SECRET.encode('utf-8'), 
                    query_string.encode('utf-8'), 
                    hashlib.sha256).hexdigest()

def _get_timestamp():
    return int(time.time() * 1000) 


def _dispatch_request(session, http_method):
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


def _debug_logs(*args):
    logging.debug("\n")
    for i in args:
        logging.debug(i)

async def send_signed_request(session, http_method, url_path, payload={}):
    query_string = urlencode(payload, True)
    if query_string:
        query_string = "{}&timestamp={}".format(query_string, _get_timestamp())
    else:
        query_string = 'timestamp={}'.format(_get_timestamp())
    hash_ = _hashing(query_string)
    # url = BASE_URL + url_path + '?' + query_string + '&signature=' + hash_
    url = f"{BASE_URL}{url_path}?{query_string}&signature={hash_}"
    params = {'url': url, 'params': {}}
    
    func_ = _dispatch_request(session, http_method)
    async with func_(**params) as response:

        _debug_logs(response.status, url, url_path, 
                    await response.read(), 
                    #await response.text()
                    )
        return response


async def send_public_request(session, url_path, payload={}):
    query_string = urlencode(payload, True)
    # url = BASE_URL + url_path
    url = f"{BASE_URL}{url_path}"
    if query_string:
        # url = url + '?' + query_string
        url = f"{url}?{query_string}"
    
    func_ = _dispatch_request(session, "GET")
    async with func_(url=url) as response:

        _debug_logs(response.status, url, url_path, 
                    await response.read(), 
                    #await response.text()
                    )
        return response





async def _test():

    coroutines = []

    async with aiohttp.ClientSession() as session:

        # get klines
        klines = send_public_request(session, '/api/v3/klines' , {"symbol": "BTCUSDT", "interval": "1d"})

        ### USER_DATA endpoints, call send_signed_request #####
        # get account informtion
        # if you can see the account details, then the API key/secret is correct
        account = send_signed_request(session, 'GET', '/api/v3/account')
  
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


        # transfer funds
        params = {
        "fromEmail": "",
        "toEmail": "",
        "asset": "USDT",
        "amount": "0.1"
        }
        sub_transfer = send_signed_request(session, 'POST', '/wapi/v3/sub-account/transfer.html', params)


        # New Future Account Transfer (FUTURES)
        params = {
        "asset": "USDT",
        "amount": 0.01,
        "type": 2
        }
        transfer = send_signed_request(session, 'POST', '/sapi/v1/futures/transfer', params)
        coroutines = [klines, account, order, sub_transfer, transfer]
        tasks = await asyncio.gather(*coroutines)

    return tasks

def run_test():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_test())

if __name__ == '__main__':
    
    run_test()
    
    




