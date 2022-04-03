from urllib import response
from flask import jsonify, abort

def generate_json(tweets):
    data = []
    line = 0

    for tweet in tweets:
        line += 1
        data.insert(line, {
        "text" : tweet.text,
        "created_at" : tweet.created_at,
        "lang" : tweet.lang,
        "source" : tweet.source,
        "retweets" : tweet.retweets,
        "likes" : tweet.likes,
        "quotes" : tweet.quotes
        })

    response = jsonify({'data' : data})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response