#By submitting this assignment, we agree to the following:
#Aggies do not lie, cheat, or steal, nor tolerate those who do.
#We have not given or received any unauthorized aid on this assignment.
#Name: Anish Yakkanti
#Group Names: Peter, Quinton, Mrinal, Jared, Anish
#Section: ENGR 102 536
#Assignment: Lab2Indie_Act2-2
#Date: 9-7-23

import math
x1 = 15     # time of measurement 1
y1 = 500    # distance at measurement 1
x2 = 45     # time of measurement 2
y2 = 2200   # distance at measurement 2
slope = (y2 - y1) / (x2 - x1)

# Time is 60 seconds
current_time = float(input("Please input time in seconds: "))  # time for evaluation
distance_traveled = (slope * (current_time))      # finds how far we've traveled
print("After", current_time, "seconds the car has traveled", distance_traveled, "m")

distance_from_start = distance_traveled % (4000 * math.pi)              # distance_traveled mod the circumference
if distance_from_start > (2000 * math.pi):                              # Checks if you're past halfway
    distance_from_halfway = distance_from_start % (2000 * math.pi)      # If so, we mod half the circumference
    distance_from_start = (2000 * math.pi) - distance_from_halfway      # Half Circumference - distance from halfway
print("The car is", distance_from_start, "m from the start of the track\n")
