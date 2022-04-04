
import tweepy
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

def get_tweets_from_twitter():

    query = '#Ukraine'
    #start_time = '2022-03-30T00:00:01Z'
    print("connecting to twitter...")
    client = tweepy.Client(os.environ.get('BEARER'))

    
    tweet_fields=['attachments','author_id','context_annotations','created_at','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','source','text','withheld']
    expansions='referenced_tweets.id'
    print("searching for tweets with hashtag: " + query)
    tweets = ""
    tweets = tweepy.Paginator(client.search_recent_tweets, query=query,''' start_time = start_time,'''tweet_fields = ['attachments','author_id','context_annotations','created_at','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','source','text','withheld'], expansions = expansions)#.flatten(limit=5000)
    print("search complete")
    return tweets

def tweets_to_df(tweets):

    list_tweets = [tweet for tweet in tweets]
    i = 1 
    """
    df = pd.DataFrame(columns=[
        
        'text',
        'created_at',
        #'hashtags',
        'lang',
        'source',
        'retweets',
        'replies',
        'likes',
        'quotes',

    ])
    """
    lists=[]
    for tweet in list_tweets:
        
        print(tweet)
        id = tweet.id
        text = tweet.text
        created_at = tweet.created_at
        lang = tweet.lang
        source = tweet.data['source']
        retweets = tweet.public_metrics['retweet_count']
        replies = tweet.public_metrics['reply_count']
        likes = tweet.public_metrics['like_count']
        quotes = tweet.public_metrics['quote_count']

        ith_tweet =[{
        "id" : id,
        "text" : text, 
        "created_at" : created_at, 
        "lang" : lang, 
        "source": source,
        "retweets" : retweets, 
        "replies" : replies, 
        "likes" : likes, 
        "quotes" :quotes
        }]
        lists.append(ith_tweet)
        i = i+1

    print(lists)
    print("inserting data to file")  
    return lists      


if __name__ == '__main__':
    print("getting program")
    tweets = get_tweets_from_twitter()
    tweets_to_df(tweets)
    print("program complete")

