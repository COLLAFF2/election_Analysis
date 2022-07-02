# The data we need to retrieve.
#1. total number of votes cast.
#2.A complete list of candidates that received votes
#3.The percentage of votes each candidate won
#4.The total number of votes each candidate won
#5.The winner of the election based on popular votes
import csv
import os
#6.Assign a variable for the file to load and the path
file_to_load=os.path.join("resources","election_results.csv")
#open the election results and read the file
with open(file_to_load) as election_data:
    print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
 # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()   

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    
     txt_file.write("counties in the election\n---------\nArapahoe\nDenver\nJefferson")
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
      # 2. Add to the total vote count.
        total_votes += 1   
    #Print candidate name for each row
        candidate_name = row[2]
     # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:    
        # Add the candidate name to the candidate list.
         candidate_options.append(candidate_name)
         # 2. Begin tracking that candidate's vote count.
         candidate_votes[candidate_name] = 0 
           # Add a vote to that candidate's count.
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
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)# Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage


   



   


   # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    # 4. Print the candidates' results to terminal

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#save the winning canidate's results to text file.
txt_file.write(winning_candidate_summary)




    






   