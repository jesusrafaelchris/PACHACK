# Importing the required libraries
import csv
import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
from tensorflow.keras import layers

#Import OS for reading in files
import os

#Import CSV File Function Handler
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


#Read in every file in Data Folder
datafiles = os.listdir('data')
print(datafiles)

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
