# from utils import get_LiveData
import asyncio
import aiohttp
import logging
import json
import argparse

from settings import config
from utils.common import setup_logging, prettify, _debug_logs
from utils.stream import get_LiveData




BASE_URL = config.API_URL


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-log", 
                        "--log",
                        default="warning",
                        help=("Provide logging level. "
                              "Example --log debug', default='warning'"))

    return parser



async def get_LiveData1(stream, repeat=1):
    if "/" in stream:
        uri = f"{BASE_URL}/stream?streams={stream}"
    else:
        uri = f"{BASE_URL}/ws/{stream}"
    logging.debug(uri)

    count = 0
    async with aiohttp.ClientSession() as session:
        ws  = await session.ws_connect(uri)
        while count < repeat:
            _data = await ws.receive()
            # logging.debug(_data.data)
            _dict = json.loads(_data.data)
            _debug_logs([prettify(_dict)]) 
            count+=1


async def main():
    parser = parse_arguments()
    args = parser.parse_args()
    if args.log:
        log_level = args.log
    else:
        log_level = config.LOG_LEVEL
    setup_logging(log_level)
    coroutines = [get_LiveData('btcusdt@trade')
                # get_LiveData('btcusdt@kline_1m')
                #  get_LiveData('btcusdt@aggTrade', 1)
                 ]
    return await asyncio.gather(*coroutines)


if __name__ == "__main__":

    asyncio.run(main())
