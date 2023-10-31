#Aggies do not lie, cheat, or steal, nor tolerate those who do.
#We have not giver or received any unauthorized aid on this assignment.
#Name: Anish Yakkanti
#Group Names: N/A
#Section: ENGR 102 537
#Assignment: Linear Interpolation
#Date 9/07/23


# Define the two observed positions
position_1 = 12
x1=8
y1=6
z1=7

position_2 = 85
x2=-5
y2=30
z2=9

# Find the time difference between the two positions

xslope = (x2-x1)/(position_2-position_1) # change in x
yslope = (y2-y1)/(position_2-position_1) # change in  y
zslope = (z2-z1)/(position_2-position_1) # change in z

time = 30.0

print("At time ", time," seconds:")

print("x1 =" , xslope * (time - position_2) + x2 , "m") #slope intercept form
print("y1 =" , yslope * (time - position_2) + y2 , "m")#used to calculate positions
print("z1 =" , zslope * (time - position_2) + z2 , "m")#for all 3 demensions
print("-----------------------")

time += 7.5 #previous time variale + 5

print("At time ", time," seconds:")

print("x2 =" , xslope * (time - position_2) + x2 , "m")
print("y2 =" , yslope * (time - position_2) + y2 , "m")
print("z2 =" , zslope * (time - position_2) + z2 , "m")
print("-----------------------")

time += 7.5

print("At time ", time," seconds:")

print("x3 =" , xslope * (time - position_2) + x2 , "m")
print("y3 =" , yslope * (time - position_2) + y2 , "m")
print("z3 =" , zslope * (time - position_2) + z2 , "m")
print("-----------------------")

time += 7.5

print("At time ", time," seconds:")

print("x4 =" , xslope * (time - position_2) + x2 , "m")
print("y4 =" , yslope * (time - position_2) + y2 , "m")
print("z4 =" , zslope * (time - position_2) + z2 , "m")
print("-----------------------")

time += 7.5

print("At time ", time," seconds:")

print("x5 =" , xslope * (time - position_2) + x2 , "m")
print("y5 =" , yslope * (time - position_2) + y2 , "m")
print("z5 =" , zslope * (time - position_2) + z2 , "m")

