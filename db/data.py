from flask import session
from .schema import Tweet
from . import Session

def start():
    session = Session()
    return session

def stop(session):
    session.commit()
    session.close()


def insert(id, text, created_at, lang, source, retweets, likes, quotes, session):

    session.add(Tweet(id= id, text = text, created_at = created_at,
                lang = lang, source = source, retweets = retweets, likes = likes,
                quotes = quotes))

    

def get_tweets():
    session = Session()
    tweets = session.query(Tweet).all()

    return tweets

def get_top10_tweets_by_likes():
    session = Session()
    tweets = session.query(Tweet).order_by(Tweet.likes.desc()).limit(10)

    return tweets

def get_tweets_by_time():
    session = Session()
    tweets = session.query(Tweet).order_by(Tweet.created_at.desc())

    return tweets
