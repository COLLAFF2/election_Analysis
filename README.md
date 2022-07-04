# Election_Analysis
using Python to collect election results and analyze
# Election_Analysis

## Project Overview
A Colorado Board of Elections requested an election audit of a recent local congressional election.
In said audit the following tasks are to be completed.

1. Calculate the total nummber of votes cast.
2. Get a complete lists of candidates who received votes.
3. Calculate total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of election based on popular vote.

## Resources 
-Data source: election_results.csv
-Software: Python 3.7.6, Visual Studio Code,1.68.1

## Summary
The analysis of the election show that:
-There were 369,711 votes cast in this election.
-The candidates were:
  -Charles Casper Stockham
  -Diana DeGette
  -Raymon Anthony Doane
-The candidate results were:
  -Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  -Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  -Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
-The winner of the election was:
  - Candidate Diana DeGette, who received 73.8% of votes and 272,892 number of votes.
  
## Challenge Overview
The Election commission requested additional data to complete the election audit. The equest included:

-The voter turnout for each county.
-The percentage of votes for each county out of total count.
-County with the highest turnout.


<img width="446" alt="Screen Shot 2022-07-02 at 6 02 41 PM" src="https://user-images.githubusercontent.com/107623913/177210110-92f5b111-62d7-44d1-a930-751c69da206e.png">

## Challenge Summary

Total votes for all counties were 369,711 as stated above. Denver had the highest turnout with 82.8% of the votes or 306,055 of votes cast. Jefferson county came in next with 10.5% of votes or 38,855 of votes cast. Lastly, Arapahoe came in with 6.7% of votes or 24,801 of votes cast.

I propose that this code can be used in future elections statewide. The python code is "robust" and can be used for any statewide election given the following:
- A seperate csv file for each election.
- A seperate election analysis file to record results.


The code does not "hard wire" candidates or counties and can therefore be used for any statewide election.




