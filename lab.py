
import asyncio
import aiohttp

from utils import send_public_request, \
            send_signed_request, live_data, run_test

import json
import argparse
import logging

def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument("-log", 
                        "--log",
                        default="warning",
                        help=("Provide logging level. "
                              "Example --log debug', default='warning'"))

    return parser

def set_logging_level(level):
    levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
    }
    level = levels.get(level.lower())

    if level is None:
        raise ValueError(
        f"log level given: {options.log}"
        f" -- must be one of: {' | '.join(levels.keys())}")
    
    logging.basicConfig(level=level)
    logger = logging.getLogger(__name__)






async def system_status(session):
    resp = send_public_request(session,
                            '/wapi/v3/systemStatus.html')
    return resp

async def system_status_sapi(session):
    resp = send_public_request(session,
                            '/sapi/v1/system/status')
    return resp


async def testing():
    async with aiohttp.ClientSession() as session:
        system_status(session)
        system_status_sapi(session)

    


def main():
    parser = parse_arguments()
    args = parser.parse_args()
    set_logging_level(args.log)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(testing())



if __name__ == "__main__":
    main()











