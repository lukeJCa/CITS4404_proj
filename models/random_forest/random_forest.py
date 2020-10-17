import nltk 
nltk.download('vader_lexicon')

from textblob import TextBlob
import csv
import pandas as pd
import numpy as np
import json
import pickle

from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

with open("sorted_dict.json", "r") as read_file:
    lexicon = json.load(read_file)


sentiment_df = pd.DataFrame()
sid = SentimentIntensityAnalyzer()
scores = []
labels = []

# We need NLTK sentiment, textblob polarity/subjectivity AND lexicon values
with open('../../datafiles/tickers.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    wordDict = dict()
    for row in spamreader:
        ticker = ', '.join(row)

        df = pd.read_csv('../../labelled_data/' + ticker + '.csv')
        ticker_labels = pd.Series(df['Label'])
        headlines = df['Headline']
        for count,headline in enumerate(headlines):
            headline_score = 0
            for word in headline.split(' '):
                headline_score += lexicon.get(word)
            testimonial = TextBlob(headline).sentiment[0]
            subjectivity = TextBlob(headline).sentiment[1]
            nltkbit = list(sid.polarity_scores(headline).values())
            scores.append([headline_score,testimonial,subjectivity,nltkbit[0],nltkbit[1],nltkbit[2],nltkbit[3]])
            labels.append(ticker_labels[count])


# Using random forest on the input features,
X_train, X_test, y_train, y_test = train_test_split(scores, labels, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=1000,max_depth=100, random_state=0,class_weight='balanced')
clf.fit(X_train, y_train)

# Random forest size is prohibitively big so i wont save it, leaving this here just in case
#pickle.dump(clf, open("random_forest.h5", 'wb'))


y_pred = clf.predict(X_test)
print(accuracy_score(y_pred,y_test))

