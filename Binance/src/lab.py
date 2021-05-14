from utils import send_public_request, \
            send_signed_request, live_data

import asyncio
import json
import argparse
import logging


def _debug_logs(*args):
    pass

async def get_accountinfo(session):
    resp = await send_signed_request(session, "GET",
                                '/api/v3/account')
    return resp


#returning 404
async def system_status(session):   
    # resp = await send_public_request(session,
    #                 '/wapi/v3/systemStatus.html',
    #                 return_type="text")
    resp = await send_signed_request(session,'GET',
                    '/wapi/v3/systemStatus.html',
                    return_type="text")
    return resp


async def system_status_sapi(session):
    resp = await send_public_request(session,
                           '/sapi/v1/system/status',
                           return_type="json")
    return resp



async def get_AllCoinInfo(session):

    # params = {'recvWindow':5000}
    params = {}
    resp = await send_signed_request(session,'GET',
                    '/sapi/v1/capital/config/getall', 
                    payload= params,
                    return_type="text")

    return resp



async def place_order(session):
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


async def get_all_orders(session):
    params = {'symbol':"LTCBTC"}
    resp = await send_signed_request(session,'GET',
                                '/api/v3/allOrders', params, return_type="json")
    
    return resp
    

async def get_AccountInfo(session):
    resp = await send_signed_request(session,'GET',
                                '/api/v3/account', return_type="json")
    
    return resp

async def get_MyTrades(session):
    params = {'symbol': 'LTCBNB'}
    resp = await send_signed_request(session,'GET',
                                '/api/v3/myTrades', params, return_type="json")
    
    return resp

async def withdraw():
    pass










