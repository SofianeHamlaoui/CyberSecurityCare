# Config.py file
#Author  : 	SofianeHamlaoui
#Github  : 	https://github.com/SofianeHamlaoui
#Twitter : 	https://twitter.com/S0fianeHamlaoui

# Set EnvVar : export $VARNAME=""

import tweepy # I use Tweepy, you can find all the links and documentations on the Github repo,
import logging # using "import logging" for error logs
import os # I "import os" to use "os.getenv()" to get environment variables

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY") # export CONSUMER_KEY="KEY"
    consumer_secret = os.getenv("CONSUMER_SECRET") # export CONSUMER_SECRET="KEY"
    access_token = os.getenv("ACCESS_TOKEN") # export ACCESS_TOKEN="KEY"
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET") # export ACCESS_TOKEN_SECRET="KEY"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api