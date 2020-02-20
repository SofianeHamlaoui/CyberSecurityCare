# get_token.py file
# To get "Access Token & Access Token Secret" to use the bot with another account
#Author  : 	SofianeHamlaoui
#Github  : 	https://github.com/SofianeHamlaoui
#Twitter : 	https://twitter.com/S0fianeHamlaoui

import tweepy

consumer_key = input('Your Consumer Key : ')
consumer_secret = input('Your Consumer Secret : ')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
print(auth.get_authorization_url())

verify = input('Verification code : ')

auth.request_token = {
    'oauth_token': auth.request_token['oauth_token'],
    'oauth_token_secret': verify
}

auth.get_access_token(verify)
print(f"Access Token : {auth.access_token}")
print(f"Access Token_Secret : {auth.access_token_secret}")