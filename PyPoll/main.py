# Create file path accross operating systems
import os

# Module for reading csv files
import csv

csvpath =os.path.join('.','Resources','budget_data.csv')
output = os.path.join("Analysis-Text", "Analysis.txt")

# Variable Declarations
# total vote counter
# candidate names list
#cadidate votes dictionary
# winner string
winner = ""
# winner number

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:
        #candidate
        #count votes

        # if candidate not in candidate_list:



#with open(output, "w") as file: