"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Section: ENGR 102 536
Assignment: Lab4Indie_Prog1
Date: 9-19-23
"""

print("input 3 number, and I will return the highest one.")
num1 =  float(input("Enter the 1st # : "))
num2 =  float(input("Enter the 2nd # : "))
num3 =  float(input("Enter the 3rd # : "))

if num1>num2 and num1>num3: # check num 1
    print(num1 ," is the biggest #")
elif num2>num1 and num2>num3: # check num 2
    print(num2 , " is the biggest #")
elif num3>num1 and num3>num2: # check num 3
    print(num3 , " is the biggest #")
else:
    print("There is no largest number, there may be equal values") #if the lagest actual is equal to another