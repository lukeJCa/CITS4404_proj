import json
import pandas as pd
import numpy as np
import csv
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
sid = SentimentIntensityAnalyzer()


with open("sorted_dict.json", "r") as read_file:
    lexicon = json.load(read_file)

print(lexicon)
scores = []
labels = []

with open('tickers.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    wordDict = dict()
    for row in spamreader:
        ticker = ', '.join(row)
        print(ticker)

        df = pd.read_csv('labelled_data/' + ticker + '.csv')
        ticker_labels = pd.Series(df['Label'])
        headlines = df['Headline']
        print(headlines)
        for count,headline in enumerate(headlines):
            headline_score = 0
            for word in headline.split(' '):
                headline_score += lexicon.get(word)
            testimonial = TextBlob(headline).sentiment[0]
            subjectivity = TextBlob(headline).sentiment[1]
            nltkbit = list(sid.polarity_scores(headline).values())
            #print(testimonial)
            scores.append([headline_score,testimonial,subjectivity,nltkbit[0],nltkbit[1],nltkbit[2],nltkbit[3]])
            labels.append(ticker_labels[count])

#print(scores)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(scores, labels, test_size=0.2, random_state=42)
reg = LogisticRegression(class_weight = 'balanced').fit(X_train, y_train)
y_pred = reg.predict(X_test)
print(accuracy_score(y_pred,y_test))

from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(scores, labels, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=0,class_weight='balanced')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(accuracy_score(y_pred,y_test))


