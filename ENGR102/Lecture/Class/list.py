grades = [87, 93, 75, 100, 82, 91, 85]
sum = 0
for i in range (len(grades)):
    sum += grades[i]
average = sum/len(grades)
print(average)