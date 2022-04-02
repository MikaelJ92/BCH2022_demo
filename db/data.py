from flask import session
from .schema import Tweet
from . import Session

def start():
    session = Session()
    return session

def stop(session):
    session.commit()
    session.close()

#def insert(text, created_at, lang, source, retweet_count, like_count, quote_count, session):
#    session.add(Tweet(text = text, created_at = created_at, lang = lang, source = source, retweet_count = retweet_count, like_count = like_count, quote_count = quote_count))

def insert(data_fr):
    Tweet.add2db(data_fr)  


def get_tweets():
    session = Session()
    tweets = session.query(Tweet).limit(1000).all()

    return tweets

#text, created_at, lang, source, retweet_count, like_count, quote_count