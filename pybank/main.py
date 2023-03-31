import os
import csv

#gives the running total
tally = 0
#stores the largest of the previous and current rows to find the max
big = 0
#stores the smallest of the previous and current rows to find the min
small = 0
#tallies how many rows we go through to find the number of months recorded
months = 0
#saves all the values in the second column so I have the first and last month to find the mean change per month
values = []
#will find the average change per month
avg = 0
#csvpath = os.path.join("./","Resources", "budget_data.csv")

difference = 0
#opens the budget dataset for use later on
with open('./Resources/budget_data.csv','r', encoding= 'utf',) as budgetdata:

    intel = csv.reader(budgetdata)
    print(intel)
    #skips the first row so that the data can be summed.
    headerline = next(intel)
    #runs through the rows, stores all the Profit/Losses data to an array for later, then as it works throught the rows, it makes a running total of profits and losses, and counts how many rows it's run through
    for row in intel:
        values.append(row[1])
        storage = row[1]
        months = months + 1
        tally = tally + int(storage)
            #runs two if statements which compare the previous profit/loss values to the one in the current row then saves the smaller and larger so we have the min and max
        if int(storage) < small:
            small = int(storage)
            smallest = row
        if int(storage) > big:
            big = int(storage)
            biggest = row
    
print(values)
#calculates the mean change per month using (last$-first$)/(#ofmonths-1)
avg = round((int(values[-1]) - int(values[0]))/(months-1),2)
#prints the data in the format requested
print("Data Analytics")
print()
print("---------------------------------------")
print()
print("Number of Months: " + str(months))
print()
print("Total: " + str(tally))
print()
print("The average change is: " + str(avg))
print()
print("Greatest Increase in Profits: " + biggest[1] + " on " + biggest[0])
print()
print("Greatest Decrease in Profits: " + smallest[1] + " on " + smallest[0])
print()

#writes the information into a text document
with open('./Analysis/Analytics.txt','wt') as results:

    results.write('Data Analytics\n\n')
    results.write("---------------------------------------\n\n")
    results.write("Number of Months: " + str(months) + '\n\n')
    results.write("Total: " + str(tally) + '\n\n')
    results.write("The average change is: " + str(avg) + '\n\n')
    results.write("Greatest Increase in Profits: " + biggest[1] + " on " + biggest[0] + '\n\n')
    results.write("Greatest Decrease in Profits: " + smallest[1] + " on " + smallest[0])
    