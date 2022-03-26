import csv

# File names: to read in from and read out to
input_file = "test.tab"
output_file = "tester.txt"

## ==================== ##
##  Using module 'csv'  ##
## ==================== ##

lines = []

with open(input_file) as to_read:
    for line in to_read:
        line = line.split()
        lines.append(line)

lines = lines[:len(lines)-10]
lines = lines[1:]


with open('tester.csv', 'a', newline='') as f_object:  
    writer_object = csv.writer(f_object)
    for line in lines:
        writer_object.writerow(line)  
    f_object.close()