'''
By submitting this assignment, we agree to the following:
"An Aggie does not lie, cheat, or steal, nor tolerate those who do"
"We have not given or received any unauthorized aid on this assignment"
Name: Anish
Group Names: Jared, Anish, Quinton, Mrinal, Peter
Section: ENGR 102 536
Assignment: Lab 7 Team Act 2
Date: 10/26/ 23

'''

import statistics                      #import stats and math
import math
def sort(a):                           #define our sorting function
    input_list = a.copy()
    output_list = []
    while bool(input_list):            #sort until input list is empty
        for i in input_list:
            if i == min(input_list):
                output_list.append(i)
                input_list.remove(i)
    return output_list                #pulls out the output_list

player_score = []                     #initialize lists to store our values
first_round_scores = []
second_round_scores = []
names = []
end = False                           #create a false value to flip
while not end:                        #collect data from users
    if (score1 := int(input("First Score: "))) >= 0:
        score2 = int(input("Second Score: "))
        name = input("Enter player name: ")
        print("Enter a negative value if finished.") #tell users how to stop
        player_score.append([score1, score2, name])  #adds to player scores and name to list
    else:
        end = True


for i in player_score:                #separates the players scores
    first_round_scores.append(i[0])   #1st round scores to list
    second_round_scores.append(i[1])  #2nd round scores to list
    names.append(i[2])                #player names to list

sorted_round_1 = first_round_scores   #create variable using separated values (1st round)
sorted_round_1 = sort(sorted_round_1) #sort the 1st round scores using defined sort function
sorted_round_2 = second_round_scores  #another variable using seperated values (2nd round)
sorted_round_2 = sort(sorted_round_2) #sort the 2nd round scores using the defined sort function

if len(sorted_round_1) % 2 == 0:      #get the median of the sorted 1st and 2nd round scores
    halfway_index = int(len(sorted_round_1) / 2) - 1
    median_1 = ((sorted_round_1[halfway_index]) + (sorted_round_1[halfway_index + 1])) / 2
#    median_1 = sorted_round_1[median_pos_1]
else:
    median_pos_1 = math.floor(len(sorted_round_1) / 2)
    median_1 = sorted_round_1[median_pos_1]

if len(sorted_round_2) % 2 == 0:
    halfway_index = int(len(sorted_round_1) / 2) - 1
    median_2 = ((sorted_round_2[halfway_index]) + (sorted_round_2[halfway_index + 1])) / 2
#    median_2 = sorted_round_2[median_pos_2]
else:
    median_pos_2 = math.floor(len(sorted_round_2) / 2)
    median_2 = sorted_round_2[median_pos_2]

safe_scores_1 = []                    #1st list initialization
for i in first_round_scores:          #find scores below median for 1st round
    if i < median_1:
        safe_scores_1.append(i)

safe_scores_2 = []                    #2nd list initialization
for i in second_round_scores:         #find scores below median for 2nd round
    if i < median_2:
        safe_scores_2.append(i)

safe_names = []                       #name list initialization
for i in player_score:                #finds the player names that were below median
    if i[0] in safe_scores_1 and i[1] in safe_scores_2:
        safe_names.append(i[2])


cut_names = []                        #cut list initialization
for i in player_score:                #finds player names who scored above the median
    if i[2] not in safe_names:
        cut_names.append(i[2])


print(f"After both cuts, {safe_names} are safe and {cut_names} are cut.")
# ^ prints out the players who made it (safe) and the players who lost (were cut).