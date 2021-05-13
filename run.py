from settings import config
import asyncio
import aiohttp
import json
import argparse
import logging
from lab import get_accountinfo, system_status, \
                system_status_sapi, place_order


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-log", 
                        "--log",
                        default="warning",
                        help=("Provide logging level. "
                              "Example --log debug', default='warning'"))

    return parser



def main():
    parser = parse_arguments()
    args = parser.parse_args()
    if args.log:
        log_level = args.log
    else:
        log_level = config.LOG_LEVEL
    setup_logging(log_level)

    with aiohttp.ClientSession() as session:

        t = get_accountinfo(session)
        


    


if __name__ == "__main__":
    main()

   




    


