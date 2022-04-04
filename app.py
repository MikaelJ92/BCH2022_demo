from flask import Flask, url_for
from db.data import get_tweets, get_top10_tweets_by_likes, get_tweets_by_time, insert, start, stop
from api import generate_json
from twitter_bot.bot import get_tweets_from_twitter, tweets_to_df


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

app.route("/all_links")
def all_links():
    links = []
    for rule in app.url_map_iter_rules():
        if len(rule.defaults) >= len(rule.arguments):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    
    print(links)

@app.route('/api/all')
def all_tweets():
    tweets = get_tweets()
    return generate_json(tweets)
    
@app.route('/api/top10likes')
def top10_likes():
    return generate_json(get_top10_tweets_by_likes())

@app.route('/api/orderbytime')
def orderbytime():
    return generate_json(get_tweets_by_time())

@app.route('/api/insert')
def more_tweets():
    session = start()
    tweets = get_tweets_from_twitter()
    df = tweets_to_df(tweets)
    for data in df:
        for tweet in data:
            insert(
                    tweet["id"],
                    tweet["text"],
                    tweet["created_at"],
                    tweet["lang"],
                    tweet["source"],
                    tweet["retweets"],
                    tweet["likes"],
                    tweet["quotes"],
                    session
            )
    
    stop(session)
    return "<h1> data insert successful</1>"
    

if __name__ == '__main__':
    app.run(debug=True)

