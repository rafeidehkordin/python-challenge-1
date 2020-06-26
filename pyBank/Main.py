#!/usr/bin/env python
# coding: utf-8

# In[140]:


# Modules
import os
import csv


# In[141]:


# Define variables

# Define output variables
row_count = 0
avg_change = 0
max_increase = 0
max_decrease = 0
max_month = ""
min_month = ""
output_text =""

# Define analysis variables

net_pl = 0
my_pl = 0
last_pl = 0
my_change = 0
sum_change = 0
sum_pl = 0
is_first_row = True


# In[142]:


# Set path for file
csvpath = os.path.join("..", "Resources", "PyBank_Resources_budget_data.csv")


# In[143]:


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

#Iterate through csv records to calculate/retrive the desired values.   
  
    for row in csvreader:
       
        my_pl =float(row[1]) 
        my_month =str(row[0])
        
        #To skip the first row when calculating the monthly profit/loss changes.
        if is_first_row == False:
            
            my_change = (my_pl-last_pl)
            
        else:
            
            is_first_row = False
            
    
        #The total number of months included in the dataset
        row_count += 1
        

        #The net total amount of "Profit/Losses" over the entire period
        net_pl += my_pl       
        
        
        #The sum of the changes in "Profit/Losses" over the entire period 
        sum_change += my_change
        

        #The greatest increase in profits (date and amount) over the entire period
        if my_change > max_increase:
            max_increase = my_change
            max_month = my_month


        #The greatest decrease in losses (date and amount) over the entire period
        if my_change < max_decrease:
            max_decrease = my_change
            min_month = my_month
            
        last_pl = my_pl
            
#The average of the changes in "Profit/Losses" over the entire period 
avg_change = round(sum_change/(row_count-1),2)
        


# In[144]:


#Generate output text

output_text = "Financial Analysis\n"
output_text += 50 * "-" + "\n"
output_text +=f'Total months: {row_count}\n'
output_text +=f'Total: {net_pl}\nAverage Change: ${round(avg_change,2)}\n'
output_text +=f'Greatest Increase in Profits: {max_month} (${round(max_increase,2)})\n'
output_text +=f'Greatest Decrease in Profits: {min_month} (${round(max_decrease,2)})'


# In[145]:


#Write output resluts into an output file

output_path = os.path.join("..","output" ,"bank.txt")

with open(output_path, 'w') as myfile:
    
    myfile.write(output_text)


# In[146]:


#Print results to terminal

print(output_text)
    


# In[ ]:




