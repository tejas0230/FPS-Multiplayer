import random
import re
import tweepy
import requests
import time

def gen():
    gen_tweet_ids = open('links', 'r', encoding="utf8").read().split()
    save = open('save', 'w')
    List = []

    for f in gen_tweet_ids:
        x = re.findall('(\w+)://([\w\-\.]+)/(\w+).(\w+)/(\d*)', f)
        if (x):
            List.append(x)

    for abc in List:
        print(abc[0][4])
        if (len(abc[0][4]) == 19):
            save.write(abc[0][4] + "\n")

gen()

api_keys = 'YOUR_API_KEY'
api_secret = 'YOUR_API_KEY_SERCET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
bearer = 'YOUR_BEARER_TOKEN'


try:
    client = tweepy.Client(consumer_key=api_keys, consumer_secret=api_secret, bearer_token=bearer,access_token=access_token, access_token_secret=access_token_secret)
    all_id = open('save','r').read().splitlines()
    for f in all_id:
        client.like(f)
        print("Liked")
        time.sleep(random.randint(5,25))
    print("Everything works")
except:
    print("Something went wrong")



