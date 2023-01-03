#PyPoll Analysis
# Import .csv file to python 
import os
import csv

# Set file upload and save
election_data = os.path.join("C:\\Users\weima\\OneDrive\Desktop\\UWA Bootcamp\\Python\\python-challenge\\PyPoll\\Resources\\election_data.csv")
election_analysis = os.path.join("C:\\Users\weima\\OneDrive\Desktop\\UWA Bootcamp\\Python\\python-challenge\\PyPoll\\Analysis\\election_analysis.txt")

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

    # Set the row headers for the
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        
        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add the candidate list.
        if candidate_name not in candidates:
            
            # Add the candidate name to the candidate list.
            candidates.append(candidate_name)
            
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
with open(election_analysis, "w") as txt_file:

    intro = (
        f"-------------------------\n"
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(intro)
    txt_file.write(intro)

# Save the results to our text file.

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.3f}% ({votes:.3f})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        txt_file.write(candidate_results)
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    
        # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)