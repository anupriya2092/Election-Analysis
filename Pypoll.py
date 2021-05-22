import os
import csv
#creating path for input file
file_to_load = os.path.join("Resources","election_results.csv")
#creating path to write in an output txt file
file_to_save = os.path.join("Analysis","election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#open the input file in read mode
with open(file_to_load,"r") as election_data:
    #we will read the file using csv reader method
    file_reader = csv.reader(election_data,delimiter = ',')
    #read only the header row and skip the header
    file_header = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
# Add the candidate name to the list            
            candidate_options.append(candidate_name) 
# Begin tracking the candidate's vote count and set the value to zero            
            candidate_votes[candidate_name] = 0
# Add a vote to each candidate's count everytime and it will be set to zero when a new candidate's name comes            
        candidate_votes[candidate_name] += 1 
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:  
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)       
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        # compare the votes of each candidate and its percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage) :
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    #print(total_votes) 
    #print(candidate_options) 
    #print(candidate_votes)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    



