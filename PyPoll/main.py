import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
candidate_dict = {}
vote_count = 0
maximum = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)

# for each row in file, count total number of votes
    for row in csvreader:
        vote_count += 1

# candidate name on third column
        candidate_name = row[2]

# use dictionary to count vote per candidate
        if candidate_name in candidate_dict.keys():
            candidate_dict[candidate_name] += 1

# when first encountering the candidate, add a vote or will error
        else:
            candidate_dict[candidate_name] = 1

print("Election Results")
print("------------------")
print(f"Total Votes: {vote_count}")
print("-------------------")
    
# for each candidate, find the percentage by overall vote count
for candidate_name in candidate_dict.keys():
    perc = round((candidate_dict[candidate_name] / vote_count)*100,2)
    
    print(f"{candidate_name}: {perc}% ({candidate_dict[candidate_name]})")
   
# find the winner's name
    if candidate_dict[candidate_name] > maximum :
        maximum = candidate_dict[candidate_name]
        winner = candidate_name


print("-------------------")
print(f"Winner: {winner}")
print("-------------------")

# write results into a txt file
output_file = os.path.join("analysis","election_final.txt")

with open(output_file, "w") as finalfile:
    
    finalfile.write('Election Results\n')
    finalfile.write('------------------\n')
    finalfile.write(f"Total Votes: {vote_count}\n")
    finalfile.write("-------------------\n")
        
        
    for candidate_name in candidate_dict.keys():
        perc = round((candidate_dict[candidate_name] / vote_count)*100,2)
        
        finalfile.write(f"{candidate_name}: {perc}% ({candidate_dict[candidate_name]})\n")
   

 
    finalfile.write("-------------------\n")
    finalfile.write(f"Winner: {winner}\n")
    finalfile.write("-------------------\n")


# # prints entire dictionary
#     print(candidate_dict)
# # prints keys [all names in list]
#     print(candidate_dict.keys())
# # prints votes(values) by name
#     print(candidate_dict[candidate_name])
# # prints the name
#     print(candidate_name)

