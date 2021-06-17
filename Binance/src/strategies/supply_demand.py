import asyncio
import aiohttp
import json
import argparse
import logging
import numpy as np

from utils.http_async import send_public_request, \
                            send_signed_request
from utils.stream import get_LiveData, get_stream
from utils.common import setup_logging, prettify, debug_logs
from settings import config


BASE_URL = config.API_URL

# BASE_URL = "https://api.binance.com/api"


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-log", 
                        "--log",
                        default="warning",
                        help=("Provide logging level. "
                              "Example --log debug', default='warning'"))

    return parser


async def get_OrderBook1(session):
    '''Default 100; 
       max 5000. 
       Valid limits:[5, 10, 20, 50, 100, 500, 1000, 5000]'''

    params  = {'symbol':'BTCUSDT', 
                'limit': 500}
    resp = await send_public_request(session, "/api/v3/depth", params, 
                                                    return_type="json")
    return resp

async def get_OrderBook(session):
    # return await get_stream(session, 'btcusdt@depth5@100ms', 5)
    return await get_stream(session, 'btcusdt@depth@100ms', 10)


async def _main():
    async with aiohttp.ClientSession() as session:

        await get_OrderBook(session)

        # bids = np.array(resp['bids'])
        # asks = np.array(resp['asks'])
        # print(resp['lastUpdateId'])
        # print("\n")
        # print(bids.shape)
        # print("\n")
        # print(asks.shape)
    
        
        
        # debug_logs(prettify(resp))

def main():
    parser = parse_arguments()
    args = parser.parse_args()
    if args.log:
        log_level = args.log
    else:
        log_level = config.LOG_LEVEL
    setup_logging(log_level)

    # asyncio.run(_main())
    asyncio.run(_main())


    


if __name__ == "__main__":
    main()