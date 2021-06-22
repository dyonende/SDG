"""
Sentiment analysis on text

Arg1:   csv with text in 'text' column
Arg2:   output csv with added column for sentiment
"""
import requests
import sys
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

df = pd.read_csv(sys.argv[1])

texts = df['text'].values
sentiments = []

for text in texts:
    scores = sia.polarity_scores(text)
    sentiment = scores['compound']  #only use compound score
    
    sentiments.append(sentiment)
           
df['sentiment'] = sentiments

df.to_csv(sys.argv[2], index=False)
