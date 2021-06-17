from settings import config

import json
import asyncio
import aiohttp
from .common import prettify, debug_logs


BASE_URL = config.API_URL

'''
A single connection can listen to a maximum of 1024 streams 
                            - Quote by Binance
'''

async def get_LiveData(stream):
    if "/" in stream:
        uri = f"{BASE_URL}/stream?streams={stream}"
    else:
        uri = f"{BASE_URL}/ws/{stream}"
    print(uri)
    async with aiohttp.ClientSession() as session:
        ws  = await session.ws_connect(uri)
        while True:
            _data = await ws.receive()
            _dict = json.loads(_data.data)
            debug_logs(prettify(_dict)) 


async def get_stream(session, stream, repeat=None):
    if "/" in stream:
        uri = f"{BASE_URL}/stream?streams={stream}"
    else:
        uri = f"{BASE_URL}/ws/{stream}"

    async with session.ws_connect(uri) as ws:
        if repeat:
            for _ in range(repeat):
                print('here')
                _data = await ws.receive()
                _dict = json.loads(_data.data)
                debug_logs(prettify(_dict)) 
        else:
            while True:
                _data = await ws.receive()
                _dict = json.loads(_data.data)
                debug_logs([prettify(_dict)]) 



if __name__ == "__main__":

    loop = asyncio.get_event_loop()

    coroutines = [get_LiveData('btcusdt@aggTrade'), 
                  get_LiveData('btcusdt@aggTrade/btcusdt@depth')]

    loop.run_until_complete(asyncio.gather(*coroutines))










