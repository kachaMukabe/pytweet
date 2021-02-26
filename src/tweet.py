import requests
import os
import json
import pprint
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
load_dotenv()


auth = OAuth1(os.environ["APP_KEY"], os.environ["APP_SECRET"], os.environ["OAUTH_TOKEN"], os.environ["OAUTH_TOKEN_SECRET"])
headers = {'Authorization': f'Bearer {os.environ["BEARER_TOKEN"]}'}

def tweet(tweet):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    payload = {'status': tweet}
    response = requests.post(url, params=payload, auth=auth)
    if response.status_code == 200:
        return "Tweeted"
    return "Failed to tweet"

def retweet(tweet_id):
    url = f"https://api.twitter.com/1.1/statuses/retweet/{tweet_id}.json" 
    response = requests.post(url, auth=auth)

def like(tweet_id):
    url = f"https://api.twitter.com/1.1/favorites/create.json" 
    payload = {'id':tweet_id}
    response = requests.post(url, params=payload, auth=auth)

def timeline():
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
    payload = {'count': 15}
    response = requests.get(url, auth=auth, params=payload)
    if response.status_code == 200:
        return response.json()
    return []

def mentions():
    url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"
    payload = {'count': 8}
    response = requests.get(url, auth=auth, params=payload)
    if response.status_code == 200:
        return response.json()
    return []

def retweets():
    url = "https://api.twitter.com/1.1/statuses/retweets_of_me.json"
    payload = {'count': 8}
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        return response.json()


def user_info():
    url = "https://api.twitter.com/1.1/account/verify_credentials.json"
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        return response.json()
    return None

def sample():
    url = f"https://stream.twitter.com/1.1/statuses/sample.json"
    response = requests.get(url, auth=auth, stream=True)
    if response.encoding is None:
        response.encoding = 'utf-8'
    for line in response.iter_lines():
        if line:
            pprint.pprint(json.loads(line), indent=2)
            print('\n')

def statuses():
    url = "https://stream.twitter.com/1.1/statuses/filter.json"
    payload = {'track': 'python'}
    response = requests.post(url, auth=auth, params=payload, stream=True)
    if response.encoding is None:
        response.encoding = 'utf-8'
    for line in response.iter_lines():
        if line:
            json_res = json.loads(line)
            print(json.dumps(json_res, indent=4, sort_keys=True))

    

def stream():
    url = f"https://api.twitter.com/2/tweets/search/stream"
    response = requests.get(url, headers=headers, stream=True)
    if response.encoding is None:
        response.encoding = 'utf-8'
    for line in response.iter_lines():
        print(line)
        if line:
            print(json.loads(line))
    