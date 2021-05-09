from utils import send_public_request, send_signed_request
import json

# response = send_signed_request('GET', '/v3/account')
# print(json.dumps(response, indent=1))

# response = send_public_request('/v3/exchangeInfo')

# print(json.dumps(response, indent=2))

# params = {  
#             'symbol':'LTCBTC',
#             'side':'BUY',
#             'type': 'LIMIT',
#             'timeInForce':	'GTC',
#             'quantity': 1,
#             'price':  500,
#             'recvWindow':5000
#         }

# response = send_signed_request("POST" , '/v3/order', params)

try:
    response = send_public_request('/v3/userDataStream')
except e:
    print(e)
response = send_signed_request('POST', '/v3/userDataStream')
print(response)




