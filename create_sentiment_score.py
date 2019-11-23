import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import nltk
from textblob import TextBlob
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from textblob import Word
#Data import
df = pd.read_csv('movies_list_v3_when_only_movies_show_up.csv')
df.shape
df.columns


#Remove Stop words
nltk.download('stopwords')
stop = stopwords.words('english')

df['stopwords'] = df['text'].apply(lambda x: len([w for w in x.split() if w in stop]))
df[['text','stopwords']].head()

#Number of special characters
df['hastags'] = df['text'].apply(lambda x: len([x for x in x.split() if x.startswith('#')]))
df[['text','hastags']].head()

#Move all to lower case
df['text'] = df['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df['text'].head()

#Remove Punctuation
df['text'] = df['text'].str.replace('[^\w\s]','')
df['text'] = df['text'].str.replace('rt\s\w+','')

# Create a Corpus using Tokenization and Stemming
corpus = []
max_value = len(df['text'])
for i in range (0,max_value):
    review = re.sub('[^a-zA-Z]',' ' , df['text'][i])    #Only include letters
    review = review.lower()         #Make all the letters small caps
    review = review.split()         #Split the words into seperate list
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = '  '.join(review)
    corpus.append(review)

corpus_df = pd.DataFrame(corpus, columns =['corpus'])
corpus_df.head()
# Lemmatization
nltk.download('wordnet')
df['corpus'] = corpus_df ['corpus'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
df['corpus'].iloc[0:15]
#Create the bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = df.iloc [:, 1].values

#Term Frequency
tf1 = (df['corpus']).apply(lambda x: pd.value_counts(x.split(" "))).sum().reset_index()
tf1.columns = ['words','tf']
tf1

#Sentiment Analysis
df['sentiment'] = df['corpus'].apply(lambda x: TextBlob(x).sentiment[0] )
df[['corpus','sentiment']].head()

export_csv = df.to_csv (r'movie_list_v4.csv', index = None, header=True) 

