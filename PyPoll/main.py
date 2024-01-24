# Create file path accross operating systems
import os

# Module for reading csv files
import csv

csvpath =os.path.join('.','Resources','election_data.csv')
output = os.path.join("Analysis-Text", "Election-Analysis.txt")

# Variable Declarations
total_votes = 0

# candidate names list
candidate_names = []

#cadidate votes dictionary
candidate_votes = {}

# winner string
winner = ["", 0]

# winner number

#read csvpath
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    
#loop through rows to count total votes 
#add candidate name into dictionary with a vote for the candidate
    for row in csvreader:
       
        candidate = row[2]
        total_votes += 1
        if candidate not in candidate_names:
            candidate_names.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] +=1

print(candidate_votes)

#write the results as text to text file

with open(output, "w") as txtfile:
    election_results = (f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
""")
    print(election_results)
    txtfile.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percent = votes / total_votes * 100
        print(f"{candidate}: {percent:.3f}% ({votes})")
        txtfile.write(f"{candidate}: {percent:.3f}% ({votes})\n")

        if votes > winner[1]:
            winner[1] = votes
            winner[0] = candidate
    winning_canidate = (f"""
-------------------------
Winner: {winner[0]}
-------------------------
""")
    print(winning_canidate)

    txtfile.write(winning_canidate)


        # candidate += str(row[2])
        # change_candidate = str(row[2]) - new_candidate
        # candidate.append(change_candidate)
        # new_candidate = str(row[2])

        #count votes

        # if candidate not in candidate_list:



#with open(output, "w") as file:
#         with open(output, "w") as file:
#             election_results = (
#         f"""
# Financial Analysis
# ----------------------------
# Total Months: {total_months}
# Total: ${profit_loss}
# Average Change: ${avg_monthlychg:.2f}
# Greatest Increase in Profits: {greatest_profit[0]} ${greatest_profit[1]}
# Greatest Decrease in Profits: {greatest_loss[0]} ${greatest_loss[1]}
# """
#     )
#     print(election_results)