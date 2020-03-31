# CySecbot_auto.py file
#Author  : 	SofianeHamlaoui
#Github  : 	https://github.com/SofianeHamlaoui
#Twitter : 	https://twitter.com/S0fianeHamlaoui

import tweepy
import sys
import logging
import json
import os 

# change to your own keys

consumer_key = $consumer_key
consumer_secret = $consumer_secret
access_token = $access_token
access_token_secret = $access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

try:
    api.verify_credentials()
    logger.info(" \033[0;32mAuthentication OK\033[0m")
except:
    logger.info(" \033[0;31mError during authentication\033[0m")
    sys.exit(0)

searching = "(#cybersecurity OR #pentesting OR #security OR #infosec OR #linux OR #Bugbountytip OR #bugbountytips OR #malware OR #hacking OR #frida)" # change to your own queries

for tweet in api.search(q=searching, lang="en", count=100, tweet_mode='extended', result_type='recent', include_entities=1):
    try:
        # uncomment the below line to retweet without comment
        #tweet.retweet()
        
        #tweettext = str(tweet.full_text) # uncomment and use this if you want to show the tweet text
        api.update_status("@S0fianeHamlaoui RT/ : https://twitter.com/" + tweet.user.screen_name + "/status/" + str(tweet.id))
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
