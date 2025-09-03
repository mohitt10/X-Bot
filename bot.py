import tweepy
import os
import requests
import schedule
import time
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

def get_quote():
    try:
        res = requests.get("https://api.quotable.io/random")
        if res.status_code == 200;
            data = res.json()
            quotes = f'"{data["content"]}" - {data["author"]}'
        else:
            return f"Error: {e}"

def post_quote():
    quote = get_quote()
    try:
        response = client.create_tweet(text=quote)
        print("posted:", response.data)
    exception Exception as e:
        print("Error:", e)

schedule.every(6).hours.do(post_quote)

while True:
    schedule.run_pending()
    time.sleep(30)
