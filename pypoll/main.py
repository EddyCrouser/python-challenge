import os
import csv

#used for checking which candidate won
counter = 0
#used to calculate the percentage votes for each candidate to be stored in the percentage array
percentage_var = 0
#stores all the unique candidates
candidate = []
#stores the vote totals for all the candidates
votes = []
#stores the percentage of the votes for each candidate
percentage = []
#gives the value of the winner based on their array slot
winner = 0

#opens the voter data for use
with open('./Resources/election_data.csv','r', encoding= 'utf') as mydata:
    #reads the data
    
    intel = csv.reader(mydata)
    #skips the first row since the headers aren't needed
    headerline = next(intel)
    #runs through the data and adds any candidate not in the array as well as increases the vote counter whenever a candidate comes up in the vote column
    for row in intel:
        if row[2] not in candidate:
            candidate.append(row[2])
            votes.append('1')
        else:
            for i in range(len(candidate)):
                if row[2] == candidate[i]:
                    votes[i] = int(votes[i]) + 1

total = 0
#sums the votes of all candidates to find the total votes cast
for i in range(len(candidate)):
    total = total + int(votes[i])
#calculates the percentage for each candidate then stores them in the percentage array so they correctly correspond to the candidate
for i in range(len(candidate)):
    percentage_var = round(100*int(votes[i])/total,3)
    percentage.append(str(percentage_var))

#starts to print out the results in the requested format
print()
print("Election Results:")
print()
print('---------------------------------')
print()
print('Total Votes: ' + str(total))
print()
print('---------------------------------')
print()
for i in range(len(candidate)):
    print(str(candidate[i]) + ": " + str(percentage[i]) + '% (' + str(votes[i]) + ')')
    print()
print('---------------------------------')
print()
#systematically checks which candidate has the largest number of votes and stores the winner
counter = int(votes[i])
for i in range(len(candidate)):
    if votes[i] >= counter:
        counter = int(votes[i])
        winner = i
print('Winner: ' + str(candidate[winner]))
print()
print('---------------------------------')
print()

#writes the results into a text document
with open('./Analysis/Analytics.txt','wt') as results:

    results.write('Election Results:\n\n')
    results.write('---------------------------------\n\n')
    results.write('Total Votes: ' + str(total) + '\n\n')
    results.write('---------------------------------\n\n')
    for i in range(len(candidate)):
        results.write(str(candidate[i]) + ": " + str(percentage[i]) + '% (' + str(votes[i]) + ')\n\n')
    results.write('---------------------------------\n\n')
    results.write('Winner: ' + str(candidate[winner]) + '\n\n')
    results.write('---------------------------------\n\n')
