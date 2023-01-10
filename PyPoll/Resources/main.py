import os
import csv

#path for data file
csvpath=os.path.join('election_data.csv')

#set our variables
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

#open the file
with open('election_data.csv') as csvfile:
    #open csv
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip the header
    header = next(csvreader)
    
    #iterate through each row
    for row in csvreader:
        
        #count unique variable IDs and call them total_votes
        total_votes+=1
        
        #if name is found count the times it appears and store in a list
        if row[2] == "Charles Casper Stockham": 
          charles_votes +=1
        elif row[2] == "Diana DeGette":
            diana_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            raymon_votes +=1
            
            
 #make a dictionary to find the winner           
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [charles_votes, diana_votes,raymon_votes]        
    
    
#zip together candidates and total votes; show the winner
dict_cand_and_votes = dict(zip(candidates,votes))
key = max(dict_cand_and_votes, key=dict_cand_and_votes.get)

#print our summary
charles_percent = (charles_votes/total_votes) *100
diana_percent = (diana_votes/total_votes) * 100
raymon_percent = (raymon_votes/total_votes)* 100

#print table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#export file
with open("election_analysis.txt", "w") as text_file:
    text_file.write(f"Election Results")
    text_file.write("\n")
    text_file.write(f"------------------------------")
    text_file.write("\n")
    text_file.write(f"Total Votes: {total_votes}")
    text_file.write("\n")
    text_file.write(f"------------------------------")
    text_file.write("\n")
    text_file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
    text_file.write("\n")
    text_file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
    text_file.write("\n")
    text_file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
    text_file.write("\n")
    text_file.write(f"------------------------------")
    text_file.write("\n")
    text_file.write(f"Winner: {key}")
    text_file.write("\n")
    text_file.write(f"----------------------------")