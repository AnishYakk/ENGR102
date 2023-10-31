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

def get_float(prompt):
    value = "placeholder"
    while value == "placeholder":
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("That's not a float! Try again.")
def find_change():
    cost = get_float("How much does the item cost? ")                   # Gets input from user
    paid = get_float("How much did you pay? ")                          # Gets input from user
    change = paid - cost
    if change < 0:                                                      # Checks if the amount paid > cost
        print("An Aggie does not lie, cheat, or STEAL!")
        quit()
    change_hold_value = change                                          # Stores in another value so we can manipulate
    twenties = 0                                                        # change but remember the value later
    tens = 0
    fives = 0                                                           # Initializes values
    twos = 0
    ones = 0
    half_dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while change > 0:                                                   # if change > 0 take out the highest
        change = round(change, 2)   # manually rounds to avoid error    # denomination possible
        if (change - 20) >= 0:
            twenties += 1
            change -= 20
        elif (change - 10) >= 0:
            tens += 1
            change -= 10
        elif (change - 5) >= 0:
            fives += 1
            change -= 5
        elif (change - 2) >= 0:
            twos += 1
            change -= 2
        elif (change - 1) >= 0:
            ones += 1
            change -= 1
        elif (change - .5) >= 0:
            half_dollars += 1
            change -= .5
        elif (change - .25) >= 0:
            quarters += 1
            change -= .25
        elif (change - .1) >= 0:
            dimes += 1
            change -= .1
        elif (change - .05) >= 0:
            nickels += 1
            change -= .05
        elif (change - 0.01) >= 0:
            pennies += 1
            change -= .01

    print(f"Your change is: {round(change_hold_value, 2)}\nThat's")     # prints total change
    if twenties > 0:                                                    # if number of denominations is non-zero
        print(twenties, "twenties")                                     # prints the number of each
    if tens > 0:
        print(tens, "tens")
    if fives > 0:
        print(fives, "fives")
    if twos > 0:
        print(twos, "twos")
    if ones > 0:
        print(ones, "ones")
    if half_dollars > 0:
        print(half_dollars, "half dollars")
    if quarters > 0:
        print(quarters, "quarters")
    if dimes > 0:
        print(dimes, "dimes")
    if nickels > 0:
        print(nickels, "nickels")
    if pennies > 0:
        print(pennies, "pennies")
    print(f"That's {round(change_hold_value, 2) * 17.07} pesos!")       # Pesos...because why not


find_change()