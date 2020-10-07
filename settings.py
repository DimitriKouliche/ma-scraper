# settings.py
import os

import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pathlib import Path  # Python 3.6+ only

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
BASE_SCRAPING_URL = "https://www.meilleursagents.com/annonces/achat/search/"
CONNECT_URL = "https://www.meilleursagents.com/_signin?show=signin"
MA_USERNAME = os.getenv("MA_USERNAME")
MA_PASSWORD = os.getenv("MA_PASSWORD")
SQLALCHEMY_CONNECTION_STRING = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
psql_engine = create_engine(SQLALCHEMY_CONNECTION_STRING)
Session = sessionmaker(bind=psql_engine)
web_session = requests.Session()
