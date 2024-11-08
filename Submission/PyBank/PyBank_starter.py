# Dependencies
import csv
import os

# File paths
filepath = "Resources/budget_data.csv"
fileoutput = "Resources/budget_analysis.txt"

# Initialize variables for tracking financial data
total_months = 0
sum_of_profit = 0
last_month_profit = 0
total_change = 0

# Track the greatest increases and decreases
greatest_increase_month = ""
greatest_decrease_month = ""
greatest_increase_profit = 0
greatest_decrease_profit = 0

# Open and read the CSV file
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip header

    # Process each row in the CSV file
    for row in csvreader:
        # Increment month count and add current months profit to total
        total_months += 1
        current_month_profit = int(row[1])
        sum_of_profit += current_month_profit

        # Handles the first row
        if total_months == 1:
            last_month_profit = current_month_profit
        else:
            # Calculate the change from the current and last month
            change = current_month_profit - last_month_profit
            total_change += change
            last_month_profit = current_month_profit

            # Update greatest increase and decrease in profit
            if change > greatest_increase_profit:
                greatest_increase_profit = change
                greatest_increase_month = row[0]
            elif change < greatest_decrease_profit:
                greatest_decrease_profit = change
                greatest_decrease_month = row[0]

# Generate the output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${sum_of_profit}
Average Change: ${round(total_change / (total_months - 1), 2)}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})
"""

print(output)

# Optionally write output to a file
with open(fileoutput, "w") as outputfile:
    outputfile.write(output)

