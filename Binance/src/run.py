from settings import config
import asyncio
import aiohttp
import json
import argparse
import logging
from utils import setup_logging
# from lab import get_accountinfo, system_status, \
#                 system_status_sapi, place_order, get_all_orders

from lab import *
from api.accounts import *


def prettify(json_):
    json_ = json.dumps(json_, indent=2)
    return json_

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
        resp = await get_AllAssets(session)
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

   




    


