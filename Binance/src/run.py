from settings import config
import asyncio
import aiohttp
import json
import argparse
import logging
from utils.common import setup_logging, prettify, debug_logs
from utils.http_async import send_public_request, send_signed_request

from lab import *
from api.accounts import *



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-log", 
                        "--log",
                        default="warning",
                        help=("Provide logging level. "
                              "Example --log debug', default='warning'"))

    return parser


async def _main():
    async with aiohttp.ClientSession() as session:
        # resp = await system_status(session)
        # resp = await get_all_orders(session)
        # resp = await get_AllCoinInfo(session)
        # resp = await get_AccountInfo(session)       #working
        # resp = await get_MyTrades(session)        #working
        # resp = await get_MyAddress(session)
        # resp = await get_AllAssets(session)
        resp = await place_order(session)
        logging.debug(resp)
        # logging.debug(prettify(resp))
        # return await asyncio.gather(*coroutines)


    


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

   




    


