'''
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Group Names: Peter, Quinton, Anish, Mrinal, Jared
Section: ENGR 102 536
Assignment: Lab5Team_Act2
Date: 9/26/23
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


# derivative of cubic polynomial at x = input
def find_deriv():
    print("For Ax^3 + Bx^2 + Cx + D")
    orig_a = get_float("Enter A: ")             # gets inputs
    orig_b = get_float("Enter B: ")
    orig_c = get_float("Enter C: ")
    orig_d = get_float("Enter D: ")

    def calc_value(x):                            # automagically calculates f(x)
        return (orig_a * x ** 3) + (orig_b * x ** 2) + (orig_c * x) + orig_d
    print(f"The derivative of\n{orig_a}x^3 + {orig_b}x^2 + {orig_c}x + {orig_d} is")
    d = 1 * orig_c                              # finds coefficients of derivatives
    c = 2 * orig_b
    b = 3 * orig_a
    a = 0
    print(f"{b}x^2 + {c}x + {d}")               # prints derivative
    value = get_float("Evaluate at: ")          # gets where to evaluate at
    print(f"The exact derivative at {value} is {(b * (value ** 2)) + (c * value) + d}")

    limit_length = 0.1                          # this approaches zero
    difference = 1                              # initialize
    count = 0                                   # initialize
    evaluate1 = 0                               # initialize
    evaluate2 = 0                               # initialize
    while not(-0.0000001 < difference < 0.0000001):             # while difference outside of tolerance
        evaluate1 = (calc_value(value + limit_length) - calc_value(value)) / limit_length       # difference quotient
        limit_length = limit_length / 2                                 # approaches zero
        evaluate2 = (calc_value(value + limit_length) - calc_value(value)) / limit_length       # difference quotient
        difference = evaluate1 - evaluate2                              # checks tolerance
        count += 1                                                      # increments count
    print(f"The derivative using limits at {value} is {evaluate2}")
    print(f"There were {count} iterations")


find_deriv()