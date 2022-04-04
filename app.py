from flask import Flask, url_for
from db.data import get_tweets, get_top10_tweets_by_likes, get_tweets_by_time, insert, start, stop
from api import generate_json
from twitter_bot.bot import get_tweets_from_twitter, tweets_to_df


app = Flask(__name__)

#@app.route('/')
#def index():
#    return '<h1>Hello World!</h1>'

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    
    html = "<ul>"
    for url, endpoint in links:
        html += "<li><a href="+url+">"+endpoint+"</a></li>"
    html += "</ul>"
    return html
    # links is now a list of url, endpoint tuples    
# https://stackoverflow.com/questions/13151161/display-links-to-new-webpages-created/13161594#13161594

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

