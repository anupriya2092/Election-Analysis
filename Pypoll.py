import os
import csv
#creating path for input file
file_to_load = os.path.join("Resources","election_results.csv")
#creating path to write in an output txt file
file_to_save = os.path.join("Analysis","election_analysis.txt")

#open the input file in read mode
with open(file_to_load,"r") as election_data:
    #we will read the file using csv reader method
    file_reader = csv.reader(election_data,delimiter = ',')
    # for row in file_reader:
    #     print(row)
    file_header = next(file_reader)
    print (file_header)



