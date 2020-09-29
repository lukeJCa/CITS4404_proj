import csv
import os
from datetime import datetime


def formatTime(fname):
    time = {}
    path = './2020-08-26 10_08_25.249321/' + str(fname)
    with open(path , 'r') as csvfile:
        data = list(csv.reader(csvfile))
        data = data[1:]
        for i in data:
            try:
                key = datetime.strptime(i[1], '%b-%d-%y %H:%M%p')
                time[str(key)] = i[2]
            except:
                key = datetime.strptime(i[1], '%H:%M%p').time()
                time[str(key)] = i[2]
    return (time)

# if __name__ == '__main__':
#     a = formatTime('ABT.csv')
#     for i,j in a.items():
#         print(i + '  ' + j)
