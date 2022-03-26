import csv
rows = []

def importCSV(csvfile):
    print("Importing CSV")
    with open(csvfile, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
    for row in csvreader:
        rows.append(row)

