from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, Float, DateTime, Table, Text)
from sqlalchemy import MetaData
import datetime
from . import engine

meta = MetaData()

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    created_at = Column(DateTime)
    lang = Column(String)
    source = Column(String)
    retweet_count = Column(Integer)
    like_count = Column(Integer)
    quote_count = Column(Integer)

    def __repr__(self):
        return "<Tweet(text='%s', created_at='%s', lang='%s', source='%s', retweet_count='%s', like_count='%s', quote_count='%s')>" % (self.text, self.created_at, self.lang, self.source, self.retweet_count, self.like_count, self.quote_count)

    def add2db(data_df):


        data_df.to_sql(
            name ='tweets_table',
            con = engine,
            if_exists ='append',
            index = True,
            chunksize = 100,
            dtype = {'text' : Text,'created_at' : DateTime, 'lang' : String(5), 'source' : Text, 'retweet_count' : Integer,'like_count' : Integer,'quote_count' : Integer})
