from utils import send_public_request, \
            send_signed_request, live_data

import asyncio
import json
import argparse
import logging


def _debug_logs(*args):
    pass

def get_accountinfo(session):
    coro = send_signed_request(session, "GET",
                                '/api/v3/account')
    task = asyncio.create_task(coro)
    return task


async def system_status(session):
    resp = await send_public_request(session,
                            '/wapi/v3/systemStatus.html')
    _debug_logs(resp.status, await resp.read())
    return resp

async def system_status_sapi(session):
    # resp = send_public_request(session,
    #                         '/sapi/v1/system/status')
    resp = await send_public_request(session,
                            '/sapi/v1/system/status')
    _debug_logs(resp.status, await resp.read())
    return resp


def place_order(session):
    params = {
    "symbol": "BNBUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 1,
    "price": "20",
    "recWindow":"20000"
    }
    resp = await send_signed_request('POST', '/api/v3/order', params) 
    return resp













