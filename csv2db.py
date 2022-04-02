from db.data import insert, start, stop
import pandas as pd
from datetime import datetime

session = start()

with open('test.csv','rb') as csvfile:
    reader = pd.read_csv(csvfile,delimiter=',', encoding='utf-8', encoding_errors = 'replace', header=0, names=['id','text', 'created_at', 'lang', 'source', 'retweets', 'replies', 'likes', 'quotes'])
    #line = 0
    #print(reader['text'][1])
    i = 0
    #print(type(pd.to_datetime(reader['created_at'])))
    #date = pd.to_datetime(reader['created_at'])
    #print(date)
    #print(type(date))
    #print(type(datetime.strptime(reader['created_at'],'%y/%m/%d %H:%M:%S')))
    """
    reader['created_at'] = pd.to_datetime(reader['created_at'], format='%Y-%m-%d %H:%M:%S')
    text = reader['text']
    created_at = reader['created_at']
    lang = reader['lang']
    source = reader['source']
    retweet_count = reader['replies']
    like_count = reader['likes']
    quote_count = reader['quotes']
    """
    #print(reader.dtypes)
    #pd.to_sql
    #reader['created_at'] = reader['created_at'].astype('str')
    insert(reader)
    #insert(text = text, created_at = created_at, lang = lang, source = source, retweet_count = retweet_count, like_count = like_count, quote_count = quote_count, session=session)



    #insert(text=reader['text'], created_at=reader['created_at'], lang=reader['lang'], source =reader['source'], retweet_count=reader['replies'], like_count=reader['likes'], quote_count=reader['quotes'],session=session)


    #for row in reader:
    #    print(row[i])
       # i += 1
        #if line != 0:
            #insert(row[2], row[5], session)
     #       print ("row: ")
      #      print(row)
       #     print("--------------")
        #line += 1
 # text, created_at, lang, source, retweets, replies, likes, quotes
stop(session)