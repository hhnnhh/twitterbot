

# Scrape Text for Diary 

#%%
import requests
from bs4 import BeautifulSoup
import datefinder
import pandas as pd
from nltk.tokenize import sent_tokenize

import tweepy

#%%
# build URLS for gutenberg webscraping
# Tagebücher have 14 Chapters on 14 URL
urls=['https://www.projekt-gutenberg.org/kafka/tagebuch/tagebuch.html']
for x in range(1,15):
    urls.append('https://www.projekt-gutenberg.org/kafka/tagebuch/chap'+str("{:03d}".format(x))+'.html')
#print(urls)
#%%
#scrape combined urls

data = []

#scrape elements
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")#.decode('utf-8')

    print(soup)

    data.append({
        #'title': soup.title,
        #'chapter': soup.h2.get_text(),
        #'text': ' '.join([p.get_text(strip=True) for p in soup.select('body p')[2:]]),
        ' '.join([p.get_text(strip=True) for p in soup.select('body p')[2:]])
        }
    )

data

#%%
import pandas as pd
df = pd.DataFrame(data) 
    
# saving the dataframe 
df.to_csv('kafka.txt') 
#%%
#make a string out of the txt to enable searching for dates with datefinder
mystr = ''.join(map(str, data)).replace('{','').replace('}','')
#%%
print(mystr)


# %%
# using regex to find all the dates in the format "15. Februar blabla ."
x = df['Kafka'].str.split('(\d{1,2}\.?\s*(?:Jan|Feb|März|April|Mai|Juni|Juli|August|Sept|Okt|Nov|Dez)\w*(?:\s*\d{4}|\d{2})?)',expand=True)

# %%
# regex : \d{1,2}\.?\s*(?:Jan|Feb|März|April|Mai|Juni|Juli|August|Sept|Okt|Nov|Dez)[^.]*

#%%
# I have a strange df now: every second columns is either a date or the text
x.head()
#%%
# first column doesnt have a date, i.e. cannot be used
x = x.drop(columns=0)
#%%
# I extract the text from every second column, starting with the second
df2 = pd.melt(x,value_vars=x[x.columns[1::2]])
# %%
df2.head()
# %%
# extracting date from every second column, starting with first
df3= pd.melt(x,value_vars=x[x.columns[0::2]])
# %%
df3.head()
# %%
# renaming columns so they dont get confused
df2.rename(columns={"value": "Text"},inplace=True)
df3.rename(columns={"value": "Datum"},inplace=True)
# %%
# final df is merged by index
final = pd.merge(df3, df2, left_index=True, right_index=True).drop(columns=["variable_x","variable_y"])

# %%

# %%
final['Text_short'] = final['Text'].str[1:280] # probeweise Textkürzung, um zu sehen, wie in etwa die Länge sein sollte

final.head()
# %%
final.to_csv('kafka_parsed.txt') 

#####
# weitermachen mit dem geparsten Text: Datum, Text, Text_short
#%%
final = pd.read_csv('data/kafka_parsed.txt')

#%%
final.drop(columns=final.columns[0], 
        axis=1, 
        inplace=True)

#%%
short = final.head(1)
# %%
#df = final['Text'].str.split('.',expand=True)
#%%
pd.set_option('display.max_colwidth', None)

df

#%%
short
#%%
#
for txt in short['Text']:
    token_text = sent_tokenize(txt,language='german')
    print(token_text)
    print(len(token_text))
    while len(token_text) < 280:
        token_text += token_text + token_text
        print("ende",token_text)
        #final['number'] = final.apply(lambda row: len(token_text), axis=1)
        #final['shortened'] = final.apply(lambda row: token_text, axis=1)

# %%
pd.set_option('display.max_colwidth', None)
final.head(1)
#%%
d = ".!?"
for txt in final['Text']:
    s =  [e+d for e in txt.split(d) if e]
    while len(s) < 280:
        print(s)
        s += s + s
final['new'].values = s

#%%
d = ".!?"
for idx, row in final.iterrows():
    for x in final['Text']:
        [x[i] for i in range(len(x)) if [sum(list(map(len,x))[:j+1]) for j in range(len(x))][i] < 280]
        print(x)
#final.loc[idx,'new_text'] = s
print(s)


# %%
# Iterate through the dataframes, first through the country dataframe and inside through the sentence one.
for index, row in final.iterrows():
    text = Text.row
    print(text)


