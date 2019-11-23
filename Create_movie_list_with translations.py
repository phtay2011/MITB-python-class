# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:40:14 2019

@author: User
"""

from googletrans import Translator
import googletrans 
translator = Translator()
googletrans.LANGCODES
text = '안녕하세요.'
src = 
dest = en
translator.translate('안녕하세요.',src = , dest =).text

full_list = []
lang = ['de', 'en', 'es', 'pt', 'it', 'ja', 'ht', 'cy', 'th', 'in', 'und',
       'ro', 'lv', 'tr', 'da', 'fr', 'hu', 'fi', 'sv', 'et', 'nl', 'eu',
       'no', 'tl', 'pl', 'ko', 'ca', 'zh', 'vi', 'ta', 'ar', 'hi', 'ru',
       'is', 'te', 'bg', 'el', 'lt', 'sl', 'fa', 'sr', 'cs']
movie_data =['Joker','Shoplifters','Toy Story 4','Avengers: Endgame','Doctor Sleep','Zombieland: Double Tap','Official Secret','Once Upon a Time in Hollywood','Spider-Man: Far From Home','Rocketman','Avengers','Doctor','Zombieland','Endgame','Sleep','Double Tap','Spider-Man','Far From Home']

for i in movie_data:
    for j in lang:
        try:
            translated_lang = translator.translate(i,dest =j).text
        except:
            translated_lang = i
        full_list.append(translated_lang )
        
full_list = list( set(full_list ))
print (full_list)