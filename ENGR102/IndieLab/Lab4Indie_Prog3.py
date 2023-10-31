"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Section: ENGR 102 536
Assignment: Lab4Indie_Prog3
Date: 9-19-23
"""
print ("-----------------------------------------------------------------------------------------------")
print ("|A machine during its initial testing phase produces 10 widgets a day. After 10 days           |")
print ("| of testing (starting on day 11), it begins to run at full speed, producing 40 widgets a day. |")
print ("| After 50 days at full speed (days 11-60), it gradually starts becoming less                  |")
print ("| productive, and produces 1 fewer widget per day, (ie. 39 widgets on day 61, etc.)            |") # made this look cool
print ("| until on day 100 it no longer produces any widgets                                           |") # situation explained to user
print ("-----------------------------------------------------------------------------------------------")

day = float(input("Enter a day between 0-100, and the total # of widgets produced will be outputted: "))

slope1 = 10
slope2 = 40
def slope(day):
    if day >= 0 and day <= 10:
        return day * slope1
    elif day > 10 and day <= 60:
        return 10 * slope1 + (day - 10) * slope2  # total widgets at day 10 + 40 widgets per day
    elif day > 60 and day <= 100:
        m = (10 * slope1) + (50 * slope2)
        day_over60 = day-60
        while (day_over60 > 0):
         m += (40 - (day_over60))  # 10 widgets at 10 days, 50 days at 40 widgets/day, then decreasing by 1 per day
         day_over60 = day_over60 - 1
        return m
    else:
        print("Your input did not meet the specification (0 - 100)")
        return 0  # Return 0 if the input is out of range

total_widgets = slope(day)

print(f"{total_widgets} widgets have been produced in {day} days")
