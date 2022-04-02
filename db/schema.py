from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, Float, DateTime, Table, Text)
from sqlalchemy import MetaData
import datetime
from . import engine

meta = MetaData()

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets_table'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    created_at = Column(DateTime)
    lang = Column(String)
    source = Column(String)
    retweets = Column(Integer)
    likes = Column(Integer)
    quotes = Column(Integer)

    def __repr__(self):
        return "<Tweet(text='%s', created_at='%s', lang='%s', source='%s', retweets='%s', likes='%s', quotes='%s')>" % (self.text, self.created_at, self.lang, self.source, self.retweets, self.likes, self.quotes)

    def add2db(data_df):

        data_df.to_sql(
            name ='tweets_table',
            con = engine,
            if_exists ='append',
            index = True,
            chunksize = 100,
            dtype = {'text' : Text,'created_at' : DateTime, 'lang' : String(5), 'source' : Text, 'retweet_count' : Integer,'like_count' : Integer,'quote_count' : Integer})

    