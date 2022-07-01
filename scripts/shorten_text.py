

#%%
import requests
from bs4 import BeautifulSoup
import datefinder
import pandas as pd
from nltk.tokenize import sent_tokenize

import tweepy
#%%
def join_tweet_or_less(lst, limit=280):
    """
    Takes in lst of strings and returns join of strings
    up to `limit` number of chars (no substrings)

    :param lst: (list)
        list of strings to join
    :param limit: (int)
        optional limit on number of chars, default 50
    :return: (list)
        string elements joined up until length of 50 chars.
        No partial-strings of elements allowed.
    """
    for i in range(len(lst)):
        new_join = lst[:i+1]
        if len(' '.join(new_join)) > limit:
            return lst[:i]
    return lst

#%%
final = pd.read_csv('/Users/hannahbohle/Documents/twitterbot/data/kafka_parsed.txt')

#%%
final.drop(columns=final.columns[0], 
        axis=1, 
        inplace=True)

#%%
short = final.reset_index().head(10)
# %%
result = []
for txt in final['Text']:
    z = txt.lstrip('., ') # strips leading character dot, comma, and space
    x = sent_tokenize(z,language='german') # tokenize text into sentences
    y = join_tweet_or_less(x) # join sentences together until >280 characters long
    print(len(y),y)
    result.append(y)

final["tweet"] = result 


# %%
pd.set_option('display.max_colwidth', None)

final.head()
# %%
