"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Group Names: Peter, Quinton, Mrinal, Anish, Jared
Section: ENGR 102 536
Assignment: Lab2Indie_Act2-1
Date: 9-7-23
"""

x1 = 15     # time of measurement 1
y1 = 500    # distance at measurement 1
x2 = 45     # time of measurement 2
y2 = 2200   # distance at measurement 2
slope = (y2 - y1) / (x2 - x1)

current_time = float(input("Please input time in seconds: "))  # time for evaluation
distance_traveled = (slope * (current_time - x1) + y1)      # finds how far we've traveled
print("The distance traveled after", current_time, "seconds is", distance_traveled, "m")