import csv
import os
from datetime import datetime
import csv
from track_movements import Tracker

def DataProcessor(dataorign, foldername):
    #firstly store all the data in a dictionary with the ticker as key and {dict[timestamp] = title} as value
    companies = {}
    folder = os.path.join(os.getcwd(), dataorign + '\\')
    for i in os.scandir(folder):
        time = {}
        path = folder + i.name
        with open(path, 'r') as csvfile:
            data = list(csv.reader(csvfile))
            data = data[1:]
            for j in data:
                try:
                    key = datetime.strptime(j[1], '%b-%d-%y %H:%M%p')
                    time[str(key)] = j[2]
                    # store the date for the empty date row
                    date = key.strftime('%Y-%m-%d ')
                except:
                    key = datetime.strptime(j[1], '%H:%M%p').time()
                    key = date + str(key)
                    time[str(key)] = j[2]
        companies[i.name] = time


    # this is for checking wether the folder is existed or not
    # if not, simply create the folders and files within. 
    if os.path.exists(os.path.join(os.getcwd(), foldername)) != True:
        os.mkdir(foldername)
        for i,j in companies.items():
            with open(foldername +'\\' + i, 'w', newline='') as cp:
                a = csv.writer(cp, delimiter=',')
                data = [['Company', 'timestamp', 'label', 'headline']]
                i = i[:-4]
                for k,l in j.items():
                    new_tracker = Tracker(datetime.strptime(k, '%Y-%m-%d %H:%M:%S'), i)
                    new_tracker = new_tracker.get_price_change()
                    tem = [i,k,new_tracker,l]
                    data.append(tem)
                a.writerows(data)
    # if folder already existed, then just append the data into the respective existing files 
    else:
        # check if the ticker's csv files already existed before append
            for i, j in companies.items():
                if os.path.isfile(os.path.join(os.getcwd(), foldername +'\\' + i)):
                    with open(foldername +'\\' + i, 'a', newline='') as cp:
                        a = csv.writer(cp)
                        data = []
                        i = i[:-4]
                        for k,l in j.items():
                            new_tracker = Tracker(datetime.strptime(k, '%Y-%m-%d %H:%M:%S'), i)
                            new_tracker = new_tracker.get_price_change()
                            tem = [i,k,new_tracker,l]
                            data.append(tem)
                        a.writerows(data)
        # if it is new ticker, then create a new csv file for it
                else:
                    with open(foldername +'\\' + i, 'w+', newline='') as cp:
                        a = csv.writer(cp, delimiter=',')
                        data = [['Company', 'timestamp', 'label', 'headline']]
                        i = i[:-4]
                        for k,l in j.items():
                            new_tracker = Tracker(datetime.strptime(k, '%Y-%m-%d %H:%M:%S'), i)
                            new_tracker = new_tracker.get_price_change()
                            tem = [i,k,new_tracker,l]
                            data.append(tem)                       
                        a.writerows(data)

if __name__ == "__main__":
    #simple put all the data folders into dataorign argument and it would create or find respective csv file and append data in it.
    DataProcessor(dataorign = 'data1', foldername = 'data')
    DataProcessor(dataorign = '2020-10-10 10_44_54.930955', foldername = 'data')
    DataProcessor(dataorign = '2020-09-29 11_39_24.557866', foldername = 'data')
    DataProcessor(dataorign = '2020-08-28 11_08_11.175489', foldername = 'data')
