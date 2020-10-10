import pandas_datareader as reader
import datetime
from datetime import timedelta

class Tracker:
    def __init__(self, timestamp, ticker):
        self.timestamp = timestamp
        self.ticker = ticker
        print(timestamp)
        self.data = reader.get_data_yahoo(ticker, timestamp, timestamp + timedelta(days=3))

    def get_price_change(self):
        return round(((self.data['Adj Close'][-1]-self.data['Adj Close'][0])/self.data['Adj Close'][0]*100),2)
    

## Example Usage
# Define your datetime object
#datetime_object = datetime.datetime.strptime('2020-06-17 06:18:00', '%Y-%m-%d %H:%M:%S')
# Get the object
#new_tracker = Tracker(datetime_object, 'ABT')
# Call the get_price_change function on it
#print(new_tracker.get_price_change())