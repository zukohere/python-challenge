# file for PyPoll exercise 
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

Date_list = []
Profit_Loss_list = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #There is a header row to skip in analysis
    csv_header = next(csvreader)
    Candidates = []
    Votes = []

    for row in csvreader:
        #checks each row to see if string in csv column 3 is in Candidates.
        # If so, increase vote count by 1  
        if row[2] in Candidates:
            for c in range(len(Candidates)):
                if row[2] == Candidates[c]:
                    Votes[c] = Votes[c]+1
        #If not already in Candidates, it just means we haven't come across them yet.
        #Add them to the list Candidates, and give them 1 vote. If we see them again, 
        #they'll meet the condition above
        else:
            Candidates.append(row[2])
            Votes.append(1)

    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {sum(Votes)}")
    print(f"-------------------------")
    for c in range(len(Candidates)):
        print(f"{Candidates[c]}: {round(Votes[c]/sum(Votes)*100,3)}% ({Votes[c]})")
        if Votes[c] == max(Votes):
            winner=c
    print(f"-------------------------")
    print(f"Winner: {Candidates[winner]}")
    print(f"-------------------------")

    output_file = os.path.join("Analysis","PyPoll_Analysis.txt")
    #Text file print statement here (path, filename)
    #Note: All new runs of program will overwrite text file.
    with open(output_file,"w") as datafile:
        print(f"Election Results",file = datafile)
        print(f"-------------------------",file = datafile)
        print(f"Total Votes: {sum(Votes)}",file = datafile)
        print(f"-------------------------",file = datafile)
        for c in range(len(Candidates)):
            print(f"{Candidates[c]}: {round(Votes[c]/sum(Votes)*100,3)}% ({Votes[c]})",file = datafile)
            if Votes[c] == max(Votes):
                winner=c
        print(f"-------------------------",file = datafile)
        print(f"Winner: {Candidates[winner]}",file = datafile)
        print(f"-------------------------",file = datafile)