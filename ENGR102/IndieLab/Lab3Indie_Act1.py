#By submitting this assignment, we agree to the following:
#Aggies do not lie, cheat, or steal, nor tolerate those who do.
#We have not giver or received any unauthorized aid on this assignment.
#Name: Anish Yakkanti
#Group Names: N/A
#Section: ENGR 102 537
#Assignment: Indy Lab 3
#Date 9/12/23

import math

#Voltage across conductor
print("Enter the following outputs to calculate The voltage across a conductor") #introduce problem
resistance = float(input("Enter the resistance: "))
current = float(input("Enter the current: "))
print("The voltage across the conductor is", resistance*current, "volts.")

#Kenetic Energy Calculation
print("Enter the following outputs to calculate the kenetic energy of an object") #introduce problem
kg = float(input("Enter the mass(in kg): "))
velocity = float(input("Enter the velocity: "))
print("The kinetic energy of the object is", (1/2) * kg * velocity ** 2, "joules.")

#Standard Deviation
print("Enter 8 test scores (0-100) that will be used to calculate Standard Deviation") #introduce problem
# standard_deviation = sqrt(sum((x - mean)^2 for x in test_scores) / len(test_scores))
score1 = float(input("Enter a test score: "))
score2 = float(input("Enter a test score: "))
score3 = float(input("Enter a test score: "))
score4 = float(input("Enter a test score: "))
score5 = float(input("Enter a test score: "))
score6 = float(input("Enter a test score: "))
score7 = float(input("Enter a test score: "))
score8 = float(input("Enter a test score: "))
mean = ((score1+ score2+ score3+ score4+ score5+ score6+ score7+ score8)/8)
test_scores = [score1, score2, score3, score4, score5, score6, score7, score8]
standard_deviation = math.sqrt(sum((x - mean)**2 for x in test_scores) / 8)
print("The standard deviation for the test scores is", standard_deviation)

#Newton 2nd Law of Motion - force for movement
print("Enter the following outputs to calculate force required to move a Space X Spaceship") #introduce problem
mass = float(input("Enter the mass(in kg): ")) #kg is mass not wheght
acceleration_due_to_gravity = float(input("Enter the gravity of the planet (Earths is 9.81 m/s^2): "))
force = mass*acceleration_due_to_gravity
print("The force required to move the Space X Spaceship is", force, "N.")