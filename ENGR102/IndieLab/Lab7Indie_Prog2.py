"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Section: ENGR 102 536
Assignment: Lab7Indie_2
Date: 10-27-23
"""

#Vector Math

import math

def vector_magnitude(vector): #meathod to get magnitude
    return math.sqrt(sum([i**2 for i in vector]))

def vector_addition(v1, v2):  #meathod to get addition
    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_subtraction(v1, v2): #meathod to get subtraction
    return [v1[i] - v2[i] for i in range(len(v1))]

def dot_product(v1, v2):  #meathod to get dot product
    return sum([v1[i] * v2[i] for i in range(len(v1))])

# Input vectors
vector_A = [int(x) for x in input("Enter the elements for vector A: ").split()]
vector_B = [int(x) for x in input("Enter the elements for vector B: ").split()]

# Displaying results
print(f"The magnitude of vector A is {vector_magnitude(vector_A):.4f}")
print(f"The magnitude of vector B is {vector_magnitude(vector_B):.4f}")
print(f"A + B is {vector_addition(vector_A, vector_B)}")
print(f"A - B is {vector_subtraction(vector_A, vector_B)}")
print(f"The dot product is {dot_product(vector_A, vector_B)}")
