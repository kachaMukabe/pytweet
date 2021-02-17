import requests
import os
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
load_dotenv()


def tweet(tweet):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    auth = OAuth1(os.environ["APP_KEY"], os.environ["APP_SECRET"], os.environ["OAUTH_TOKEN"], os.environ["OAUTH_TOKEN_SECRET"])
    payload = {'status': tweet}
    response = requests.post(url, params=payload, auth=auth)
    print(response)