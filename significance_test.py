import csv
from collections import Counter


with open('tickers.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    wordDict = dict()
    for row in spamreader:
        ticker = ', '.join(row)
        print(ticker)
        with open('labelled_data/' + ticker + '.csv', newline='') as tickerfile:
            headlinereader = csv.reader(tickerfile, delimiter=' ', quotechar='|')
            for entry in headlinereader:
                data = ', '.join(entry)
                try:
                    score = int(data.split(',')[3])
                except:
                    score = 0
                headline = entry[2:]
                
                for word in headline:
                    if word not in wordDict:
                        wordDict[word] = 0
                    wordDict[word] += score
    my_dict = {k: v for k, v in sorted(wordDict.items(), key=lambda item: item[1])}
    with open('sig_dict.csv', 'w') as f:
        for key in my_dict.keys():
            f.write("%s,%s\n"%(key,my_dict[key]))
    #print(wordDict)