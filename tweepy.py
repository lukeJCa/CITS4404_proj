import requests
from bs4 import BeautifulSoup
import pandas as pd

ticker = 'AMZN'
url='https://finviz.com/quote.ashx?t=' + ticker
res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
print(res)
soup = BeautifulSoup(res.text,'html.parser')

print("got here")

table = soup.find("table",{"class":"fullview-news-outer"})
tableDataframe = pd.read_html(str(table))
print(type(tableDataframe))
tableDataframe =  tableDataframe[0]
tableDataframe.to_csv('./data/' + ticker + ".csv")