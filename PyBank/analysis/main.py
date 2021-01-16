import os

import csv

DIRPATH = "C:\\Users\\candi\\git\\Trilogy\\Homework\\03-Python\\python-challenge\\PyBank\\Resources"

budget_csv = os.path.join(DIRPATH,"budget_data.csv")

with open(budget_csv) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    date = []
    profit_loss = []
    profit_loss_change = []
    monthly_change = []

    
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(row[1])
    

    last_row = len(date)

    i = 0    

    for i in range(len(profit_loss)-1):
        net_rev = int(profit_loss[i+1]) - int(profit_loss[i])
        profit_loss_change.append(net_rev)
    total_change = sum(profit_loss_change)
    tot_chg_avg = total_change / 86
    
    profit_loss_typechg = list(map(int, profit_loss))
    total_change = str(total_change)

    last_row = len(date)
    total = sum(profit_loss_typechg)
    increase = max(profit_loss_change)
    decrease = min(profit_loss_change)

    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months: {last_row}")
    print(f"Total: ${total}")
    print(f"Average Change: ${tot_chg_avg}")
    print(f"Greatest Increase in Profits:: ${increase}")
    print(f"Greatest Decrease in Profits:: ${decrease}")
    print("-------------------")






 










#  ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```