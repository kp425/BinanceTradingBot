import aiohttp
import asyncio
from .common import setup_logging
from .http_async import send_public_request, \
                        send_signed_request

async def test():

    coroutines = []

    async with aiohttp.ClientSession() as session:

        # get klines
        klines = send_public_request(session, '/api/v3/klines' , {"symbol": "BTCUSDT", "interval": "1d"})

        ### USER_DATA endpoints, call send_signed_request #####
        # get account informtion
        # if you can see the account details, then the API key/secret is correct
        account = send_signed_request(session, 'GET', '/api/v3/account')
  
        # # place an order
        # if you see order response, then the parameters setting is correct
        params = {
        "symbol": "BNBUSDT",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": 1,
        "price": "200"
        }
        order = send_signed_request(session, 'POST', '/api/v3/order', params)


        # transfer funds
        params = {
        "fromEmail": "",
        "toEmail": "",
        "asset": "USDT",
        "amount": "0.1"
        }
        sub_transfer = send_signed_request(session, 'POST', '/wapi/v3/sub-account/transfer.html', params)


        # New Future Account Transfer (FUTURES)
        params = {
        "asset": "USDT",
        "amount": 0.01,
        "type": 2
        }
        transfer = send_signed_request(session, 'POST', '/sapi/v1/futures/transfer', params)
        coroutines = [klines, account, order, sub_transfer, transfer]
        tasks = await asyncio.gather(*coroutines)

    return tasks


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', default='debug')
    args = parser.parse_args()
    if args.log:
        setup_logging(args.log)
    asyncio.run(test())