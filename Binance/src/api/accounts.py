from utils import send_signed_request, send_public_request

async def get_AccountInfo(session):
    resp = await send_signed_request(session,'GET',
                                '/api/v3/account', return_type="json")
    
    return resp


async def get_MyTrades(session):
    params = {'symbol': 'LTCBNB'}
    resp = await send_signed_request(session,'GET',
                                '/api/v3/myTrades', params, return_type="json")
    
    return resp

async def get_MyAddress(session):

    params = {'asset': 'BTC'}
    resp = await send_signed_request(session,'GET',
                                '/sapi/v1/capital/deposit/address', 
                                params, return_type="bytes")
    
    return resp


async def get_AllAssets(session):
    resp = await send_signed_request(session,'GET',
                                '/sapi/v1/capital/config/getall', 
                                return_type="json")
    return resp


async def withdraw(session):
    params = {'coin': 'LTC', 
              'address': '',
              'amount':0.1}
    resp = await send_signed_request(session,'GET',
                                '/api/v3/myTrades', params, return_type="json")
    
    return resp
