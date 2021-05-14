# print("Hello World")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == "Denver" :
#     print(counties[1])

# if counties[1] != "Jeffesron" :
#     print(counties[2])
# #####

# temperature = int(input("What is the temp outside?  "))
# if temperature > 80 :
#     print("turn on AC")
# else :
#     print("open window")

# ######

# score = int(input("What is your score? "))
# if score >= 90 :
#     print("grade is A")
# elif score >=80 :
#     print("grade is B")
# elif score >= 70 :
#     print("grade is C")
# elif score >= 60 :
#     print("grade is D")
# else :
#     print ("grade is F")
# ######

# if "El Paso" in counties :
#     print("elpas is in the list")
# else:
#     print("elpaso is not in list")

# if "Arapahoe" in counties and "El paso" not in counties:
#     print ("only arapahoe is in counties")
# else:
#     print ("arapahoe is in list of countries and elpaso is not in list")
# ######

# for i in range(len(counties)):
#     print (counties[i])
# #######

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for voters in counties_dict.values():
#     print(voters)

# for county,voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered votes")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county in range(len(voting_data)):
#     print(voting_data[county].get('county'))

# for dict in voting_data:
#     for values in dict.values():
#         print (values)
# ##########

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

for count_dict in voting_data:
    county = ""
    votes = 0
    for key,value in count_dict.items() :
#        print (key + " : " + str(value))
        if key=="county" :
            county = value
        elif key == "registered_voters":
            votes = value
    print (f"{county} county has {votes:,} registered votes.")




##        print(f"{county} county has {voters} registered votes.")

# The data we need to retrieve
# 1. Total number of votes cast.
# 2. A complete list of all the candidates
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


import datetime as dt
now = dt.datetime.now()
print(now)

from datetime import datetime
now = datetime.now()
print(now)

#assign a variable to the file name to be loaded
file_to_load = 'Resources/election_results.csv'
#open thefile_to_load file and read the file
#election_data = open(file_to_load,'r')
#close the file
#election_data.close()
with open(file_to_load) as election_data:
    print(election_data)

#write the output file
import os
file_to_save = os.path.join("Analysis","election_analysis.txt")
outfile = open (file_to_save,"w")
outfile.write("Hello World")
outfile.close()

#write output file without close()
import os
file_to_save = os.path.join("Analysis","election_analysis.txt")
with open (file_to_save,"w") as txt_file:
    txt_file.write("Counties in Election\n--------------------\nArapahoe\nDenver\nJefferson")







    




