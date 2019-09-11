'''In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.


As an example, your analysis should look similar to the one below:


  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------

In addition, your final script should both print the analysis to the terminal and export a text file with the results.'''

import os
import csv

# Create the file path/directory
election_csv = os.path.join('..','Resources','election_data.csv')



with open(election_csv, 'r') as election_file:
    csv_reader = csv.reader(election_file, delimiter=',')

    # Skip the first row
    header = next(csv_reader)

    # Create Empty Lists
    Voter_IDs = []
    Candidates = []
    Kahn_Votes = []
    Correy_Votes = []
    Li_Votes = []
    OTooley_Votes = []

    # Loop through the Data
    for row in csv_reader:

        ### Voter ID and Total Votes ###
        #------------------------------#

        # Create Voter_ID Variable
        Voter_ID = row[0]        
        # Fill Empty Voter List
        Voter_IDs.append(Voter_ID)
        # Calculate Total Votes
        Total_Votes = len(Voter_IDs)

        
        ### Reading Data to Find Candidate Names & Stats ###
        #--------------------------------------------------#
        if row[2] not in Candidates:
          Candidates.append(row[2])
        
        if row[2] == 'Khan':
          Kahn_Votes.append(row[2])
        elif row[2] == 'Correy':
          Correy_Votes.append(row[2])
        elif row[2] == 'Li':
          Li_Votes.append(row[2])
        elif row[2] == "O'Tooley":
          OTooley_Votes.append(row[2])

          # Get the % of Votes for each Candidate
          Khan_Total = len(Kahn_Votes)
          Correy_Total = len(Correy_Votes)
          Li_Total = len(Li_Votes)
          OTooley_Total = len(OTooley_Votes)

          Khan_Percent = format((Khan_Total / Total_Votes) * 100, '.3f')
          Correy_Percent = format((Correy_Total / Total_Votes) * 100, '.3f')
          Li_Percent = format((Li_Total / Total_Votes) * 100, '.3f')
          OTooley_Percent = format((OTooley_Total / Total_Votes) * 100, '.3f')

          # Find the Winner!
          Candidate_Totals = {'Khan': Khan_Total, 'Correy': Correy_Total, 'Li': Li_Total, "O'Tooley": OTooley_Total}
          
          Winner = max(Candidate_Totals, key=Candidate_Totals.get)



        
        

# Final Variables
Khan = Candidates[0]
Correy = Candidates[1]
Li = Candidates[2]
OTooley = Candidates[3]


### Output to .txt file
with open('main.txt', 'w+') as txt_file:
    
    txt_file.write('\n')
    txt_file.write('Election Results\n')
    txt_file.write('---------------------------\n')
    txt_file.write(f'Total Votes: {Total_Votes}\n')
    txt_file.write('---------------------------\n')
    txt_file.write(f'{Khan}: {Khan_Percent}% ({Khan_Total})\n')
    txt_file.write(f'{Correy}: {Correy_Percent}% ({Correy_Total})\n')
    txt_file.write(f'{Li}: {Li_Percent}% ({Li_Total})\n')
    txt_file.write(f'{OTooley}: {OTooley_Percent}% ({OTooley_Total})\n')
    txt_file.write(f'--------------------------\n')
    txt_file.write(f'Winner: {Winner}\n')
    txt_file.write(f'--------------------------\n')




print('')
print('Election Results')
print('---------------------------')
print(f'Total Votes: {Total_Votes}')
print('---------------------------')
print(f'{Khan}: {Khan_Percent}% ({Khan_Total})')
print(f'{Correy}: {Correy_Percent}% ({Correy_Total})')
print(f'{Li}: {Li_Percent}% ({Li_Total})')
print(f'{OTooley}: {OTooley_Percent}% ({OTooley_Total})')
print(f'--------------------------')
print(f'Winner: {Winner}')
print(f'--------------------------')
