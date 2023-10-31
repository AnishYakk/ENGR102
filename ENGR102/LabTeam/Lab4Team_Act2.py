'''
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Group Names: Jared, Peter, Quinton, Mrinal
Section: ENGR 102 536
Assignment: Lab4Team_Act1
Date: 9/19/23
'''

import math
def get_float(prompt):
    value = "placeholder"
    while value == "placeholder":
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("That's not a float! Try again.")


def parking_fee():
    time_parked = get_float("How many hours were you parked? If you lost your ticket, enter the value as a negative number: ")
    fee = 0                                     # sets an initial value for the fee
    if time_parked < 0:                         # if the value is negative, increment the fee by 36
        fee += 36
        time_parked *= -1
    if time_parked == 0:                        # if the time is zero, zero is due
        print("No Charge")
        quit()
    while time_parked > 21:                     # 21 hours is when the max daily price is reached
        fee += 24                               # so we subtract 24 to go to the next day
        time_parked -= 24                       # and increment the fee accordingly

    if time_parked > 4:                         # time parked is between 4 and 21, so we take the fee for 0-4
        fee += 7 + (time_parked - 4)            # and add one dollar per hour past that

    elif time_parked > 2:                       # if time parked is between 2 and 4, we add the fee for
        fee += 7                                # 0-2 and 2-4

    elif time_parked > 0:                       # if time parked is between 0-2, we add the fee for
        fee += 4                                # 0-2, but not 2-4

    print(f"You owe: ${fee}")                   # prints the final fee

parking_fee()


