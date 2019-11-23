# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:00:12 2019

@author: User
http://adilmoujahid.com/posts/2014/07/twitter-analytics/
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
'''
 access_token = "CREDENTIALS_IN_TEXT_FILE"
 access_token_secret = "CREDENTIALS_IN_TEXT_FILE"
 consumer_key = "CREDENTIALS_IN_TEXT_FILE"
 consumer_secret = "CREDENTIALS_IN_TEXT_FILE"
'''
access_token = "1124327501654716423-s6XhLjClYajimqfvi8XDZZRpg7G7vv"
access_token_secret = "ay6ukhBnSla9uZJ5vwlp79jFj7aT33ylFpkQe4HSbPRM5"
consumer_key = "VEnaIbeztVZYyP8dm0SNyHsZ6"
consumer_secret = "5Kj8qunQ4mtbl6Q107gtkUuhYKFbrfupzz2ZCf66pLwaHWcZKs"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    movie_data =['Joker','Shoplifters','Toy Story 4','Avengers: Endgame','Doctor Sleep','Zombieland: Double Tap','Official Secret','Once Upon a Time in Hollywood','Spider-Man: Far From Home','Rocketman','Avengers','Doctor','Zombieland','Endgame','Sleep','Double Tap','Spider-Man','Far From Home']

    #Full list
    # movie_data =['Joker','Shoplifters','Toy Story 4','Avengers: Endgame','Doctor Sleep','Zombieland: Double Tap','Official Secret','Once Upon a Time in Hollywood','Spider-Man: Far From Home','Rocketman','Avengers','Doctor','Zombieland','Endgame','Sleep','Double Tap','Spider-Man','Far From Home',
    # 'Joaquin Phoenix','Zazie Beetz','Robert De Niro','Bryan Callen','Shea Whigham','Lily Franky','Sakura Ando','Mayu Matsuoka','Kirin Kiki','Jyo Kairi','Tom Hanks','Patricia Arquette','Tim Allen','Joan Cusack','Bonnie Hunt','Robert Downey Jr.','Chris Evans','Mark Ruffalo','Chris Hemsworth','Scarlett Johansson','Rebecca Ferguson','Ewan McGregor','Jacob Tremblay','Cliff Curtis','Carel Struycken','emma stone','Abigail Breslin','Woody Harrelson','Jesse Eisenberg','Zoey Deutch','Matthew Goode','Indira Varma','Keira Knightley','Katherine Kelly','Ralph Fiennes','Leonardo DiCaprio','Luke Perry','Margot Robbie','Brad Pitt','Margaret Qualley','Samuel L. Jackson','Zendaya','Tom Holland','Jake Gyllenhaal','Michael Keaton','Bryce Dallas Howard','Richard Madden','Taron Egerton','Jamie Bell','Steven Mackintosh'
    # ]
    stream.filter(track=movie_data)

# to run the script python twitter_streaming.py > twitter_data.txt
