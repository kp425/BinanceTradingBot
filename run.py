from settings import config
import requests
import asyncio
import hashlib
import hmac

API_KEY = config.API_KEY
SECRET_KEY = config.SECRET_KEY
API_URL = config.API


def get_signature():
    hashedsig = hashlib.sha256(SECRET_KEY)


def get_headers():
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',  # noqa
        }
        if config.API_KEY:
            assert API_KEY
            headers['X-MBX-APIKEY'] = API_KEY
        return headers

url = API_URL + "/v3/account"
print(url)
resp = requests.get(url, headers=get_headers(),
                params=dict(symbol="ETHBUSD"))
print(resp.json())

# r = requests.get("https://api.binance.com/api/v3/depth",
#                  params=dict(symbol="ETHBUSD"))
# results = r.json()

# print(r)
# print(results)