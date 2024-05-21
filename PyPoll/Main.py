import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

total_votes_cast = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

with open(election_data_csv) as election_csv:
    csvreader = csv.reader(election_csv)
    csvheader = next(csvreader)
    total_votes_cast = total_votes_cast + 1

    for row in csvreader:
        # total votes cast:
        total_votes_cast = total_votes_cast + 1
        
        # total votes for stockham:
        if row[2] == "Charles Casper Stockham":
            stockham_votes = stockham_votes + 1
        # stockham percentage of votes:
        stockham_percentage = stockham_votes / total_votes_cast * 100
        
        # total votes for degette:
        if row[2] == "Diana DeGette":
            degette_votes = degette_votes + 1
        # degette percentage of votes:
        degette_percentage = degette_votes / total_votes_cast * 100
        
        # total votes for doane:
        if row[2] == "Raymon Anthony Doane":
            doane_votes = doane_votes + 1
        # doane percentage of votes:
        doane_percentage = doane_votes / total_votes_cast * 100
        
        # determining winner
        winner = max(stockham_votes,degette_votes,doane_votes)
        if winner == stockham_votes:
            name_of_winner = "Charles Casper Stockham"
        elif winner == degette_votes:
            name_of_winner = "Diana DeGette"
        elif winner == doane_votes:
            name_of_winner = "Raymon Anthony Doane"

output_file = (
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes Cast: {total_votes_cast}\n"
    f"-----------------------------\n"
    f"Charles Casper Stockham: {stockham_percentage:.3f}% ({stockham_votes})\n"
    f"Diana DeGette: {degette_percentage:.3f}% ({degette_votes})\n"
    f"Raymon Anthony Doane: {doane_percentage:.3f}% ({doane_votes})\n"
    f"-----------------------------\n"
    f"Winner: {name_of_winner}\n"
    f"-----------------------------\n"
)
print(output_file)

election_output_file = os.path.join("Analysis","election_output.txt")

with open(election_output_file, "w") as txt_file:
    txt_file.write(output_file)
