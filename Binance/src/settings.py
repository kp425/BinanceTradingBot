import os
from os.path import join, dirname
from dotenv import load_dotenv


class DevConfig:
    def __init__(self):
        self.env_path = os.path.join(dirname(__file__), 'env/dev.env')
        if os.path.exists(self.env_path):
            #this condition is to work in colab
            #remove it
            load_dotenv(self.env_path)
        self.API_KEY = os.environ.get("API_KEY")
        self.SECRET_KEY = os.environ.get("SECRET_KEY")
        self.API_URL = "https://testnet.binance.vision"
        self.WS = "wss://testnet.binance.vision/ws"
        self.STREAM = "wss://testnet.binance.vision/stream"

class ProdConfig:
    def __init__(self):
        self.env_path = os.path.join(dirname(__file__), 'env/prod.env')
        load_dotenv(self.env_path)
        self.API_KEY = os.environ.get("API_KEY")
        self.SECRET_KEY = os.environ.get("SECRET_KEY")
        self.API = "https://api.binance.com/api"
        self.WS = "wss://stream.binance.com:9443/ws"
        self.STREAM = "wss://stream.binance.com:9443/stream"    

dev = True 

if dev:
    config = DevConfig()
else:
    config = ProdConfig()







