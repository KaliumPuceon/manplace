# Man Place Bot
This is a bot that lists all the many, many places you may find a man when he's
not in his Man Cave. I made this using the pretty awesome
[Tweepy](http://www.tweepy.org/) twitter library for python.

The `sources.txt` file has all the wiki pages I scraped to
put this together, and there's also some links down below.

# Authentication
If you want to run this, first make sure you have (ugh) python 2, and install
tweepy with `pip install tweepy` or whatever you want. Clone this repo to where
you want it, then open up the `keys_example.py` file and drop in your own auth
keys. You can get these by registering an app on twitter's app platform thing.
Change the title of `keys_example.py` to `keys.py` and the bot will be able to
read them from there.

# Sources
1. [list of human habitation forms](https://en.wikipedia.org/wiki/List_of_human_habitation_forms)
1. [list of house types](https://en.wikipedia.org/wiki/List_of_house_types)
1. [list of building types](https://en.wikipedia.org/wiki/List_of_building_types)
1. [list of non-building structures](https://en.wikipedia.org/wiki/Nonbuilding_structure)
