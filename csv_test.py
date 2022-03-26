# Importing the required libraries
import csv
import pandas as pd

rows = []

def importCSV(filename):
    print("Importing CSV")
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)
        for row in csvreader:
            rows.append(row)
            print(row)

importCSV('test.csv')
