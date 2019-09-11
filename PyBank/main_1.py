import csv
import os

'''In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:


The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The average of the changes in "Profit/Losses" over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period


As an example, your analysis should look similar to the one below:


  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)'''



# Create the file path/directory
budget_csv = os.path.join('..','Resources','budget_data.csv')



with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')


    # Skip the first row
    header = next(csv_reader)

    # Empty Lists (PL = Profit/Losses)
    Month_List = []
    PL_List = []
    PL_Chngs_List = []
    PL_dict = {}
    PL_Prev = 0
   
    # Loop through the Data
    for row in csv_reader:

        # Declare Loop Variables
        Month = str(row[0])
        PL = int(row[1])
        
       
        # Fill the Lists
        Month_List.append(Month)
        PL_List.append(PL)
        # Create the PL Changes Variable & Fill Changes List
        PL_Change = PL - PL_Prev
        PL_Chngs_List.append(PL_Change)
        

        # Create PL Dictitionay
        PL_dict.update({row[0]: PL_Change})

        # Get Max & Min Key:Value Pairs
        PL_Max = max(PL_dict.values()) 
        PL_Max_Month = [i for i, v in PL_dict.items() if v == PL_Max]

        PL_Min = min(PL_dict.values())
        PL_Min_Month = [j for j, v in PL_dict.items() if v == PL_Min]
             
            

        # Re-assigning the new PL Previous Value
        PL_Prev = PL 
        
        
    # Post-Loop Variables
    Month_Total = len(Month_List)
    PL_Sum = sum(PL_List)
    PL_Chngs_Avg = sum(PL_Chngs_List[1:]) / (len(PL_Chngs_List) - 1)
    
### Output to .txt file
    with open('main_1.txt', 'w+') as txt_file:
       
        txt_file.write('\n')
        txt_file.write('Financial Analysis\n')
        txt_file.write('------------------\n')
        txt_file.write(f'Total Months: {Month_Total}\n')
        txt_file.write(f'Total: ${PL_Sum}\n')
        txt_file.write(f'Average Change: ${round(PL_Chngs_Avg, 2)}\n')
        txt_file.write(f'Greatest Increase in Profits: {PL_Max_Month} (${PL_Max})\n')
        txt_file.write(f'Greatest Decrease in Profits: {PL_Min_Month} (${PL_Min})\n')   
        txt_file.write('')
       
### Print the Output ###

print('')
print('Financial Analysis')
print('------------------')
print(f'Total Months: {Month_Total}')
print(f'Total: ${PL_Sum}')
print(f'Average Change: ${round(PL_Chngs_Avg, 2)}')
print(f'Greatest Increase in Profits: {PL_Max_Month} (${PL_Max})')
print(f'Greatest Decrease in Profits: {PL_Min_Month} (${PL_Min})')   
print('')
