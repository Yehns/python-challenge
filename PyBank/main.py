# PyBank Analysis
# Import .csv to analyse
import os
import csv

# Set file upload and save path
budget_csv = os.path.join("C:\\Users\weima\\OneDrive\Desktop\\UWA Bootcamp\\Python\\python-challenge\\PyBank\\Resources\\budget_data.csv")
budget_analysis = os.path.join("C:\\Users\weima\\OneDrive\Desktop\\UWA Bootcamp\\Python\\python-challenge\\PyBank\\Analysis\\budget_analysis.txt")

# Set profit list comprehension
profit_loss = []

# Open budget_csv and read the file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)

# Set the row headers for the data
    csv_header = next(csv_file)

# Set total_months to a zero value 
total_months = 0 
# Determine the sum of rows
for row in open(budget_csv):
    total_months += 1

# Determine the "Net Total Profit/Losses" over the entire period - (as a sum off the raw data)
total = 0
with open(budget_csv, newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        total = total - int(row['Profit/Losses'])

# Determine the "Average Change" over the entire period 
average_change = []
with open(budget_csv, newline = '') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        average_change.append(float(row["Profit/Losses"]))
# Calculate the mean/average of the entire period 
        mean = sum(average_change)/len(average_change)

# Determine the "Greatest Increase" over the entire period
greatest_increase = []
with open(budget_csv, newline = '') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        greatest_increase.append(float(row["Profit/Losses"]))
# Use pythons "maximum" method to "grab" the largest value in the list
        maximum = max(greatest_increase)

# Determine the "Greatest Decrease" over the entire period
greatest_decrease = []
with open(budget_csv, newline = '') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        greatest_decrease.append(float(row["Profit/Losses"]))
# Use pythons "minimum" method to "grab" the lowest value in the list
        minimum = min(greatest_decrease)

# The finanl section prints all results in python and saves the results as a .txt file
with open(budget_analysis, "w") as txt_file:
# Setthe terminal print, and text file print values
    budget= (
f"-------------------------------------------------------\n"
f"Financial Analysis\n"
f"-------------------------------------------------------\n"
# Subtract final value by 1 to remove header row being counted for "total months"
f"Total Months = {total_months - (int(1))}\n"
f"Total Profit/Loss = ${total}\n"
f"Average Change = ${mean:.2f}\n"
f"Greatest Increase = ${maximum:.2f}\n"
f"Greatest Decrease = %{minimum:.2f}\n"
f"-------------------------------------------------------\n")
# Print analysis into terminal
    print(budget)
# Save analysis as a text file in specific folder
    txt_file.write(budget)