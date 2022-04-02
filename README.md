# BCH2022_demo

## About
This is a demo project for Code Bootcamp Häme 2022. The goal for this project was to build a demo website with Python and explore the deployment process of web applications. The project contains three main parts:
 - a script/bot that gets recent tweets from twitter with given hashtag.
 - Backend done with Python's Flask
 - And simple frontend


## Installation

- Git clone this repository:

```
git clone

```
- To use the twitter bot, you need to create a twitter developer account and create an APIv2 Bearer token.
- you need to make a .env file and add two environmental variables

```
BEARER = {your Twitter Bearer token}

DATABASE = {link to your database} 
```

- make virtual environment for the project

```
pip install virtualenv

python -m virtualenv venv

source venv/Scripts/activate

```

- install required modules

```
pip install -r requirements.txt

```

- run the twitter bot and csv2db from your project folder
```
python twitter_bot/bot.py
python csv2db.py

```