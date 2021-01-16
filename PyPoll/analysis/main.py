#read csv file
import os

import csv

DIRPATH = "C:\\Users\\candi\\git\\Trilogy\\Homework\\03-Python\\python-challenge\\PyPoll\\Resources"

election_csv = os.path.join(DIRPATH,"election_data.csv")

with open(election_csv) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)


    # #create lists to store data 
    voter_id = []
    county = []
    candidate = []

#store data in lists
    for row in csv_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    cand1 = []
    for votes in candidate:
        if votes == "Khan":
            cand1.append(votes)
    
    cand2 = []
    for votes in candidate:
        if votes == "Correy":
            cand2.append(votes)

    cand3 = []
    for votes in candidate:
        if votes == "Li":
            cand3.append(votes)

    cand4 = []
    for votes in candidate:
        if votes == "O'Tooley":
            cand4.append(votes)

# calculate candidate percentages and round the outcome
cand1_percent = round((len(cand1) / len(voter_id) * 100), 2)
cand2_percent = round((len(cand2) / len(voter_id) * 100), 2)
cand3_percent = round((len(cand3) / len(voter_id) * 100), 2)
cand4_percent = round((len(cand4) / len(voter_id) * 100), 2)

# Print to terminal
print(f"Election Results")
print(f"--------------")
print(f"Total Votes: {len(voter_id)}")
print(f"--------------")
print(f"Khan: {cand1_percent}% ({len(cand1)})")
print(f"Correy: {cand2_percent}% ({len(cand2)})")
print(f"Li: {cand3_percent}% ({len(cand3)})")
print(f"O'Tooley: {cand4_percent}% ({len(cand4)})")
print(f"--------------")
print(f"Winner: Khan")
print(f"--------------")

# Path for Output

outputpath = "C:\\Users\\candi\\git\\Trilogy\\Homework\\03-Python\\python-challenge\\PyPoll\\analysis"
financial_analysis = os.path.join(outputpath, "election_analysis.txt")

# Output to txt file (copied from terminal)
f = open("election_analysis.txt", "w+")
f.write("Election Results")
f.write("--------------")
f.write("Total Votes: 3521001")
f.write("--------------")
f.write("Khan: 63.0% (2218231)")
f.write("Correy: 20.0% (704200)")
f.write("Li:  14.0% (492940)")
f.write("O'Tooley:  3.0% (105630)")
f.write("--------------")
f.write("Winner: Khan")
f.write("--------------")

f.close()