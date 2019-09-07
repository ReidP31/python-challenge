import csv
import os

# Create the file path/directory
budget_csv = os.path.join('..','Resources','budget_data.csv')

# Define Budget Analysis Function
def Budget_Analysis():
    
    month = Budget_Data[0]
    total_months = []

    total_months.append(month)

    print(total_months)

     

    return

with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    
    for row in csv_reader:
    
        Budget_Analysis(row)

    
    

        

        
