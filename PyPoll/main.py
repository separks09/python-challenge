#Import dependencies
import os
import csv
import pandas as pd

#Loop for user input
file_list = []
file_list = os.listdir("../PyPoll_Raw")
print(file_list)
user_input = input("Type your choice from the files above to run:")
if user_input in file_list:

#Create a path to the csv file
    csv_file = '../PyPoll_Raw/'+user_input+""

#Read csv into Pandas DataFrame
    poll_df = pd.read_csv(csv_file)

#Determine total number of voters in DataFrame
    vote_counts = poll_df["Voter ID"].count()


#Find and store all candidates in array for iteration 
    candidate_array= poll_df["Candidate"].unique()

#Create new DataFrame to store calculated info from raw data
    election_totals_capture = {
        "Candidate": [],
        "Total Votes": [],
        "Percent of Votes": []
    }
    election_total_df = pd.DataFrame(election_totals_capture, columns=["Candidate", "Total Votes", "Percent of Votes"])

#Collect and calculate info from raw data, store to DataFrame 
    xx = 0
    for x in candidate_array:
        votes_candidate_df = poll_df.loc[poll_df["Candidate"]== candidate_array[xx],:]
        votes_candidate = votes_candidate_df["Voter ID"].count()
        percent_candidate = (votes_candidate/vote_counts)
        election_total_df = election_total_df.append({"Candidate":candidate_array[xx], "Total Votes":votes_candidate, "Percent of Votes":percent_candidate},ignore_index=True)
        xx = xx+1

# Sort the DataFrame by the values in the "Total Votes" column to find the winner
    election_total_df = election_total_df.sort_values("Total Votes",ascending = False)

# Reset the index and format for final presentation
    election_total_df = election_total_df.reset_index(drop=True)
    election_total_df["Percent of Votes"] = election_total_df["Percent of Votes"].map("{:.2%}".format)
    election_total_df["Total Votes"] = election_total_df["Total Votes"].map("{:.0f}".format)
    election_total_df.head()

#Return winner
    winner = election_total_df.iloc[0]["Candidate"]

#Print results to console
    print("Election Results \n-------------------------\nTotal Votes: "+str(vote_counts)+"\n-------------------------")
    y = 0
    for row in election_total_df:
        print(election_total_df.iloc[y]["Candidate"]+" : "+election_total_df.iloc[y]["Percent of Votes"]+" ("+election_total_df.iloc[y]["Total Votes"]+")")
        y = (y + 1)
    yy = -1
    print(election_total_df.iloc[yy]["Candidate"]+" : "+election_total_df.iloc[yy]["Percent of Votes"]+" ("+election_total_df.iloc[yy]["Total Votes"]+")")
    print("\n-------------------------\nWinner: "+winner+"\n-------------------------")

#Create text file name from original input
    noext_user_input = user_input.split(".")
    new_file = noext_user_input[0]

#Write text file using same terminal print values   
    f = open(""+new_file+".txt","w")
    f.write("Election Results \n------------------------\nTotal Votes: "+str(vote_counts)+"\n------------------------")
    y = 0
    for row in election_total_df:
        f.write("\n"+election_total_df.iloc[y]["Candidate"]+" : "+election_total_df.iloc[y]["Percent of Votes"]+" ("+election_total_df.iloc[y]["Total Votes"]+")")
        y = (y + 1)
    yy = -1
    f.write("\n"+election_total_df.iloc[yy]["Candidate"]+" : "+election_total_df.iloc[yy]["Percent of Votes"]+" ("+election_total_df.iloc[yy]["Total Votes"]+")")
    f.write("\n------------------------\nWinner: "+winner+"\n-------------------------")
    f.close()
#Account for bad file path input  
else:
    print("Confirm file is csv and in folder \"PyPoll_Raw\", then try again.")