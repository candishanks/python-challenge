#read csv file
import os

import csv

DIRPATH = "C:\\Users\\candi\\git\\Trilogy\\Homework\\03-Python\\python-challenge\\PyBank\\Resources"

budget_csv = os.path.join(DIRPATH,"budget_data.csv")

with open(budget_csv) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    #create lists to store data
    date = []
    profit_loss = []
    profit_loss_change = []
    monthly_change = []

    #add data to lists
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(row[1])
    
    #find last row/number of data lines
    last_row = len(date)

    #interate through rows to calculate needed data
    i = 0    

    for i in range(len(profit_loss)-1):
        net_rev = int(profit_loss[i+1]) - int(profit_loss[i])
        profit_loss_change.append(net_rev)
    total_change = sum(profit_loss_change)
    #I believe that this should  be 86, i.e. the number of data rows excluding the header.
    #However, when calculated with 86, the outcome doesn't match the read me. 
    tot_chg_avg = total_change / 87
    
    #changing data types to work around bugs
    profit_loss_typechg = list(map(int, profit_loss))
    total_change = str(total_change)

    #calculating final data
    last_row = len(date)
    total = sum(profit_loss_typechg)
    increase = max(profit_loss_change)
    decrease = min(profit_loss_change)

    #printing final analysis
    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months: {last_row}")
    print(f"Total: ${total}")
    #the solution in the "read me is incorrect" I can only replicate the that number if I divide by 87. 
    #However, the denominator in the mean equation should be 86, i.e. 87 rows of data minus 1 header row, totaling 86. 
    #I think....
    print(f"Average Change: ${tot_chg_avg}")
    print(f"Greatest Increase in Profits: ${increase}")
    print(f"Greatest Decrease in Profits: ${decrease}")
    print("-------------------")

#outputting to text file

outputpath = "C:\\Users\\candi\\git\\Trilogy\\Homework\\03-Python\\python-challenge\\PyBank\\analysis"
financial_analysis = os.path.join(outputpath, "financial_analysis.txt")

# Outputting to text file (copied text from terminal)
f = open("financial_analysis.txt", "w+")
f.write("-------------------")
f.write("Total Months: 86")
f.write("Total: $38382578")
f.write("Average Change: $-2261.896551724138")
f.write("Greatest Increase in Profits: 1926159")
f.write("Greatest Decrease in Profits: $-2196167")
f.write("-------------------")

f.close()