from flask import Flask
from db.data import get_tweets, get_top10_tweets_by_likes, get_tweets_by_time
from api import generate_json
from twitter_bot.bot import get_tweets_from_twitter, tweets_to_df


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/api/all')
def all_tweets():
    return generate_json(get_tweets())
    
@app.route('/api/top10likes')
def top10_likes():
    return generate_json(get_top10_tweets_by_likes())

@app.route('/api/orderbytime')
def orderbytime():
    return generate_json(get_tweets_by_time())

@app.route('/api/insert')
def more_tweets():
    tweets = get_tweets_from_twitter()
    tweets_to_df(tweets)
    return "new data get"

    

if __name__ == '__main__':
    app.run(debug=True)

