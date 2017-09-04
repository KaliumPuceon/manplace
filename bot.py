#!/usr/bin/python3

import tweepy
from keys import *
from sys import exit

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitter = tweepy.API(auth)

twitter.update_status(status="Test Twitter Post from API: Limited Edition")
