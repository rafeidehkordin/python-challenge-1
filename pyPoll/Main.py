#!/usr/bin/env python
# coding: utf-8

# In[64]:


# Modules
import os
import csv


# In[65]:


# Define variables

# Define output variables
vote_count = 0
candidates =[]
vote_stats={}
winner=""
output_text=""

# Define analysis variables
unique_candidates =set()
max_vote = 0
percentage =0


# In[66]:


# Set path for file
csvpath = os.path.join("..", "Resources", "PyPoll_Resources_election_data.csv")


# In[93]:


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    #Iterate through csv records to retrive the votes.
    for row in csvreader:
        
        candidates.append(row[2])


# In[94]:


#The total number of votes cast
vote_count =len(candidates)   


#A complete list of candidates who received votes
unique_candidates= set(candidates)

#Generate vote stats dictionary as {'candidate name': [total_votes,vote_percentage]}
vote_stats = {element:[0,0] for element in unique_candidates}

   
#The total number of votes each candidate won
for item in candidates:
    vote_stats[item][0] += 1


#The percentage of votes each candidate won
for items in vote_stats.values():
    
    percentage = items[0]/vote_count*100
    items[1]="{0:0.4g}".format(percentage)
    print(items[1])


#The winner of the election based on popular vote.
for key, value in vote_stats.items():
    
    if max_vote<value[0]:
        winner = key
        max_vote =value[0]
        


# In[95]:


output_text = "Election Results\n"
output_text += 40 * "-" + "\n"
output_text += f'Total Votes: {vote_count} \n'
output_text +=40 * "-" + "\n"

for key, value in vote_stats.items():
    
    output_text += f'{key}: {value[1]}% ({value[0]})\n'

output_text +=40 * "-" + "\n"

output_text += f'Winner: {winner}\n'
output_text +=40 * "-" + "\n"


# In[96]:


#Write output resluts into an output file

output_path = os.path.join("..","output" ,"polls.txt")

with open(output_path, 'w') as myfile:
    
    myfile.write(output_text)
    


# In[97]:


#Print results to terminal

print(output_text)


# In[ ]:





# In[ ]:




