# file for PyBank exercise 
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

Date_list = []
Profit_Loss_list = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #There is a header row to skip in analysis
    csv_header = next(csvreader)
    for row in csvreader:
        # Handle the data as two lists
        Date_list.append(row[0])
        Profit_Loss_list.append(int(row[1]))

##Create a list of the various monthly increases and decreases in P&L (diffs) to calculate avg change
templist = Profit_Loss_list + [0]
del templist[0] 
diffs = [templist[i] - Profit_Loss_list[i] for i in range(len(Profit_Loss_list)-1)] #The -1 is because there is not data beyond our list to measure change.
templist.clear() #done with this
Average_Change = sum(diffs)/(len(diffs))

#find max and min from diffs.
Max_Prof = max(diffs)
Min_Prof = min(diffs)

# find the months that the max and min were in (remember diffs is reduced by 1 row at beginning [and the end, but no impact here].)
# come to think of it, this may find more than one month if multiple months have the max or min. Test later.
Great_Prof_Month = [Date_list[j+1]  for j in range(len(diffs)) if diffs[j] == Max_Prof]
Great_Loss_Month = [Date_list[k+1]  for k in range(len(diffs)) if diffs[k] == Min_Prof]

#store outputs to print, why not.
output1=  f"Total Months: {len(Date_list)}"
output2 = f"Total: ${sum(Profit_Loss_list)}"
output3 = f"Average Change: ${round(Average_Change,2)}"
output4 = f"Greatest Increase in Profits: {Great_Prof_Month} (${Max_Prof})"
output5 = f"Greatest Increase in Profits: {Great_Loss_Month} (${Min_Prof})"

###Terminal print statement here
print("Financial Analysis")
print("----------------------------")
print(output1)
print(output2)
print(output3)
print(output4)
print(output5)

###Text file print statement here
output_file = os.path.join("Analysis","PyBank_Analysis.txt")
#with the path and "a" meaning append as "datafile", print to "datafile"
#Note: All new runs of program will add to text file.
with open(output_file,"a") as datafile:  
    print("Financial Analysis",file = datafile)
    print("----------------------------",file = datafile)
    print(output1,file = datafile)
    print(output2,file = datafile)
    print(output3,file = datafile)
    print(output4,file = datafile)
    print(output5,file = datafile)
