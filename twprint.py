#!/usr/bin/env puthon
import tweepy
import twkey

CONSUMER_KEY = twkey.key["cons_key"]
CONSUMER_SECRET = twkey.key["cons_sec"]
ACCESS_TOKEN_KEY = twkey.key["acto_key"]
ACCESS_TOKEN_SEC = twkey.key["acto_sec"]

api = tweepy.Api(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token_key=ACCESS_TOKEN_KEY,
    access_token_secret=ACCESS_TOKEN_SECRET
 )

api.update_status("Hello,World!")
"""

"""