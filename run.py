from utils import send_public_request, \
            send_signed_request, live_data


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
    "price": "20"
    }
    response = send_signed_request('POST', '/api/v3/order', params)
    print(response)

place_order()







