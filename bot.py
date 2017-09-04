#!/usr/bin/python

import tweepy
from keys import *
from sys import exit
import random

def getManPlace():
    shitfile = open("used.txt","r")
    placefile = open("source.txt","r")
    shitlist = shitfile.read().split("\n")
    placelist = placefile.read().split("\n")
    shitfile.close()
    placefile.close()
    check = True
    while check:
        choice = random.choice(placelist)
        if not (choice in shitlist):
            shitfile = open("used.txt","a")
            shitfile.write(choice+"\n")
            return(choice)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitter = tweepy.API(auth)

twitter.update_status()
