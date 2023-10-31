"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish
Group Names: Jared, Anish, Quinton, Mrinal, Peter
Section: ENGR 102 536
Assignment: Lab7IndieAct3
Date: 10/24/23
"""

num_widgets = []
while not ((value := int(input("Enter the number of widgets made. Enter a negative value when done. "))) <= 0):
    num_widgets.append(value)
num_days = len(num_widgets)


jump_lengths = []
for i in range(num_days - 1):
    jump_lengths.append(i + 1)
# print(jump_lengths)

differences = []
count = 0
for i in jump_lengths:
    differences.append([])
    for j in range(num_days):
        try:
            differences[count].append(num_widgets[j + i] - num_widgets[j])
        except IndexError:
            pass
    count += 1

# print(differences)

count = 0
for i in differences:
    num_values = len(i)
    num_pos = 0
    num_neg = 0
    for j in i:
        if j > 0:
            num_pos += 1
        elif j < 0:
            num_neg += 1
    pos_percent = round(((num_pos / num_values) * 100), 1)
    neg_percent = round(((num_neg / num_values) * 100), 1)
    print(f"For {jump_lengths[count]}-day intervals, {pos_percent} were increasing and {neg_percent} were decreasing.")
    count += 1
