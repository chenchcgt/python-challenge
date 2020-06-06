import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

vote_count = 0
khan_count = 0
correy_count = 0
li_count = 0
tooley_count = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)

    for row in csvreader:

        vote_count += 1
        
        if row[2] == "Khan":
            khan_count += 1
        elif row[2] == "Correy":
            correy_count += 1
        elif row[2] == "Li":
            li_count += 1
        elif row[2] == "O'Tooley":
            tooley_count += 1
    
    khan_perc = (khan_count / vote_count)*100
    correy_perc = (correy_count / vote_count)*100
    li_perc = (li_count / vote_count)*100
    tooley_perc = (tooley_count / vote_count)*100

    def highest(array, n):
        max = array[0]

        for i in range(1,n):
            if array[i] > max:
                max = array[i]
        return max


    array = [correy_perc, li_perc, tooley_perc,khan_perc]
    n = len(array)
    winner = highest(array,n)




    if winner == khan_perc:
        winner_person = "Khan"
    elif winner == correy_perc:
        winner_person  = "Correy"
    elif winner == li_perc:
        winner_person = "Li"
    else:
        winner_person = "O'Tooley"


print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes:  {vote_count}")
print(f"--------------------------")
print(f"Khan: {round(khan_perc,2)}% ({khan_count})")
print(f"Correy: {round(correy_perc,2)}% ({correy_count})")
print(f"Li: {round(li_perc,2)}% ({li_count})")
print(f"O'Tooley: {round(tooley_perc,2)}% ({tooley_count})")
print(f"--------------------------")
print(f"Winner: {winner_person}")
print(f"--------------------------")



#Write to file
titles = ["Total Votes: ", "Khan: ", "Correy: ", "Li: ", "O'Tooley:", "Winner: " ]

values = [
vote_count, 
(str(round(khan_perc,2))+'% ('+ str(khan_count) + ')'),
(str(round(correy_perc,2))+'% ('+ str(correy_count) + ')'),
(str(round(li_perc,2))+'% ('+ str(li_count) + ')'),
(str(round(tooley_perc,2))+'% ('+ str(tooley_count) + ')'),
winner_person
]

# , round(khan_perc,2), round(avg,2), max_month_desc+'('+str(maximum)+')', min_month_desc+'('+str(minimum)+')']
result_csv = zip(titles, values)

output_file = os.path.join("analysis","election_final.csv")

with open(output_file, "w") as finalfile:
    writer = csv.writer(finalfile)
    
    writer.writerow(['Election Results'])
    writer.writerow(['------------------'])
    # writer.writerow(['Total Votes: ' + str(vote_count))
    writer.writerows(result_csv)
    writer.writerow(['------------------'])


