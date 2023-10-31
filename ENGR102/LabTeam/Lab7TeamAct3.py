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

board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],   # Chess board
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]


def print_board():   # Prints board properly without the ""
    for i in board:
        line = ""
        for j in i:
            line = line + j
        print(line)



while True:
    print('\n*********************************************************************************************************') #Prints Seperation of moves

    print_board()
    initial = input("Enter the position of the piece you want to move using xy notation: ")
    initial_x = int(initial[0]) - 1 # Calculate initial pos
    initial_y = int(initial[1])
    if board[8 - initial_y][initial_x] == ".":
        print("Bad user. Bad. *sprays water bottle*") # if user inputs empty for inital error message
        quit()
    final = input("Enter the target position using xy notation: ")
    final_x = int(final[0]) - 1 #Calculate final pos
    final_y = int(final[1])
    piece = board[8 - initial_y][initial_x]
    board[8 - initial_y][initial_x] = "." #Change initial to .
    board[8 - final_y][final_x] = piece

