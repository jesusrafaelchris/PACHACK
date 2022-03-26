import csv
import pandas as pd
import keras
import numpy

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
wavelength = rows[0]
reflectance = rows[1]
uncertainty = rows[2]
