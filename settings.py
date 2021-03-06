import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SECRET_TOKEN = os.environ.get('SECRET_TOKEN')
CLIENT_ID = os.environ.get('CLIENT_ID')