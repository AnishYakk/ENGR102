#By submitting this assignment, we agree to the following:
#Aggies do not lie, cheat, or steal, nor tolerate those who do.
#We have not giver or received any unauthorized aid on this assignment.
#Name: Anish Yakkanti
#Group Names: N/A
#Section: ENGR 102 537
#Assignment: Indy Lab 3
#Date 9/12/23

from math import*

#Radius of a circle
circle_area = float(input("Enter the area of a circle (in^2): "))
print(f"The radius of a circle with a area {circle_area:.2f} in^2 is {sqrt(circle_area / pi):.3f} inches" )

#Side length of an equalateral Triangle
triangle_area = float(input("Enter the area of an equalateral triangle (in^2): "))
print(f"Side length of an equalateral Triangle with an area of {triangle_area:.2f} in^2 is {sqrt(4 * triangle_area / sqrt(3)):.3f} inches")

#Side length of a square
square_area = float(input("Enter the area of an square (in^2): "))
print(f"The side length of a square with the area {square_area:.2f} in^2 is {sqrt(square_area):.3f} inches")