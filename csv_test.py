# Importing the required libraries
import csv
from operator import length_hint
import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers

#Import OS for reading in files
import os

#Import CSV File
rows = []
def importCSV(filename):
    print("Importing CSV")
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        #print(header)
        for row in csvreader:
            rows.append(row)
            #print(row)

#Convert .tab file to .csv file
def tabtoCSV(filename):
    with open(filename, 'rb') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        size = len(filename)
        new_filename = filename[:size - 3]
        print(new_filename)
        with open(new_filename + '.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('wavelength', 'reflectance', 'epsilon'))
            writer.writerows(lines)


#Read in every .tab file in Data Folder
datafiles = os.listdir('data')
for file in datafiles:
    #Now we have each file we can do things to it
    tabtoCSV(file)

#Import CSV File
#importCSV('test.csv')

#Define Wavelength, Reflectance and Uncertainty Variables
#wavelength = rows[0]
#reflectance = rows[1]
#uncertainty = rows[2]

#Import data into a dataframe
#asteroid_train = pd.read_csv('test.csv')
#asteroid_train.head()
#(train_data, train_labels), (test_data, test_labels) = 
