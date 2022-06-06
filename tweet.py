#%%
import tweepy
# %%
#API Key/Consumer Key HzTuGauYtjR72ZFWdXBD3CaIk

#API Key Secret rL0nKJPIZ1z7P8jG09Ywe1LO56fU76xfKl4e1XpEqlUxP3czLf

#Bearer Token AAAAAAAAAAAAAAAAAAAAANyFcwEAAAAApSs8L32ixPdM1vWzlSt4nqxSWH8%3DMCupcxBhf04ePLh25CZm3txzguaxNrbDJnbG9cMIDVN0p6xaoO

#Client ID

#ZzltNWtRcjYtRXEwazVvZ2tTS3k6MTpjaQ

#Client Secret

#4AiLjIXsygBEdxsQUsjd3t2uG6pwCR_NGdoQnJ6-puPozMmXHp
# Authenticate to Twitter
auth = tweepy.OAuthHandler("HzTuGauYtjR72ZFWdXBD3CaIk", "rL0nKJPIZ1z7P8jG09Ywe1LO56fU76xfKl4e1XpEqlUxP3czLf")
auth.set_access_token("ZzltNWtRcjYtRXEwazVvZ2tTS3k6MTpjaQ", "4AiLjIXsygBEdxsQUsjd3t2uG6pwCR_NGdoQnJ6-puPozMmXHp")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")
# %%
import tweepy
import json
from random import randint

auth = tweepy.OAuthHandler("HzTuGauYtjR72ZFWdXBD3CaIk", "rL0nKJPIZ1z7P8jG09Ywe1LO56fU76xfKl4e1XpEqlUxP3czLf")
auth.set_access_token("ZzltNWtRcjYtRXEwazVvZ2tTS3k6MTpjaQ", "4AiLjIXsygBEdxsQUsjd3t2uG6pwCR_NGdoQnJ6-puPozMmXHp")
#auth = tweepy.OAuthHandler(<your tweepy_api_key>, <your tweepy_api_secret_key>)
#auth.set_access_token(<your tweepy_access_token>, <your tweepy_token_secret>)
api = tweepy.API(auth)

with open("kafka.json", "r") as f:
    c = json.load(f)
for k in c:
    if str(k) == str(randint(1,5)):
        tweet = c[k]
api.update_status(tweet)
# %%
