import os
import csv

#Creating path to csv file:
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#Identifying functions:
total_months = 0
total_net_pl = 0
net_change_list = []
month_pull = []
greatest_increase = ["",0]
greatest_decrease = ["", 1000000000]

#Read CSV file and note header row as different
with open(budget_data_csv) as budgetcsv:
    csvreader = csv.reader(budgetcsv)    
    csv_header = next(csvreader)
    header_row = next(csvreader)
    total_months = total_months + 1
    total_net_pl = total_net_pl + int(header_row[1])
    prev_net = int(header_row[1])

#Compute variables
    for row in csvreader:
        
 #Total:       
        total_months = total_months + 1
        total_net_pl = total_net_pl + int(row[1])

 #Net Change:      
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_pull = month_pull + [row[0]]

#Greatest Increase:
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

#Greatest Decrease:
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change


#Average Net Change:
net_monthly_avg = sum(net_change_list)/len(net_change_list)

output_file = (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Net: ${total_net_pl}\n"
    f"Average Change: {net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(output_file)

budget_output_file = os.path.join("Analysis","budget_output.txt")

with open(budget_output_file, "w") as txt_file:
    txt_file.write(output_file)

          
















