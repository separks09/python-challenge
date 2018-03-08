#Import dependencies
import os
import csv
import pandas as pd

#Loop for user input
file_list = []
file_list = os.listdir("../PyBank_Raw")
print(file_list)
user_input = input("Type your choice from the files above to run:")
if user_input in file_list:
    
#Create a path to the csv file
    csv_file = '../PyBank_Raw/'+user_input+""

#Read csv into Pandas dataframe
    budget_pd = pd.read_csv(csv_file)

#Determine total number of months in dataframe
    date_counts = budget_pd["Date"].count()

#Determine total revenue
    total_revenue = budget_pd["Revenue"].sum()

#Determine change in revenue each month 
    monthly_revenue_change=budget_pd["Revenue"].diff()

#Determine average change in revenue each month
    avg_revenue_change = monthly_revenue_change.mean()
    avg_revenue_change = avg_revenue_change.astype(int)

#Determine maximum revenue and locate index of month it occurred in 
    max_revenue = monthly_revenue_change.max()
    max_revenue = max_revenue.astype(int)
    max_revenue_month = monthly_revenue_change[monthly_revenue_change == max_revenue].index[0]

#Determine minimum revenue and locate index of month it occurred in
    min_revenue = monthly_revenue_change.min()
    min_revenue = min_revenue.astype(int)
    min_revenue_month = monthly_revenue_change[monthly_revenue_change == min_revenue].index[0]

#Print results to terminal
    print("Financial Analysis")
    print("-------------------")
    print("Total Months: "+ str(date_counts))
    print("Total Revenue: $"+ str(total_revenue))
    print("Average Revenue Change: $"+str(avg_revenue_change))
    print("Greatest Increase in Revenue: {} ${}".format(budget_pd.iloc[max_revenue_month,0], max_revenue))
    print("Greatest Decrease in Revenue: {} ${}".format(budget_pd.iloc[min_revenue_month,0], min_revenue))

#Create text file name from original input
    noext_user_input = user_input.split(".")
    new_file = noext_user_input[0]

#Write text file using same terminal print values   
    f = open(""+new_file+".txt","w")
    f.write("Financial Analysis\n-------------------\nTotal Months: "+ str(date_counts)+"\nTotal Revenue: $"+ str(total_revenue)+"\nAverage Revenue Change: $"+str(avg_revenue_change))
    f.write("\nGreatest Increase in Revenue: {} ${}".format(budget_pd.iloc[max_revenue_month,0], max_revenue)+"\nGreatest Decrease in Revenue: {} ${}".format(budget_pd.iloc[min_revenue_month,0], min_revenue))
    f.close()
#Account for bad file path input  
else:
    print("Confirm file is csv and in folder \"PyBank_Raw\", then try again.")