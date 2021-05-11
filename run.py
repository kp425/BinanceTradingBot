from utils import send_public_request, \
            send_signed_request, live_data, run_test

import json
import argparse
import logging

def get_accountinfo():
    r = send_signed_request("GET",'/api/v3/account')
    print(r)


def place_order():

    params = {
    "symbol": "BNBUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 1,
    "price": "20",
    "recWindow":"20000"
    }
    response = send_signed_request('POST', '/api/v3/order', params)
    print(response)


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

def main():

    parser = parse_arguments()
    args = parser.parse_args()
    set_logging_level(args.log)
    run_test()



if __name__ == "__main__":
    main()

   




    


