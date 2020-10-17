import nltk 
nltk.download('vader_lexicon')
from textblob import TextBlob
import csv
import pandas as pd
from nltk import NaiveBayesClassifier
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
import numpy as np
import json

with open("sorted_dict.json", "r") as read_file:
    lexicon = json.load(read_file)


sentiment_df = pd.DataFrame()
sid = SentimentIntensityAnalyzer()
textblob_sent = []
labels = []
with open('tickers.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    wordDict = dict()
    for row in spamreader:
        ticker = row[0]
        with open('labelled_data/' + ticker + '.csv', newline='') as tickerfile:
            headlinereader = csv.reader(tickerfile, delimiter=' ', quotechar='|')
            for entry in headlinereader:
                data = ', '.join(entry)
                try:
                    score = int(data.split(',')[3])
                except:
                    score = 0
                labels.append(score)

                headline = ', '.join(entry[2:])
                testimonial = TextBlob(headline)
                headline_score = 0
                for word in headline.split(' '):
                    print(word)
                    headline_score += lexicon.get(word)
                nltk_sent = list(sid.polarity_scores(headline).values())
                textblob_sent.append([nltk_sent[0], nltk_sent[1], nltk_sent[2], nltk_sent[3]])


sentiment_df['Labels'] = labels
sentiment_df['Textblob'] = textblob_sent

from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(textblob_sent, labels, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=500,max_depth=50, random_state=0,class_weight='balanced')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(accuracy_score(y_pred,y_test))

