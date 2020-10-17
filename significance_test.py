import csv
from collections import Counter
import pandas as pd
import numpy as np
import json

with open('tickers.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    wordDict = dict()
    for row in spamreader:
        ticker = ', '.join(row)
        print(ticker)

        df = pd.read_csv('labelled_data/' + ticker + '.csv')
        labels = df['Label']
        headlines = df['Headline']
        print(headlines)
        for count,headline in enumerate(headlines):
            score = labels[count]
            for word in headline.split(' '):
                print(word)
                if word not in wordDict:
                    wordDict[word] = 0
                wordDict[word] += score
    sorted_dict = {k: v for k, v in sorted(wordDict.items(), key=lambda item: item[1])}

    dictlist = []
    for key, value in sorted_dict.items():
        temp = (key,value)
        print(temp)
        dictlist.append(temp)
    
    with open('ordered_list.csv','wb') as out:
        csv_out=csv.writer(out)
        for row in dictlist:
            print(row)
            #csv_out.writerow(row)
    
    maximum = max(wordDict, key=wordDict.get)
    mymax = wordDict[maximum]

    minimum = min(wordDict, key=wordDict.get)
    mymin = wordDict[minimum]

    #print(mymin)
    #print(mymax)
    for k in wordDict:
        wordDict[k] = (float(wordDict[k])-mymin)/(mymax-mymin)
    sorted_dict = {k: v for k, v in sorted(wordDict.items(), key=lambda item: item[1])}
    print(sorted_dict)



    json = json.dumps(sorted_dict)
    f = open("sorted_dict.json","w")
    f.write(json)
    f.close()
    