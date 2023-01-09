# PyPoll Analysis
# Import .csv file to python 
import os
import csv

# Set file upload and save
election_data = os.path.join("Resources\\election_data.csv")
election_analysis = os.path.join("Analysis\\election_analysis.txt")

# Set "Total Votes" variable as zero
total_votes = 0

# Set candidates and candidate_votes list comprehension
candidates = []
candidate_votes = {}

# Set winner as a name, and set winning_count and winning_percentage as 0
winner = ''
winning_count = 0
winning_percentage = 0

# Open election_data and read the file
with open(election_data) as election_data:
    file_reader = csv.reader(election_data)

# Set the row headers for the data
    headers = next(file_reader)

# Determine the sum of rows
    for row in file_reader:
        total_votes += 1

# Identify the candidate_name from each row
        candidate_name = row[2]

# If candidate_name does not match existing candidate, add new candidate_name to list
        if candidate_name not in candidates:
            
# Add candidate_name to list
            candidates.append(candidate_name)
            
# Determine total candidate_votes for each candiidate_name
            candidate_votes[candidate_name] = 0
        
# Add a value to candidate_name for each candidate_vote
        candidate_votes[candidate_name] += 1
with open(election_analysis, "w") as txt_file:

# Print total_votes into terminal and text file
    intro = (
        f"-------------------------\n"
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(intro)
    txt_file.write(intro)

# Determine the associated total votes and percentage of votes for each candidate_name
    for candidate_name in candidate_votes:
        # Determine candidate_votes and vote_percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
# Set candidate_results as string for printing and saving
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.3f}% ({votes:.0f})\n")

# Print and save candidate_results
        print(candidate_results)
        txt_file.write(candidate_results)
        
# Determine winnng_candidate as a the greatest vote_percentage from candidate_results
        if (vote_percentage > winning_percentage):
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    
# Print the winning candidate's results to the terminal and text file
    end= (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(end)
    txt_file.write(end)
