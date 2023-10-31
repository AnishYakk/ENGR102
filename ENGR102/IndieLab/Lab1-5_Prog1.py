
#By submitting this assignment, we agree to the following:
#Aggies do not lie, cheat, or steal, nor tolerate those who do.
#We have not giver or received any unauthorized aid on this assignment.
#Name: Anish Yakkanti
#Group Names: N/A
#Section: ENGR 102 537
#Assignment: Indy Lab 1.5
#Date 8/29/23


import math

#a
print ("I was born in Omaha, NE")

#b (voltage across conductor)
print("The voltage across the conductor is", 5*20, "volts.")

#c (KE = (1/2) * 100 kg * (21 m/s)^2 = 22050 J)
print("The kinetic energy of the object is", (1/2) * 100 * 21 ** 2, "joules.")

#d Standard Deviation
# standard_deviation = sqrt(sum((x - mean)^2 for x in test_scores) / len(test_scores))
mean = ((98+ 56+ 72+ 85+ 92+ 45+ 62+ 77)/8)
#make list for test scores
test_scores = [98, 56, 72, 85, 92, 45, 62, 77]
standard_deviation = math.sqrt(sum((x - mean)**2 for x in test_scores) / 8)
print("The standard deviation is", standard_deviation)

#e
#F = ma, F = 549,054 kg * 9.81 m/s^2 = 538,6219.74 N
force = 549054*9.81
print("The force required to move the Space X Falcon 9 is", force, "N.")
