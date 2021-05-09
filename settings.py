import os
from os.path import join, dirname
from dotenv import load_dotenv


dev_config = {

}

class LoadConfig:
    def __init__(self, env_path):
        self.env_path = env_path 
        load_dotenv(env_path)
        self.API_KEY = os.environ.get("API_KEY")
        self.SECRET_KEY = os.environ.get("SECRET_KEY")
        self.API = os.environ.get("API")
        self.WS = os.environ.get("WS")
        self.STREAM = os.environ.get("STREAM")

dev = True 

if dev:
    dev_path = os.path.join(dirname(__file__), 'env/dev.env')
    config = LoadConfig(dev_path)
else:
    prod_path = os.path.join(dirname(__file__), 'env/prod.env')
    config = LoadConfig(prod_path)








