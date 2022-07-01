

#%%
import requests
from bs4 import BeautifulSoup
import datefinder
import pandas as pd
from nltk.tokenize import sent_tokenize
import numpy as np
import tweepy
#%%
def join_tweet_or_less(lst, limit=268):
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
#reihe 282 muss ich löschen, 16. Februar 2014 ist falsch
conds = [(final.index >= 0) & (final.index <= 21),#10
         (final.index > 22) & (final.index<=108),#11
         (final.index > 109) & (final.index<=186),#12
         (final.index > 187) & (final.index<=235),#13
         (final.index > 236) & (final.index<=326),#14
         (final.index > 327) & (final.index<=376),#15
         (final.index > 377) & (final.index<=498),#16
         (final.index > 399) & (final.index<=431),#17
         (final.index > 426) ] #1919

# Set up your target values (in the same order as your conditions)
choices = ['1910', '1911', '1912', '1913','1914','1915','1916','1917','1919']

final['year'] = np.select(conds, choices)

#%%
final.head()

#%%
final['dairy_date'] = final["Datum"]+" "+final['year']
#%%
final.drop(columns=final.columns[0], 
        axis=1, 
        inplace=True)

#%%
final.drop(columns=['year'],axis=1, inplace=True) # keep Datum for comparison

#%%
#short = final.reset_index().head(10)
# %%
# hier muss ich überlegen, ob ich lange Texte über mehrere Tage tweete oder 
# mehrere Tweets an einem Tag? Das können aber sehr viele werden. Vielleicht mehrere Tweets, aber maximal z.B. 3?
result = []
for txt in final['Text']:
    z = txt.lstrip('., ') # strips leading character dot, comma, and space
    x = sent_tokenize(z,language='german') # tokenize text into sentences
    y = join_tweet_or_less(x) # join sentences together until >280 characters long
    w = ' '.join(y)
    print(len(w),w)
    result.append(w)

final["tweet"] = result 

#%%
final.head(4)

#%%
final["finaltweet"] = final['dairy_date'] +". "+ final['tweet']

# %%
#pd.set_option('display.max_colwidth', None)

final.head(4)

#%%
final = final.reset_index()
#%%
final = final.drop([final.index[3]])
#%%
final.loc[-1] = ['19. Juli','19. Juli 1910','Geschlafen, aufgewacht, geschlafen, aufgewacht, elendes Leben. Oft überlege ich es und lasse den Gedanken ihren Lauf, ohne mich einzumischen, und immer, wie ich es auch wende, komme ich zum Schluß, daß mir in manchem meine Erziehung schrecklich geschadet hat.', '19. Juli 1910. Geschlafen, aufgewacht, geschlafen, aufgewacht, elendes Leben. Oft überlege ich es und lasse den Gedanken ihren Lauf, ohne mich einzumischen, und immer, wie ich es auch wende, komme ich zum Schluß, daß mir in manchem meine Erziehung schrecklich geschadet hat.']  # adding a row
#final.loc[-1] = ['17. Mai','Kometennacht 17./18. Mai 1910','Mit Blei, seiner Frau und seinem Kind beisammengewesen, mich aus mir heraus zeitweilig gehört, wie das Winseln einer jungen Katze beiläufig, aber immerhin.','Kometennacht 17./18. Mai 1910. Mit Blei, seiner Frau und seinem Kind beisammengewesen, mich aus mir heraus zeitweilig gehört, wie das Winseln einer jungen Katze beiläufig, aber immerhin.']
#final.loc[-1] = ['28. Mai','Wieviel Tage sind wieder stumm vorüber; heute ist der 28. Mai. Habe ich nicht einmal die Entschlossenheit, diesen Federhalter, dieses Stück Holz täglich in die Hand zu nehmen. Ich glaube schon, daß ich sie nicht habe. ', 'Wieviel Tage sind wieder stumm vorüber; heute ist der 28. Mai. Habe ich nicht einmal die Entschlossenheit, diesen Federhalter, dieses Stück Holz täglich in die Hand zu nehmen. Ich glaube schon, daß ich sie nicht habe. ', '28. Mai 1910', 'Wieviel Tage sind wieder stumm vorüber; heute ist der 28. Mai. Habe ich nicht einmal die Entschlossenheit, diesen Federhalter, dieses Stück Holz täglich in die Hand zu nehmen. Ich glaube schon, daß ich sie nicht habe. ']  # adding a row
final.index = final.index + 1  # shifting index
final = final.sort_index()  # sorting by index
#%%
final.drop(columns=["Text","Text_short"],inplace=True,axis=1)

#%%
final.dropna(subset = ["Datum"], inplace=True)
#%%
# now we need a column which we can use to compare to todays date
from datetime import datetime
import dateparser

#string = '1. Juli 2010'
#dateFormatter = '%d. %B %Y'
new_date=[]
for date in final['Datum']:
    print(date)
    converted = dateparser.parse(str(date)).strftime('%m-%d')
    new_date.append(converted)
    
final["date"] = new_date

#%%
final.drop(columns=["Datum","tweet","dairy_date"],inplace=True,axis=1)

#%%
final.head()

#%%
final.info()
# %%
final.to_json('/Users/hannahbohle/Documents/twitterbot/data/tweetlength_short.json') 

# %%
