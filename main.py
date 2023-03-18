import os
import csv

csvpath = os.path.join("..", "budget_data.csv")

records = []
line_num = 0

#open csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Go to the next row from the start of the file
    header = next(csvreader)
    line_num += 1
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        PL = int(row[1])
        Date = row[0]
        #append row P/L value to list of records
        records.append(PL)

total_months = 0
total = 0
avg_profit_loss = 0
max_increase = 0
max_decrease = 0

for PL in records:
    total += PL
    total_months += 1
    print(total, total_months) 
    #Min/Max values
    if max_decrease == 0:
        max_decrease = PL
    elif PL > max_increase:
        max_increase = PL
    elif PL < max_decrease:
        max_decrease = PL
        
#calculate average
avg_profit_loss = round(total / total_months, 2)

#print values
print(max_increase, max_decrease, avg_profit_loss)

print("----------")

print(f"Total months: {total_months}")
print()
print(f"Total: ${total}")
print()
print(f"Greatest increase in profits: {max_increase}")
print()
print(f"Greatest decrease in profits: {max_decrease}")
print()
print(f"Average change: {avg_profit_loss}")

# Set output file name
output_path = 'output_main.txt'

# Open the output path as a file object
with open(output_path, 'w') as file:
    # Write to the output file
    file.write(f"Total months: {total_months}\n")
    file.write(f"------------------")
    file.write(f"Total: ${total}")
    file.write(f"------------------")
    file.write(f"Greatest increase in profits: {max_increase}")
    file.write(f"------------------")
    file.write(f"Greatest decrease in profits: {max_decrease}")
    file.write(f"------------------")
    file.write(f"Average change: {avg_profit_loss}")