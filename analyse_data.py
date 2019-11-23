# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:28:09 2019

@author: User
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
#Next we will read the data in into an array that we call tweets.
tweets_data_path = 'movies_list_v2.csv'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
# See tweet data
#We can print the number of tweets using the command below
print (len(tweets_data))

#Create a Dataframe
tweets = pd.DataFrame()
tweets  = pd.read_csv(tweets_data_path)

#Func to extract info from dic
def extract_dic_key (string):
    lst=[]
    for i in range(len(tweets_data)):
        lst.append(tweets_data[i][string])
    return lst

# Find all the dict_keys
list_of_keys = list(tweets_data[0].keys())
list_of_relevant_fields = ['created_at','id','id_str','text','source', 'truncated', 'in_reply_to_status_id', 'in_reply_to_status_id_str',
 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user', 'geo', 'coordinates',
 'place', 'contributors', 'reply_count', 'retweet_count', 'favorite_count',
 'entities', 'favorited', 'retweeted', 'filter_level', 'lang', 'timestamp_ms']
#prepare tweets DF
for i in list_of_relevant_fields:
    tweets[i]=extract_dic_key(i)

#Add a country col
country_col = []
for i in range(len(tweets_data)):
    if tweets_data[i]['place'] != None:
        country_col.append(tweets_data[i]['place']['country'])
    else:
        country_col.append(np.nan)
tweets['country']=country_col

#Add user info
user_col = []
for i in range(len(tweets_data)):
    if tweets_data[i]['user'] != None:
        user_col.append(tweets_data[i]['user']['location'])
    else:
        user_col.append(np.nan)
tweets['user_location']=user_col


#Convert df to csv
tweets.to_csv (r'movies_list.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

#Create charts
tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

tweets_by_country = tweets['user_location'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('location', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:8].plot(ax=ax, kind='bar', color='blue')

"""
Mining the data
"""
#Function to for text. True if text is foud
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
movie_data =['Joker','Shoplifters','Toy Story 4','Avengers: Endgame','Doctor Sleep','Zombieland: Double Tap','Official Secret','Once Upon a Time in Hollywood','Spider-Man: Far From Home','Rocketman','Avengers','Doctor','Zombieland','Endgame','Sleep','Double Tap','Spider-Man','Far From Home']#To find word in text
for i in movie_data:
    tweets[i] = tweets['text'].apply(lambda tweet: word_in_text(i, tweet))
tweets.columns
#Calculate number of tweets
lst={}
for i in movie_data:
    try:
        lst[i] = tweets[i].value_counts()[True]
    except:
        lst[i] = 0
    


#Plot Graph
prg_langs = movie_list
tweets_by_prg_lang = [ tweets[i].value_counts()[True] for i in prg_langs ]
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs. javascript vs. ruby (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()

"""
Target relevant tweets
"""
tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))
tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))

#Count number of tweets
print (tweets['programming'].value_counts()[True])
print (tweets['tutorial'].value_counts()[True])
print (tweets['relevant'].value_counts()[True])

#Compare popularity of languages
print (tweets[tweets['relevant'] == True]['python'].value_counts()[True])
print (tweets[tweets['relevant'] == True]['javascript'].value_counts()[True])
print (tweets[tweets['relevant'] == True]['ruby'].value_counts()[True])

#Plot graph
tweets_by_prg_lang = [tweets[tweets['relevant'] == True]['python'].value_counts()[True],
                      tweets[tweets['relevant'] == True]['javascript'].value_counts()[True],
                      tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]]
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs. javascript vs. ruby (Relevant data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()

"""
Extracting links from the relevants tweets
"""
# retrieve links to programming tutorials
def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

#Create new Dataframe containing relevant tweets
tweets_relevant = tweets[tweets['relevant'] == True]
tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

print (tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link'])
print (tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link'])
print (tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link'])
