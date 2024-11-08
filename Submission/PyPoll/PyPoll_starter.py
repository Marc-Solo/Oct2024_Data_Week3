# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
fileload = ("Resources/election_data.csv")  # Input file path
fileoutput = ("analysis/election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
vote_dict = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the CSV file and process it
with open(fileload) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in vote_dict:
            vote_dict[candidate_name] = 0

        # Add a vote to the candidate's count
        vote_dict[candidate_name] += 1


# Generate and print the winning candidate summary
output = f""""
Election Results
    
-----------------------------
Total Votes: {total_votes}
-----------------------------
"""

print(output)

# Loop through the candidates to determine vote percentages and identify the winner
for candidate_name in vote_dict.keys():
    votes = vote_dict[candidate_name]

    # Get the vote count and calculate the percentage
    vote_percentage = round((votes / total_votes) * 100, 3)

    # Candidate
    text = f"{candidate_name}: {vote_percentage}% ({winning_count})"
    print (text)

    # Update the winning candidate if this one has more votes
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

     

winner_output = f"""
-------------------------
Winner: {winning_candidate}
-------------------------
 """

output += winner_output
    
print(winner_output)       
 

# Write the results to a text file
with open(fileoutput, "w") as txt_file:
    txt_file.write(output)





