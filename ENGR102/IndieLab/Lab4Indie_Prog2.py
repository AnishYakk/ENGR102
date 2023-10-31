"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Section: ENGR 102 536
Assignment: Lab4Indie_Prog2
Date: 9-19-23
"""

reynoldNumber = 0

#take user input
print("Enter the following values to calculate the Reynold Number (𝑅e)")
v = float(input("Enter the Velocity of flow m/s : ")) #Velocity of flow m/s
d = float(input("Enter the pipe diameter (m) : ")) #pipe diameter (m)
fluid = float(input("Enter the fluid kinematic viscosity m^2/s : ")) # the fluid kinematic viscosity m^2/s

#Calculate The Re
reynoldNumber = (v*d)/fluid

#if statment to calculate output
if reynoldNumber < 2300: #flow is laminar
    print("The Reynold Number is ", reynoldNumber, " this means that the fluid is in laminar flow")
elif reynoldNumber > 2900: #fully turbulent
    print("The Reynold Number is ", reynoldNumber, " this means that the fluid is in fully turbulent")
else:
    print("The Reynold Number is ", reynoldNumber, " this means that the fluid is in transition") #in transition

