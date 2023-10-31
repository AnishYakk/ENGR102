'''
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Group Names: Peter, Quinton, Anish, Mrinal, Jared
Section: ENGR 102 536
Assignment: Lab5Team_Act1
Date: 9/26/23
'''
'''
Testing Results:
For 1x^3 + 3x^2 + x + 0
Left bound: -3
Right Bound: -2
Zero: (-2.6180340056307614, -9.882231566393784e-08)
22 Iterations

For 5x^3 - 6x^2 + 1x + 1
Left bound: 0
Right Bound: 1
Zero: Does Not Exist

For -1x^3 - 4x^2 + 3x + 7
Left Bound: 0
Right Bound: 1
Zero: (1.4426834434270859, -3.342008092488413e-08)
26 Iterations

For 1x^3 + 9x^2 + 26x +26
Left Bound: -5
Right Bound: -4
Zero: (-4.521379709243774, -1.4498127143269812e-08)
21 Iterations
'''
# Get a float value from the user
def get_float(prompt):
    value = "placeholder"
    while value == "placeholder":
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("That's not a float! Try again.")


def find_root():
    print("For Ax^3 + Bx^2 + Cx + D")
    a = get_float("Enter A: ")
    b = get_float("Enter B: ")
    c = get_float("Enter C: ")
    d = get_float("Enter D: ")
    left = get_float("Enter left bound: ")
    right = get_float("Enter right bound: ")
    count = 0

    def calc_value(x):          # automagically calculates f(x)
        return (a * x ** 3) + (b * x ** 2) + (c * x) + d

    midpoint = (left + right) / 2                                       # midpoint is the 'solution'
    while not(-0.0000001 < calc_value(midpoint) < 0.0000001):           # while error is outside of tolerance
        if (calc_value(left) > 0) and (calc_value(midpoint) > 0):       # if both positive
            left = midpoint                                                 # left becomes midpoint
        elif (calc_value(left) < 0) and (calc_value(midpoint) < 0):     # if both negative
            left = midpoint                                                 # left becomes negative
        else:                                                           # if differing signs
            right = midpoint                                                # right becomes midpoint
        count += 1
        midpoint = (left + right) / 2
        if count > 1000000:                                             # if it loops too long, break
            print("oops!")
            break

    print(f"There's a zero at f({midpoint})")
    print(f"f({midpoint}) = {calc_value(midpoint)}")
    print(f"It took {count} iterations to find the zero")


find_root()

