"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Section: ENGR 102 536
Assignment: Lab5Indie_Act1
Date: 9-26-23
"""

#The Collatz conjecture

userinput = (int(input("Enter a positive integer That will be inputted in the Collatz Conjecture: ")))

if (userinput <= 0):
    print("The number entered was not a positive integer, please restart the program and enter a positive integer") # get user inpt

interation = 0;

while (userinput != 1): # stop when 1 is reached
    if (userinput%2 == 0): # check if even
        userinput = userinput/2
        interation += 1 #adds to interation
        print ("iteration #:", interation, " The new # is ", userinput)
    elif(userinput%2 != 0): # check if wrong
        userinput = (userinput*3)+1
        interation += 1 #adds to interation
        print ("iteration #:", interation, " The new # is ", userinput)

print ("it took ", interation, " interations of the Collatz conjecture to reach the value 1") # total interations

