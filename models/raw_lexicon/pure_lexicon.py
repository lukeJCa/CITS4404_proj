import csv
import pandas as pd
import numpy as np
import json
import pickle

from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


## The pre-made list of all our words and associated (and scaled) values
with open("sorted_dict.json", "r") as read_file:
    lexicon = json.load(read_file)

scores = []
labels = []
# Iterate through ticker list to get all of our dataframes
with open('../../datafiles/tickers.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        ticker = row[0]
        df = pd.read_csv('../../labelled_data/' + ticker + '.csv')
        #print(df)
        for count,headline in enumerate(df['Headline']):
            headline = df['Headline'][count]
            headline_score = 0
            for word in headline.split(' '):
                headline_score += lexicon.get(word)
            scores.append([headline_score])
            labels.append(df['Label'][count])

# Train, test and save our model, using SGD Classifier to converge to some sensible solution
X_train, X_test, y_train, y_test = train_test_split(np.array(scores), labels, test_size=0.2, random_state=42)
clf = SGDClassifier(class_weight='balanced',fit_intercept=False,max_iter=100)
clf.fit(X_train, y_train)

pickle.dump(clf, open("sgdmodel.h5", 'wb'))

y_pred = clf.predict(X_test)
print(accuracy_score(y_pred,y_test))
print(f1_score(y_pred,y_test, average = 'weighted'))
print(precision_score(y_pred,y_test, average = 'weighted'))
print(recall_score(y_pred,y_test, average = 'weighted',zero_division=1))

cf_matrix = confusion_matrix(y_test, y_pred)
ax = sn.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, fmt='.2%', cmap='Blues',xticklabels = [-1,0,1], yticklabels = [-1,0,1])
plt.savefig("SGD_heatmap.png")