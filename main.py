import os
import csv

#path for data file
csvpath=os.path.join('budget_data.csv')

#lists to store data
months = []
total_profit = []
profit_change = []

#open the file
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    header = next(csvreader)

    #iterate through rows
    for row in csvreader:
    
     #append months and total profit
     months.append(row[0])
     total_profit.append(int(row[1]))
    
    #iterate through profits to find monthly change
    for i in range(len(total_profit)-1):
    
     #take difference in two months and add to profit change
     profit_change.append(total_profit[i+1]-total_profit[i])
    
    #get minimum and maximum profit change
    greatest_increase = max(profit_change)
    greatest_decrease = min(profit_change)

    #associate min and max to appropriate month 
    greatest_increase_month = profit_change.index(max(profit_change)) + 1
    greatest_decrease_month = profit_change.index(min(profit_change)) + 1

    #print results
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months:{len(months)}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    print(f"Great Increase in Profits: {months[greatest_increase_month]} (${(str(greatest_increase))})")
    print(f"Great Decrease in Profits: {months[greatest_decrease_month]} (${(str(greatest_decrease))})")

#file export

with open("financial_analysis_sum.txt", "w") as text_file:
    
    #write how to print the summary
    text_file.write("Financial Analysis")
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(f"Total Months: {len(months)}")
    text_file.write("\n")
    text_file.write(f"Total: ${sum(total_profit)}")
    text_file.write("\n")
    text_file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    text_file.write("\n")
    text_file.write(f"Greatest Increase in Profits: {months[greatest_increase_month]} (${(str(greatest_increase))})")
    text_file.write("\n")
    text_file.write(f"Greatest Decrease in Profits: {months[greatest_decrease_month]} (${(str(greatest_decrease))})")
    