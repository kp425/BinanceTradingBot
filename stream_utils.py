from settings import config

import json
import asyncio
import aiohttp


BASE_URL = config.API_URL

'''
A single connection can listen to a maximum of 1024 streams 
                            - Quote by Binance
'''

async def live_data(stream):
    if "/" in stream:
        uri = f"{BASE_URL}/stream?streams={stream}"
    else:
        uri = f"{BASE_URL}/ws/{stream}"
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










