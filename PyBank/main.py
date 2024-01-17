# Create file path accross operating systems
import os

# Module for reading csv files
import csv

csvpath =os.path.join('.','Resources','budget_data.csv')
output = os.path.join("Analysis-Text", "Analysis.txt")

total_months = 0
profit_loss = 0
change_list =[]
greatest_profit = ["", 0]
greatest_loss = ["", 0]
 
# Method 1 Plain Reading of CSV files
    # with open(csvpath, 'r') as file_handler:
    # lines = file_handler.read()
    # print(lines)
# print(type(lines))

# Method 2: Improved reading using CSV module

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    # total_months = len(csvpath)
    # print(f"Number of months: {total_months}")
    # print(csvreader)

    csv_header = next(csvreader)
    # print(f"CSV Header:{csv_header}")
    total_months += 1
    first_row = next(csvreader)
    profit_loss += int(first_row[1])
    previous = int(first_row[1])
    
    for row in csvreader:
        total_months += 1
        profit_loss += int(row[1])
        change = int(row[1]) - previous
        change_list.append(change)
        previous = int(row[1])   

        if change > greatest_profit[1]:
            greatest_profit[1] = change
            greatest_profit[0] = row[0] 
        
        if change < greatest_loss[1]:
            greatest_loss[1] = change
            greatest_loss[0] = row[0] 
avg_monthlychg = sum(change_list) / len(change_list)

with open(output, "w") as file:
    bank_results = (
        f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${profit_loss}
Average Change: ${avg_monthlychg:.2f}
Greatest Increase in Profits: {greatest_profit[0]} ${greatest_profit[1]}
Greatest Decrease in Profits: {greatest_loss[0]} ${greatest_loss[1]}
"""
    )
    print(bank_results)
    file.write(bank_results)