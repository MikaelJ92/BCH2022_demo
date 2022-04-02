import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

engine = sqlalchemy.create_engine(os.environ.get('DATABASE'))
Session = sessionmaker(bind=engine)