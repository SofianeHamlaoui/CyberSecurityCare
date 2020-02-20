# CySecbot_user.py file
# user -> askes for input 
               # 1)  searching = the search query/queries
               # 2)  numberOfTweets = number of tweets to retweet
#Author  : 	SofianeHamlaoui
#Github  : 	https://github.com/SofianeHamlaoui
#Twitter : 	https://twitter.com/S0fianeHamlaoui

import tweepy
import sys
import logging
import json
import os 

consumer_key = os.getenv("CONSUMER_KEY") # export CONSUMER_KEY="KEY"
consumer_secret = os.getenv("CONSUMER_SECRET") # export CONSUMER_SECRET="KEY"
access_token = os.getenv("ACCESS_TOKEN") # export ACCESS_TOKEN="KEY"
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET") # export ACCESS_TOKEN_SECRET="KEY"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
numberOfTweets = input("How many Tweets you want to RT ? : ")

try:
    api.verify_credentials()
    logger.info(" \033[0;32mAuthentication OK\033[0m")
except:
    logger.info(" \033[0;31mError during authentication\033[0m")

if (len(sys.argv) > 1):
    searching = sys.argv[1:]
else:
    print("""Please provide a a query, 

Usage : \033[0;32mpython CySecbot.py "queries"\033[0m

Example :  \033[0;34mpython CySecbot.py "#CyberSecurity, Pentest"\033[0m

Check this link to know how Twitter Queries (operators) work : \033[0;34mhttps://t.co/XBM05DGSGj\033[0m
  """)
    sys.exit(0)

for tweet in api.search(q=searching, lang="en", count=numberOfTweets, tweet_mode='extended', result_type='recent', include_entities=1):
    try:
        # retweet with comment : ( uncomment the 2 lines below)

        #tweettext = str(tweet.full_text) # Add this if you want to show the tweet text
        #api.update_status("@S0fianeHamlaoui RT @" + tweet.user.screen_name + " https://twitter.com/" + tweet.user.screen_name + "/status/" + str(tweet.id)) # this will retweet with comment 
        tweet.retweet() # This will retweet the tweets without a comment 
        print("\n###################################################################")
        print("Retweeted the tweet of @" + tweet.user.screen_name + " > \033[0;32mSuccessfully\033[0m")
        print(f"URL : https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}\n")
        os.system("sleep 1")
    except tweepy.TweepError as e:
        if (e.args[0][0]['message']) == "Status is a duplicate.":
            print("Tweet Already Retweeted\n")
        else:
            print(e.args[0][0]['message'] +"\n")
            os.system("sleep 1")

