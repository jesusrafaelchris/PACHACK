import csv
import os


#Convert .tab file to .csv file

'''def tabtoCSV(filename):
    with open(filename) as to_read:
        if file == ".DS_Store":
            print("file is DS Store")
        else:
            lines = []
            print("Converting " + filename + " to .csv")
            for line in to_read:
                line = line.split()
                lines.append(line)
            lines = lines[:len(lines)-10]
            lines = lines[1:]
            remove_start_filename = filename.replace('/Users/christiangrinling/Documents/GitHub/PACHACK/data/', '')
            size = len(remove_start_filename)
            new_filename = remove_start_filename[:size - 4]
            with open('/Users/christiangrinling/Documents/GitHub/PACHACK/data_csv/' + new_filename + '.csv', 'w') as out_file:  
                writer_object = csv.writer(out_file)
                for line in lines:
                    writer_object.writerow(line)



#Read in every .tab file in Data Folder
datafiles = os.listdir('/Users/christiangrinling/Documents/GitHub/PACHACK/data')
for file in datafiles:
    tabtoCSV('/Users/christiangrinling/Documents/GitHub/PACHACK/data/' + file)'''


#We need to limit the data between 435 and 925 nanocrons
datafiles = os.listdir('/Users/christiangrinling/Documents/GitHub/PACHACK/data_csv')
for file in datafiles:
    print("Converting " + file + " to set bounds")
    if file == ".DS_Store":
        print("file is DS Store")
    else:
        with open('/Users/christiangrinling/Documents/GitHub/PACHACK/data_csv/' + file, 'r') as openfile:
            modified_lines = []
            csvreader = csv.reader(openfile)
            for column in csvreader:
                #print(column)
                modified_lines.append(column)
            
            for i in range(0,len(modified_lines) - 50):
                modified_rows = []
                #print(modified_lines[i])
                wavelength = modified_lines[i][0]
                #print(wavelength)
                if 435 <= float(wavelength) <= 925:
                    #print("wavelength in range")
                    modified_rows.append(column)
            with open('/Users/christiangrinling/Documents/GitHub/PACHACK/data_csv_modified/' + file, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(modified_rows)



