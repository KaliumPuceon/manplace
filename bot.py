#!/usr/bin/python

# example crontab entry:
# 0 0,4,8,12,16,20 * * * cd /home/kalium/bots/manplace; ./bot.py
# ofc, replace that with the path you put this junk in

import tweepy
from keys import *
import random

# They're all prefixes 'cos that's way easier to read on twitter
# DISCLAIMER: I have no idea what is meant to happen in a man cave

prefix_list = ([
    "I've just finished setting up my man ",
    "I moved all my sports stuff into my man ",
    "You should come over to my man ",
    "I bought a bunch of drinks for my man ",
    "I just bought a new thing for my man ",
    "Can you come help me set up my man ",
    "I want to  get away from it all in my man ",
    "I have to replace all the batteries in my man ",
    "I have some concerns about the structural integrity of my man ",
    "Only TRUE MEN are allowed in the man ",
    "Prove your mettle and I will give you the password to the man ",
    "We installed these locks to secure the man ",
    "I'm hosting tonight's ritual at my man ",
    "I'm holding a part to christen my new man ",
    "Have you seen Chad's new man ",
    "They say that Eric isn't letting anyone see the inside of his man ",
    ])

def getManPlace():
    deadfile = open("used.txt","r")
    placefile = open("source.txt","r")
    deadlist = deadfile.read().split("\n")
    placelist = placefile.read().split("\n")
    deadfile.close()
    placefile.close()
    check = True
    while check:
        choice = random.choice(placelist)
        if not (choice in deadlist):
            deadfile = open("used.txt","a")
            deadfile.write(choice+"\n")
            return(choice)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitter = tweepy.API(auth)

twitter.update_status(random.choice(prefix_list)+getManPlace().lower())
