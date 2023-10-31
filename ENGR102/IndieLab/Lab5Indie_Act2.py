"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Section: ENGR 102 536
Assignment: Lab5Indie_Act2
Date: 9-26-23
"""
#Averaging measurements

userinput = 0.0
count = 0
total = 0
max_measurment = None
min_measurment = None 

while (userinput >= 0):

    userinput = float(input("enter as many measurements as you want, until entering a negative measurement."))
    if (userinput < 0): # if statment so negative number isnt considered
        break
    count += 1 # count used to calculate avg
    total += userinput # total used to calculate avg

    if max_measurment == None or max_measurment <= userinput: # gets maximum measurment
        max_measurment = userinput
    
    if min_measurment == None or min_measurment >= userinput: # gets minimum measurment
        min_measurment = userinput




avg = total/count # calculate avg given count and total
print ("the average is: ", avg)
print ("the minimum is: ", min_measurment) #Prints avg, min, max
print ("the maximum is: ", max_measurment)