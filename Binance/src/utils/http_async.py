import argparse
import hashlib
import hmac
import json
from urllib.parse import urlencode
import time
from settings import config
import logging
from .common import setup_logging, debug_logs

API_KEY = config.API_KEY
SECRET = config.SECRET_KEY
BASE_URL = config.API_URL


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




async def send_signed_request(session, http_method, url_path, payload={}, 
                                                        return_type=None):
    query_string = urlencode(payload, True)
    if query_string:
        query_string = "{}&timestamp={}".format(query_string, _get_timestamp())
    else:
        query_string = 'timestamp={}'.format(_get_timestamp())
    hash_ = _hashing(query_string)
    url = f"{BASE_URL}{url_path}?{query_string}&signature={hash_}"
    params = {'url': url, 'params': {}}
    
    func_ = _dispatch_request(session, http_method)
    async with func_(**params) as response:
        debug_logs(response.status, url_path, url,
                    # await response.json()
                    # await response.read(), 
                    # await response.text()
                    )
        if return_type is None:
            resp = None
        elif return_type == "json":
            resp = await response.json()
        elif return_type == "text":
            resp = await response.text()
        elif return_type == "bytes":
            resp = await response.read()
        
    return resp


async def send_public_request(session, url_path, payload={}, return_type=None):
    query_string = urlencode(payload, True)
    url = f"{BASE_URL}{url_path}"
    if query_string:
        url = f"{url}?{query_string}"
    func_ = _dispatch_request(session, "GET")
    async with func_(url=url) as response:
        debug_logs(response.status, url_path, 
                    # await response.json()
                    # await response.read(), 
                    #await response.text()
                    )
        if return_type is None:
            resp = None 
        elif return_type == "json":
            resp = await response.json()
        elif return_type == "text":
            resp = await response.text()
        elif return_type == "bytes":
            resp = await response.read()
    return resp







    
    




