"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Section: ENGR 102 536
Assignment: Lab6Indie
Date: 10-05-23
"""
from math import*

#prints context for situation
print("================================================")
print("|| This program will use linear approximation ||")
print("|| of a stress-strain curve, when given a     ||")
print("|| strain, the program will calculate stress. ||")
print("================================================")

while True:
    try:
        strain = float(input("Enter a strain (ideally between 0 - 30): ")) #asks user for strain
        if strain < 0:
            raise ValueError
        break
    except ValueError:
        print("Negative values are not accepted, please enter a Positive value")


if strain >=0 and strain <= 5:
    stress = strain * 1
    print("The stress is: " , stress, "N/m^2. This point is in the Young’s Modulus region")
elif strain >5 and strain <= 6:
    stress = (strain * .5) + 2.5
    print("The stress is: " , stress, "N/m^2. This point is in the linear elastic region")
elif strain >6 and strain <= 16:
    stress = 5.5
    print("The stress is: " , stress, "N/m^2. This point is in the plastic region region")
elif strain>16 and strain <= 25:
    stress = (.4 * strain) - .9
    print("The stress is: " , stress, "N/m^2. This point is in the strain hardening region")
elif strain >25 and strain <30:
    stress = (-.5 * strain) +21.6
    print("The stress is: " , stress, "N/m^2. This point is in the necking region")
else:
    print("You have passed the fracture point, this material broke at a strain of 30 and a stress of 6.6 N/m^2")


