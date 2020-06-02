import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

# Title = []
# Price = []
# Subscriber_Count = []
# Number_of_Reviews = []
# # Course_Length = []
# encoding='utf-8'
months = 0
total_amount = 0
maximum = 0
minimum = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)
    # maximum = max(int(column[1].replace(',', '')) for column in csvreader)
    # maximum = min(csvreader, key=lambda row: int(row[1]))
    # maximum = max(csvreader, key=lambda column: int(column[1].replace(',','')))

    for row in csvreader:
        
        months = months + 1
        total_amount = total_amount + int(row[1])
    avg = total_amount/months
         

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)   
    maximum = max(csvreader, key=lambda row: int(row[1]))
    

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)   
    minimum = min(csvreader, key=lambda row: int(row[1]))

    print(f"Financial Analysis")
    print(f"__________________")    
    print(f"Total Months: {months}")
    print(f"Total :$ {total_amount}")
    print(f"Average Change: $ {round(avg,2)}")
    print(f"Greatest Increase in Profits: {maximum}")
    print(f"Greatest Decrease in Profits: {minimum}")


titles = ["Total Months", "Total: $", "Average Change: $", "Greatest Increase in Profits: ", "Greatest Decrease in Profits: "]
values = [months, total_amount, round(avg,2), maximum, minimum]
result_csv = zip(titles, values)

output_file = os.path.join("budget_final.csv")

with open(output_file, "w") as finalfile:
    writer = csv.writer(finalfile)
    
    writer.writerow(['Financial Analysis'])
    writer.writerow(['_____________________'])
    writer.writerows(result_csv)
