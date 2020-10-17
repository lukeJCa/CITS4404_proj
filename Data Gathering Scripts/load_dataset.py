import csv
import pandas as pd

def combine_dataframe():

    full_dataset = pd.DataFrame()
    with open('tickers.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            ticker = ', '.join(row)
            df = pd.read_csv('labelled_data/' + ticker + '.csv')
            full_dataset = pd.concat([full_dataset,df])
    return full_dataset


# Usage, function uses the tickers file and the labelled_data folder to form 1 large dataset
if __name__ == "__main__":
    print(combine_dataframe())
# for george