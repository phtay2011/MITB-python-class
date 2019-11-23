# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:31:19 2019

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
#Data import
df = pd.read_csv('movies_list_v2.csv')
df.shape
df.columns
#Data Cleaning
print(df.isna().sum())

df.iloc[:,0]

#Detect Non-numbers
cnt=0
for row in df['id']:
    try:
        int(row)
    except ValueError:
        #test.loc[cnt, '# of followers']=np.nan
        print(cnt)
    cnt+=1
#Find the device info

device_list = ['Android', 'iPhone', 'iPad', 'Mac', 'iΟS', 'iOS  ',
       'Android #5', 'Android #8', 'iOS',
       'Android #7','Windows Phone']               

df['Device_info'] = df['source'].apply(lambda x: re.split('<|>|for ',x)[3] )
df['Device_info'] = df['Device_info'].apply(lambda x: x if x in device_list else np.nan)
df['Device_info'] = df['Device_info'].replace(['Android #7','Android #5','Android #8'],'Android')
df['Device_info'] = df['Device_info'].replace(['iPhone','iPad','Mac','iOS  ','iOS'],'iΟS')
  
#list of unique values
df['Device_info'].unique()
print(df['Device_info'].isna().sum())

#language
df['lang'].unique()
tweets_by_lang = df['lang'].value_counts()

#Country data clearning
df['country'].unique()
country_list = [nan, 'United States', 'South Africa', 'Kenya', 'Chile', 'Mexico',
       'Nigeria', 'India', 'México', 'United Kingdom', 'Singapore',
       'Belgium', 'Indonesia', 'Canada', 'Antigua and Barbuda',
       'Malaysia', 'Sweden', 'Republic of the Philippines', 'Brazil',
       'Argentina', 'Hashemite Kingdom of Jordan', 'Brasil', 'Malawi',
       'France', 'Costa Rica', 'Botswana', 'United Arab Emirates', 'Peru',
       'Portugal', 'Kingdom of Saudi Arabia', 'Zimbabwe', 'Colombia',
       'Italy', 'Bangladesh', 'Jamaica', 'Saint Lucia', 'Australia',
       'Germany', 'Hong Kong', 'Cyprus', 'Nederland', '日本',
       'Estados Unidos', 'Bahamas', 'Trinidad and Tobago', 'Deutschland',
       'New Zealand', 'Zambia', 'Ísland', 'Algeria', 'Reino Unido',
       'Belize', "People's Republic of China", 'Ghana', 'Tanzania',
       'Paraguay', 'Republic of Korea', 'Kuwait', 'Russia', 'Bahrain',
       'El Salvador', 'Egypt', 'Panamá', 'Uganda', 'España', 'Pakistan',
       'Italia', 'Fiji', 'Denmark', 'Switzerland', 'Albania',
       'Dominican Republic', 'Ireland', 'Republic of Croatia', 'Qatar',
       'Namibia', 'Polska', 'Dominica']

#Create new csv file
columns_to_use = ['id', 'text','lang','country', 'user_location', 'Device_info']
df_2 = pd.DataFrame()
for i in columns_to_use:
    df_2[columns_to_use] = df[columns_to_use] 
    
export_csv = df_2.to_csv (r'actors_list_v2.csv', index = None, header=True) 


