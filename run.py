from utils import send_public_request, \
            send_signed_request, live_data, setup_logging

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



def main():
    parser = parse_arguments()
    args = parser.parse_args()
    setup_logging(args.log)




if __name__ == "__main__":
    main()

   




    


