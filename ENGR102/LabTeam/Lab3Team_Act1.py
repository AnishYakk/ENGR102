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


#pounds(force) to newtons - Peter
def pounds_to_newtons(force_pounds):
    newtons = force_pounds * 4.44822
    return newtons
newtons = float(input("Enter pounds (force) to be converted into newtons: "))
print(newtons, "pounds of force is equal to", pounds_to_newtons(newtons), "newtons")


#kilometers to miles - Anish
def kilometers_to_miles(kilometers):
  miles = kilometers * 0.621371
  return miles
miles =  float(input("Enter the # of kilometers to be converted to Miles: "))
print("There are", kilometers_to_miles(miles), " km in", miles, "miles" )

#Seconds per revolution to Hertz - Mrinal
secs=float(input ("Enter the seconds per revolution -"))
hertz = secs # hertz and secs are 1-to-1
print(hertz,"hertz")

#Miles per Hour to Centimeter per Second - 

#Degrees Fahrenheit to degrees Rankine - Jared
