# Importing the required libraries
import csv
import pandas as pd

rows = []
#tab_file = "example.tab"
#csv_file = "tab_to_csv.csv"

#dataframe = pd.read_csv(tab_file,delimiter="\t")
#dataframe.to_csv(csv_file, encoding='utf-8', index=False)

def importCSV(csvfile):
    print("Importing CSV")
    with open(csvfile, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)
        for row in csvreader:
            rows.append(row)
            print(row)

importCSV('test.csv')
