import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import datetime
import os 

failed = []
with open('tickers.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    title = str(datetime.datetime.now())
    os.mkdir(title)
    for row in spamreader:
        # Get ticker string from file
        ticker = str(row[0])
        print("Currently scraping for: " + ticker)

        try:
            # Form url string and request it
            url='https://finviz.com/quote.ashx?t=' + ticker
            res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
            print("Response" + str(res))
            soup = BeautifulSoup(res.text,'html.parser')
            table = soup.find("table",{"class":"fullview-news-outer"})
            tableDataframe = pd.read_html(str(table))
            tableDataframe =  tableDataframe[0]
            tableDataframe.to_csv('./' + title + '/' + ticker + ".csv")
        except:
            print(ticker + " failed, bad response")
            failed.append(ticker)

if not failed:
    print("No failures")
else:
    print("Failures: \n")
    for xx in failed:

        print(str(xx) + "\n")
