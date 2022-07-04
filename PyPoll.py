# The data we need to retrieve.
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
#file_to_load = r'C:\Users\LaStella\dabc\DataClass\Election_Analysis\Resources\election_results.csv'
# "FileNotFound" error when only "Resources" is used. 
# Needs entire path, with double slashes.
file_to_load = os.path.join("C:\\Users\\LaStella\\dabc\\DataClass\\Election_Analysis\\Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("C:\\Users\\LaStella\\dabc\\DataClass\\Election_Analysis\\analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
# Print the file object.
    print(election_data)

    # To do: perform analysis.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.
#    for row in file_reader:
#        print(row)









