'''
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Group Names: Peter, Jared, Quinton, Mrinal
Section: ENGR 102 536
Assignment: Lab6Team
Date: 10/3/23
'''

def find_risk():
    sum_points = 0                                                                      # initialize sum_points
    gender = input("Are you male or female? Enter 'm' or 'f': ")                        # input for gender
    if not (gender == 'm' or gender == 'f'):
        print("Not a valid gender!")
        quit()

    age = 0                                                                             # input for age
    while not(20 <= age <= 79):
        try:
            age = float(input("This quiz is for ages 20 to 79. Enter your age: "))
        except ValueError:
            print("Not a valid age!")
            quit()

    cholesterol = input("What is your Cholesterol Level? ")                             # input for cholesterol
    try:
        cholesterol = int(cholesterol)
    except ValueError:
        print("Not a valid Cholesterol level!")
        quit()

    smoker = input("Do you smoke? Enter 'y' or 'n': ")                                  # input for smoker/non
    if smoker == 'y':
        smoker = True
    elif smoker == 'n':
        smoker = False
    else:
        print("Not a valid Smoker response!")
        quit()

    hdl = input("What is your HDL level? ")                                             # input for HDL
    try:
        hdl = int(hdl)
    except ValueError:
        print("Not a valid HDL Level!")
        quit()

    bp = int(input("What is your Blood Pressure level? "))                              # input for BP
    try:
        bp = int(bp)
    except ValueError:
        print("Not a valid Blood Pressure!")
        quit()

    treated = input("Are you being treated for Blood Pressure? Enter 'y' or 'n': ")     # input for bp treatment
    if treated == 'y':
        treated = True
    elif treated == 'n':
        treated = False
    else:
        print("Not a valid level of Treatment!")
        quit()
    hypochondria = input("Are you a hypochondriac? Enter 'y' or 'n': ")                 # probably nothing to
                                                                                        # worry about

    if gender == 'm':                       # age, cholesterol, and smoker point values for male
        if 34 >= age >= 20:
            sum_points -= 9
            if smoker:
                sum_points += 8
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 4
            elif 200 <= cholesterol <= 239:
                sum_points += 7
            elif 240 <= cholesterol <= 270:
                sum_points += 9
            elif 280 <= cholesterol:
                sum_points += 11
        elif 39 >= age >= 35:
            sum_points -= 4
            if smoker:
                sum_points += 8
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 4
            elif 200 <= cholesterol <= 239:
                sum_points += 7
            elif 240 <= cholesterol <= 270:
                sum_points += 9
            elif 280 <= cholesterol:
                sum_points += 11
        elif 44 >= age >= 40:
            sum_points += 0
            if smoker:
                sum_points += 5
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 3
            elif 200 <= cholesterol <= 239:
                sum_points += 5
            elif 240 <= cholesterol <= 270:
                sum_points += 6
            elif 280 <= cholesterol:
                sum_points += 8
        elif 49 >= age >= 45:
            sum_points += 3
            if smoker:
                sum_points += 5
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 3
            elif 200 <= cholesterol <= 239:
                sum_points += 5
            elif 240 <= cholesterol <= 270:
                sum_points += 6
            elif 280 <= cholesterol:
                sum_points += 8
        elif 54 >= age >= 50:
            sum_points += 6
            if smoker:
                sum_points += 3
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 2
            elif 200 <= cholesterol <= 239:
                sum_points += 3
            elif 240 <= cholesterol <= 270:
                sum_points += 4
            elif 280 <= cholesterol:
                sum_points += 5
        elif 59 >= age >= 55:
            sum_points += 8
            if smoker:
                sum_points += 3
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 2
            elif 200 <= cholesterol <= 239:
                sum_points += 3
            elif 240 <= cholesterol <= 270:
                sum_points += 4
            elif 280 <= cholesterol:
                sum_points += 5
        elif 64 >= age >= 60:
            sum_points += 10
            if smoker:
                sum_points += 1
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 1
            elif 200 <= cholesterol <= 239:
                sum_points += 1
            elif 240 <= cholesterol <= 270:
                sum_points += 2
            elif 280 <= cholesterol:
                sum_points += 3
        elif 69 >= age >= 65:
            sum_points += 11
            if smoker:
                sum_points += 1
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 1
            elif 200 <= cholesterol <= 239:
                sum_points += 1
            elif 240 <= cholesterol <= 270:
                sum_points += 2
            elif 280 <= cholesterol:
                sum_points += 3
        elif 74 >= age >= 70:
            sum_points += 12
            if smoker:
                sum_points += 1
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 0
            elif 200 <= cholesterol <= 239:
                sum_points += 0
            elif 240 <= cholesterol <= 270:
                sum_points += 1
            elif 280 <= cholesterol:
                sum_points += 1
        elif 79 >= age >= 75:
            sum_points += 13
            if smoker:
                sum_points += 1
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 0
            elif 200 <= cholesterol <= 239:
                sum_points += 0
            elif 240 <= cholesterol <= 270:
                sum_points += 1
            elif 280 <= cholesterol:
                sum_points += 1

        if bp < 120:                        # blood pressure point values for males (includes treatment point values)
            sum_points += 0
        elif 120 <= bp < 130:
            if treated:
                sum_points += 1
            elif not treated:
                sum_points += 0
        elif 130 <= bp < 160:
            if treated:
                sum_points += 2
            elif not treated:
                sum_points += 1
        elif 160 <= bp:
            if treated:
                sum_points += 3
            elif not treated:
                sum_points += 2

    elif gender == 'f':                     # age, cholesterol and smoker point values for female
        if 34 >= age >= 20:
            sum_points -= 7
            if smoker:
                sum_points += 9
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 4
            elif 200 <= cholesterol <= 239:
                sum_points += 8
            elif 240 <= cholesterol <= 270:
                sum_points += 11
            elif 280 <= cholesterol:
                sum_points += 13
        elif 39 >= age >= 35:
            sum_points -= 3
            if smoker:
                sum_points += 9
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 4
            elif 200 <= cholesterol <= 239:
                sum_points += 8
            elif 240 <= cholesterol <= 270:
                sum_points += 11
            elif 280 <= cholesterol:
                sum_points += 13
        elif 44 >= age >= 40:
            sum_points += 0
            if smoker:
                sum_points += 7
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 3
            elif 200 <= cholesterol <= 239:
                sum_points += 6
            elif 240 <= cholesterol <= 270:
                sum_points += 8
            elif 280 <= cholesterol:
                sum_points += 10
        elif 49 >= age >= 45:
            sum_points += 3
            if smoker:
                sum_points += 7
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 3
            elif 200 <= cholesterol <= 239:
                sum_points += 6
            elif 240 <= cholesterol <= 270:
                sum_points += 8
            elif 280 <= cholesterol:
                sum_points += 10
        elif 54 >= age >= 50:
            sum_points += 6
            if smoker:
                sum_points += 4
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 2
            elif 200 <= cholesterol <= 239:
                sum_points += 4
            elif 240 <= cholesterol <= 270:
                sum_points += 5
            elif 280 <= cholesterol:
                sum_points += 7
        elif 59 >= age >= 55:
            sum_points += 8
            if smoker:
                sum_points += 4
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 2
            elif 200 <= cholesterol <= 239:
                sum_points += 4
            elif 240 <= cholesterol <= 270:
                sum_points += 5
            elif 280 <= cholesterol:
                sum_points += 7
        elif 64 >= age >= 60:
            sum_points += 10
            if smoker:
                sum_points += 2
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 1
            elif 200 <= cholesterol <= 239:
                sum_points += 2
            elif 240 <= cholesterol <= 270:
                sum_points += 3
            elif 280 <= cholesterol:
                sum_points += 4
        elif 69 >= age >= 65:
            sum_points += 12
            if smoker:
                sum_points += 2
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 1
            elif 200 <= cholesterol <= 239:
                sum_points += 2
            elif 240 <= cholesterol <= 270:
                sum_points += 3
            elif 280 <= cholesterol:
                sum_points += 4
        elif 74 >= age >= 70:
            sum_points += 14
            if smoker:
                sum_points += 1
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 1
            elif 200 <= cholesterol <= 239:
                sum_points += 1
            elif 240 <= cholesterol <= 270:
                sum_points += 2
            elif 280 <= cholesterol:
                sum_points += 2
        elif 79 >= age >= 75:
            sum_points += 16
            if smoker:
                sum_points += 1
            if cholesterol <= 160:
                sum_points += 0
            elif 160 <= cholesterol <= 199:
                sum_points += 1
            elif 200 <= cholesterol <= 239:
                sum_points += 1
            elif 240 <= cholesterol <= 270:
                sum_points += 2
            elif 280 <= cholesterol:
                sum_points += 2

        if bp < 120:                        # BP points for females (includes treatment points)
            sum_points += 0
        elif 120 <= bp < 130:
            if treated:
                sum_points += 3
            elif not treated:
                sum_points += 1
        elif 130 <= bp < 140:
            if treated:
                sum_points += 4
            elif not treated:
                sum_points += 2
        elif 140 <= bp < 160:
            if treated:
                sum_points += 5
            elif not treated:
                sum_points += 3
        elif 160 <= bp:
            if treated:
                sum_points += 6
            elif not treated:
                sum_points += 4

    if hdl >= 60:                           # HDL point values
        sum_points += -1
    elif 50 <= hdl < 60:
        sum_points += 0
    elif 40 <= hdl < 50:
        sum_points += 1
    elif 0 <= hdl < 40:
        sum_points += 2


    # TOTAL POINTS IF MALE
    if gender == 'm':
        if sum_points < 0:
            print(f'10-Year risk is less than 1%')
        elif 0 <= sum_points <= 4:
            print(f'10-Year risk is 1%')
        elif 5 < sum_points < 6:
            print(f'10-Year risk is 2%')
        elif sum_points == 7:
            print(f'10-Year risk is 3%')
        elif sum_points == 8:
            print(f'10-Year risk is 4%')
        elif sum_points == 9:
            print(f'10-Year risk is 5%')
        elif sum_points == 11:
            print(f'10-Year risk is 8%')
        elif sum_points == 12:
            print(f'10-Year risk is 10%')
        elif sum_points == 13:
            print(f'10-Year risk is 12%')
        elif sum_points == 14:
            print(f'10-Year risk is 16%')
        elif sum_points == 15:
            print(f'10-Year risk is 20%')
        elif sum_points == 16:
            print(f'10-Year risk is 25%')
        elif sum_points >= 17:
            print(f'10-Year risk is greater than or equal to 30%')

    # TOTAL POINTS IF FEMALE
    if gender == 'f':
        if sum_points < 9:
            print(f'10-Year risk is less than 1%')
        elif 9 <= sum_points <= 12:
            print(f'10-Year risk is 1%')
        elif 13 <= sum_points <= 14:
            print(f'10-Year risk is 2%')
        elif sum_points == 15:
            print(f'10-Year risk is 3%')
        elif sum_points == 16:
            print(f'10-Year risk is 4%')
        elif sum_points == 17:
            print(f'10-Year risk is 5%')
        elif sum_points == 18:
            print(f'10-Year risk is 6%')
        elif sum_points == 19:
            print(f'10-Year risk is 8%')
        elif sum_points == 20:
            print(f'10-Year risk is 11%')
        elif sum_points == 21:
            print(f'10-Year risk is 14%')
        elif sum_points == 22:
            print(f'10-Year risk is 17%')
        elif sum_points == 23:
            print(f'10-Year risk is 22%')
        elif sum_points == 24:
            print(f'10-Year risk is 27%')
        elif sum_points >= 25:
            print(f'10-Year risk is greater than or equal to 30%')


find_risk()                                     # runs the code
