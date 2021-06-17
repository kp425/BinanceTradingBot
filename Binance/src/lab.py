import asyncio
import json
import argparse
import logging

from utils.http_async import send_public_request, \
                            send_signed_request
from utils.stream import get_LiveData
from utils.common import setup_logging, prettify, debug_logs


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
    # params = {
    # "symbol": "BNBUSDT",
    # "side": "BUY",
    # "type": "LIMIT",
    # "timeInForce": "GTC",
    # "quantity": 1,
    # "price": "20",
    # "recWindow":"20000"
    # }

    params = {
    "symbol": "ETHBTC",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 0.001,
    "price": "2000",
    # "recWindow":"20000"
    }

    resp = await send_signed_request(session,'POST', '/api/v3/order', 
                                                params, return_type="json") 
    return resp


async def get_all_orders(session):
    params = {'symbol':"LTCBTC"}
    resp = await send_signed_request(session,'GET',
                                '/api/v3/allOrders', params, return_type="json")
    
    return resp
    












