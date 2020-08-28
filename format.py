import csv
import os
from datetime import datetime


def formatTime(fname):
    time = []
    path = './2020-08-26 10_08_25.249321/' + str(fname)
    with open(path , 'r') as csvfile:
        data = list(csv.reader(csvfile))
        data = data[1:]
        for i in data:
            try:
                time.append(datetime.strptime(i[1], '%b-%d-%y %H:%M%p'))
            except:
                time.append(datetime.strptime(i[1], '%H:%M%p').time())
    return (time)

# if __name__ == '__main__':
#     a = formatTime('ABT.csv')
#     print(a)