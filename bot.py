import tweepy
import os
import requests
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
        res = requests.get("http://api.quotable.io/quotes/random", timeout=10)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, list) and len(data) > 0:
            data = data[0]
        return f'"{data["content"]}" - {data["author"]}'
    except Exception as e:
        return None

def post_quote():
    quote = get_quote()
    try:
        response = client.create_tweet(text=quote)
        print("posted:", response.data)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    post_quote()
