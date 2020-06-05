import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")


months = 0
total_amount = 0
maximum = 0
minimum = 0
amount_prior = 0
difference_current = 0
difference_sum = 0
avg_month = 0
avg = 0
compare_current = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)

# Loop through rows
    for row in csvreader:
        
        months = months + 1
        total_amount = total_amount + int(row[1])
        if row[0] != 'Jan-2010':
            difference_current = int(row[1]) - amount_prior
            difference_sum = difference_sum + difference_current
            amount_prior = int(row[1])
            compare_current = difference_current

        # Calculate average by total months - first month
            avg_month = months - 1
            avg = difference_sum/avg_month
           
        #    Compare if current difference is larger than max
            if compare_current >= maximum:

                maximum = compare_current          
                max_month_desc = row[0]

        # Compare if current difference is lower than min
            elif compare_current <= minimum:

                minimum = compare_current
                min_month_desc = row[0]
        else:
            amount_prior = int(row[1])


# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     headers = next(csvreader, None)  
#     maximum = max(csvreader, key=lambda row: int(row[1]))
    

# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     headers = next(csvreader, None)   
#     minimum = min(csvreader, key=lambda row: int(row[1]))

    # Output print

    print(f"Financial Analysis")
    print(f"__________________")    
    print(f"Total Months: {months}")
    print(f"Total :$ {total_amount}")
    print(f"Average Change: $ {round(avg,2)}")
    print(f"Greatest Increase in Profits: {max_month_desc} (${maximum})")
    print(f"Greatest Decrease in Profits: {min_month_desc} (${minimum})")

# Write to file

titles = ["Total Months", "Total: $", "Average Change: $", "Greatest Increase in Profits: ", "Greatest Decrease in Profits: "]
values = [months, total_amount, round(avg,2), max_month_desc+'('+str(maximum)+')', min_month_desc+'('+str(minimum)+')']
result_csv = zip(titles, values)

output_file = os.path.join("budget_final.csv")

with open(output_file, "w") as finalfile:
    writer = csv.writer(finalfile)
    
    writer.writerow(['Financial Analysis'])
    writer.writerow(['_____________________'])
    writer.writerows(result_csv)
