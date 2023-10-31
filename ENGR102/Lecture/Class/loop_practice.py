print("guess number")
num = 7
user_guess = int(input("enter guess from 1-10: "))
count = 0
while user_guess != num:
    print("You wrong boi!")
    count +=1
    user_guess = int(input("enter anotha guess from 1 - 10: "))
print("you guessed correct in ", count+1, " tries")