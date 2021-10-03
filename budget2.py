# import the os module 

import os

# import the csv file 

import csv 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

import csv 
csvpath = os.path.join('Bootcamp_copy,gt-virt-atl-data-pt-09-2021-u-c-b','02-Homework,03-Python','Instructions','Pybank', 'Resources', 'budget_data.csv')

#paste the path
#C:\Users\User\Documents\Bootcamp_copy\gt-virt-atl-data-pt-09-2021-u-c-b\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv
#C:\Users\User\Documents\Bootcamp_copy\buget.py

#lists of csv foles
total_months = []
net_profit = []
profit_change = []

# Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Open and read csv
with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
print(csvreader)

# Read the header row first (skip this step if there is now header)
csv_header = next(csvreader)
print(f"CSV Header: {csv_header}")

for row in csvreader:
        total_months.append(row[0])
        net_profit.append(row[1])
        

 # Take the difference between the months and append to monthly profit change
        for i in range(len(net_profit)-1):
            profit_change.append(net_profit[i+1]-net_profit[i])

# Obtain the max and min of the the montly profit change list
max_increase_value = max(profit_change)
max_decrease_value = min(profit_change)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = profit_change.index(max(profit_change)) + 1
max_decrease_month = profit_change.index(min(profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output = "output.txt"
with open("output","w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("--------------------")
    new.write("\n")
    new.write(f"Total Months:{len(total_months)}")
    new.write("\n")
    new.write(f"Total: ${sum(net_profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {total_months[monthly_decrease]} (${(str(increase))})")
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(net_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")





