import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = os.path.join(dirname(__file__), 'env/dev.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")
