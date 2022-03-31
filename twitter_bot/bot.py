
import tweepy
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

def getTweets():

    query = '#Ukraine'
    start_time = '2022-03-30T00:00:01Z'
    print("connecting to twitter...")
    client = tweepy.Client(os.environ.get('BEARER'))

    
    tweet_fields=['attachments','author_id','context_annotations','created_at','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','source','text','withheld']
    expansions='referenced_tweets.id'
    print("searching for tweets with hashtag: " + query)
    tweets = ""
    tweets = tweepy.Paginator(client.search_recent_tweets, query=query, start_time = start_time,tweet_fields = ['attachments','author_id','context_annotations','created_at','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','source','text','withheld'], expansions = expansions).flatten(limit=100)
    print("search complete")
    return tweets

def tweetsToDF(tweets):

    list_tweets = [tweet for tweet in tweets]
    i = 1 

    df = pd.DataFrame(columns=[
        'id',
        'text',
        'created_at',
        #'hashtags',
        'lang',
        'source',
        'retweet_count',
        'reply_count',
        'like_count',
        'quote_count',

    ])

    for tweet in list_tweets:
        
        id = i
        text = tweet.text
        created_at = tweet.created_at
        #hashtags = tweet.entities['hastags']
        lang = tweet.lang
        source = tweet.data['source']
        retweets = tweet.public_metrics['retweet_count']
        replies = tweet.public_metrics['reply_count']
        likes = tweet.public_metrics['like_count']
        quotes = tweet.public_metrics['quote_count']
        i = i+1

        ith_tweet = [id, text, created_at, lang, source, retweets, replies, likes, quotes]

        df.loc[len(df)] = ith_tweet
    print("inserting data to file")        
    df.to_csv('test.csv')


if __name__ == '__main__':
    print("getting program")
    tweets = getTweets()
    tweetsToDF(tweets)
    print("program complete")

