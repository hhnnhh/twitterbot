#%%
import tweepy
import pandas as pd
from datetime import date
import json


#%%
today = date.today().strftime('%m-%d')
heute = str(today)
print("Today's date:", heute)


#%%
entry = pd.read_json('/Users/hannahbohle/Documents/twitterbot/data/tweetlength_short.json')

#%%
# check if date is todays date, if so, then prepare todays tweet
# hier noch einbauen: 
# nur im Jahr 2010 suchen und wenn das Datum matcht, dann tweeten
# sonst, tue nichts
#finaltweet = entry.loc[entry['date'] == '07-10', 'finaltweet'].iloc[0]
finaltweet = entry.loc[entry['date'] == today, 'finaltweet'].iloc[0]


print(finaltweet)

# %%
# Access
# https://developer.twitter.com/en/portal/projects/1528471243594338305/apps/24348124/keys
# https://docs.tweepy.org/en/stable/examples.html


#API Key/Consumer Key 
consumer_key = "VoZsLqjjq5UOckBU9duYji9H3"

#API Key Secret 
consumer_secret = "1W03zh1ckf2vBddVTyXxPm30nb6ceUl5o4t67XWutKGwCXRjKF"

#Bearer Token 
bearer_token = "AAAAAAAAAAAAAAAAAAAAANyFcwEAAAAAvfpFYp%2BXqSIRbbv2L4Us7Ka4NXI%3DsgLvBaiICPOhc0Qz7PpQhSkoLHKM6qkDLD56lqhSUNYCj0T1dI"

#Client ID ZzltNWtRcjYtRXEwazVvZ2tTS3k6MTpjaQ

# Access Token Secret 
access_token_secret = "eSPYT2Ms2JlnRLJeK5H6XAvAlx4nAQgq51qEwfWwVF2j9"

# Access Token 
access_token = "1528440001251446786-zIkYzkVW03G2VFM98ie1YdPpvWygMb"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

#api.update_status("1. Juli. Der Wunsch nach besinnungsloser Einsamkeit. Nur mir gegenübergestellt sein. Vielleicht werde ich es in Riva haben. Vorvorgestern mit Weiß, Verfasser der 'Galeere'. Jüdischer Arzt, Jude von der Art, (...) dem man sich (...) gleich nahe fühlt.")
api.update_status(finaltweet)
# %%
