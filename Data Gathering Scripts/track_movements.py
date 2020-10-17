import pandas_datareader as reader
import datetime
from datetime import timedelta
import os
import csv

class Tracker:
    def __init__(self, timestamp, ticker):
        self.timestamp = timestamp
        self.ticker = ticker
        print(timestamp)
        self.data = reader.get_data_yahoo(ticker, timestamp, timestamp + timedelta(days=3))

    def get_price_change(self):
        change = round(((self.data['Adj Close'][-1]-self.data['Adj Close'][0])/self.data['Adj Close'][0]*100),2)
        print(change)
        return_value = 0
        if change > 2:
            return_value = 1
        elif change < -2:
            return_value = -1
        return return_value

def Test(filename):
    time = {}
    f = os.path.join(os.getcwd(), 'data1\\' + filename)
    with open(f, 'r') as cp:
                    data1 = list(csv.reader(cp))
                    data1 = data1[1:]
                    for j in data1:
                        try:
                            key = datetime.datetime.strptime(j[1], '%b-%d-%y %I:%M%p')
                            time[str(key)] = j[2]
                            # store the date for the empty date row
                            date = key.strftime('%Y-%m-%d ')
                        except:
                            key = datetime.datetime.strptime(j[1], '%I:%M%p').time()
                            key = date + str(key)
                            time[str(key)] = j[2]
    with open(filename, 'w+', newline='') as cb:
        a = csv.writer(cb, delimiter=',')
        data = [['Company', 'timestamp', 'label', 'headline']]
        for k,l in time.items():
            new_tracker = Tracker(datetime.datetime.strptime(k, '%Y-%m-%d %H:%M:%S'), filename)
            new_tracker = new_tracker.get_price_change()
            tem = [filename,k,new_tracker,l]
            data.append(tem)
        a.writerows(data)


## Example Usage
# Define your datetime object
#datetime_object = datetime.datetime.strptime('2020-06-17 06:18:00', '%Y-%m-%d %H:%M:%S')
# Get the object
#new_tracker = Tracker(datetime_object, 'DIS')
# Call the get_price_change function on it
#print(new_tracker.get_price_change())