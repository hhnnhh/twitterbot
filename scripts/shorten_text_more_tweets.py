

#%%
import requests
from bs4 import BeautifulSoup
import datefinder
import pandas as pd
from nltk.tokenize import sent_tokenize

import tweepy

#%%
text = "über Hauptmanns ›Die Jungfern vom Bischofsberg‹. Endlich nach fünf Monaten meines Lebens, in denen ich nichts schreiben konnte, womit ich zufrieden gewesen wäre, und die mir keine Macht ersetzen wird, obwohl alle dazu verpflichtet wären, komme ich auf den Einfall, wieder einmal mich anzusprechen. Darauf antwortete ich noch immer, wenn ich mich wirklich fragte, hier war immer noch etwas aus mir herauszuschlagen, aus diesem Strohhaufen, der ich seit fünf Monaten bin und dessen Schicksal es zu sein scheint, im Sommer angezündet zu werden und zu verbrennen, rascher, als der Zuschauer mit den Augen blinzelt. Wollte das doch nur mit mir geschehn! Und zehnfach sollte mir das geschehn, denn ich bereue nicht einmal die unglückselige Zeit. Mein Zustand ist nicht Unglück, aber er ist auch nicht Glück, nicht Gleichgültigkeit, nicht Schwäche, nicht Ermüdung, nicht anderes Interesse, also was ist er denn? Daß ich das nicht weiß, hängt wohl mit meiner Unfähigkeit zu schreiben zusammen. Und diese glaube ich zu verstehn, ohne ihren Grund zu kennen. Alle Dinge nämlich, die mir einfallen, fallen mir nicht von der Wurzel aus ein, sondern erst irgendwo gegen ihre Mitte. Versuche sie dann jemand zu halten, versuche jemand ein Gras und sich an ihm zu halten, das erst in der Mitte des Stengels zu wachsen anfängt. Das können wohl einzelne, zum Beispiel japanische Gaukler, die auf einer Leiter klettern, die nicht auf dem Boden aufliegt, sondern auf den emporgehaltenen Sohlen eines halb Liegenden, und die nicht an der Wand lehnt, sondern nur in die Luft hinaufgeht. Ich kann es nicht, abgesehen davon, daß meiner Leiter nicht einmal jene Sohlen zur Verfügung stehn. Es ist das natürlich nicht alles, und eine solche Anfrage bringt mich noch nicht zum Reden. Aber jeden Tag soll zumindest eine Zeile gegen mich gerichtet werden, wie man die Fernrohre jetzt gegen den Kometen richtet. Und wenn ich dann einmal vor jenem Satze erscheinen würde, hergelockt von jenem Satze, so wie ich zum Beispiel letzte Weihnachten gewesen bin und wo ich so weit war, daß ich mich nur noch gerade fassen konnte, und wo ich wirklich auf der letzten Stufe meiner Leiter schien, die aber ruhig auf dem Boden stand und an der Wand. Aber was für ein Boden, was für eine Wand!Und"
#%%
def join_tweet_or_less(lst, limit=840):
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
        if len(' '.join(new_join)) > 280:
            return lst[:i+1]
        elif len(' '.join(new_join)) > 280 and len(' '.join(new_join)) < 560:
            return lst[:i]
        elif len(' '.join(new_join)) > 560:
            return lst[:i]
    return lst


#%%
join_tweet_or_less(text)
#%%
final = pd.read_csv('/Users/hannahbohle/Documents/twitterbot/data/kafka_parsed.txt')

#%%
final.drop(columns=final.columns[0], 
        axis=1, 
        inplace=True)

#%%
short = final.reset_index().head(10)
# %%
# hier muss ich überlegen, ob ich lange Texte über mehrere Tage tweete oder 
# mehrere Tweets an einem Tag? Das können aber sehr viele werden. Vielleicht mehrere Tweets, aber maximal z.B. 3?
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
#%%
final.drop()
# %%
final.to_csv('/data/tweetlength_parsed.txt') 

# %%
