from settings import config

import json
import asyncio
import aiohttp
import websockets

SOCKET_URL = config.WS
STREAM_URL = config.STREAM

'''
A single connection can listen to a maximum of 1024 streams 
                            - Quote by Binance
'''

async def live_data(stream):
    if "/" in stream:
        uri = STREAM_URL+"/?streamsp={}".format(stream)
    else:
        uri = SOCKET_URL+"/{}".format(stream)
    print(uri)
    async with aiohttp.ClientSession() as session:
        ws  = await session.ws_connect(uri)
        while True:
            data = await ws.receive()
            print(data)

if __name__ == "__main__":

    loop = asyncio.get_event_loop()

    coroutines = [live_data('btcusdt@aggTrade'), 
                  live_data('btcusdt@aggTrade/btcusdt@depth')]

    loop.run_until_complete(asyncio.gather(*coroutines))

# loop.run_until_complete(live_data('btcusdt@aggTrade'))
# loop.run_until_complete(live_data('btcusdt@aggTrade/btcusdt@depth'))
# loop.run_until_complete(live_data('btc'))








