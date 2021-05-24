# Election-Analysis
Weekly Assignment 3 - Election Audit analysis to be presented to the Colorado Board of Election Commission

## Overview of the Project

### Purpose and Background
The Colorado Board of Election Commission has asked to perform an election audit of the results for Congressional precint in Colorado. The key points in this project will be to
report the total number of votes cast, the total number of votes for each candidate as well as the county and the winner of the elections. Also we will be finding the county with
the largest turnover of votes.We will be using python programming language to perform these calculations and do our analysis as it will be more faster as compared to excel and can
automate our process. We will run a python script to do our analysis and write our script in a way, that can also be used for analysing election results in future for other Senate
and state elections.

## Election-Audit Results

- A total of 369,711 votes were cast in the Congressional election. This includes the votes of all the counties that is , Arapahoe , Jefferson and Denver.
  To get the total number of votes we just looped through all the rows in the file and stored the count in a variable that gave the total count of votes.

- During the election audit analysis we performed calculations over the three counties and their votes. After running the Python script we calculated individual votes per county
  and also their percentage out of the total votes casted. Following is the breakdown of votes against each county:
	Jefferson county received 38,855 votes which is 10.5% of the total votes.
	Denver county received 306,055 votes which is 82.8% of the total votes.
	Arapahoe received 24,801 votes which is 6.7% of the total votes.
	
- As we can see Denver county had the largest number of vote count.

- There were three candidates who stood in the election and received votes from each of the counties. As per the calculations and analysis performed on election results,
  following is the breakdown of votes against each candidate :
	Charles Casper Stockham received 85,213 votes which is 23% of the total votes.
	Diana DeGette received 272,892 votes which is 73.8% of the total votes.
	Raymon Anthony Doane received 11,606 votes which is 3.1% of the total votes.
	
- As we can see Diana DeGette received maximum number of votes ie, 272,892 votes which is a huge win as it constitutes 73.8% of the total votes casted in the elections.
  On the other hand Raymon Anthony Doane received the lowest number of votes in the election which is only 3% of the total votes casted.
  
  The results list and the outcomes of the election is summarized in the text file below:

  [election results](./Analysis/election_results.txt)
  

## Election-Audit Summary

This proposal outlines a plan to provide the Colorado Election Board of Commission , a readable and feasible way to perform an election audit.
We have used Python script which is a widely used programming language that is easy to read , learn and write. Also its an open source language that makes it easy to debug
and find errors and improves readability.
In this script we have used variables in the form of lists and dictionaries where we can easily add , delete and change the entries.
For any future elections we can modify this script , for example :

1. If we want to calculate how many votes each candidate received from each of the county, we can add a conditional loop on our input file reader to add an 
   additional key in the dictionary of candidate names and vote count. Using this key as the county name and votes from each county as the value , we can calculate
   total votes from each county that is received by a particular candidate. The output result for example will be like the following:
   
   {'Charles Casper Stockham': {'Jefferson': 19723, 'Denver': 57188, 'Arapahoe': 8302}, 
    'Diana DeGette': {'Jefferson': 17963, 'Denver': 239282, 'Arapahoe': 15647}, 
	'Raymon Anthony Doane': {'Jefferson': 1169, 'Denver': 9585, 'Arapahoe': 852}}
	
2. In our data for the election results if we have the total number of registered voters list in a county,we can find out how many people actually cast their vote
   out of the total registered voters in each county. 
   In our present data if we see some of the ballot IDs are missing for each county. Also in our python script we can loop through each row or voter and set a flag
   to "True" if a vote is counted against a particular ballot ID. If not we can set it to "False".
   This way it will give election commission an estimate of how many successful votings took place in each county for any election.
   
