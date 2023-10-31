"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Section: ENGR 102 536
Assignment: Lab7Indie_3
Date: 10-27-23
"""

#Password Protection
def password_protection():
    # Reading the number of username/password pairs
    num_of_users = int(input("Enter the number of users: "))
    
    # Reading usernames and passwords and putting them in a dictionary
    user_data = {}
    for _ in range(num_of_users):
        username = input("Enter username: ")
        
        # Check if username already exists
        while username in user_data:
            print("Username already exists. Please enter a different username.")
            username = input("Enter username: ")
            
        password = input("Enter password: ")
        user_data[username] = password
    
    # user typing in usernames and passwords
    while True:
        entered_username = input("Enter username to login: ")
        entered_password = input("Enter password: ")
        
        # Checking if the entered username and password are correct
        if user_data.get(entered_username) == entered_password:
            print("You are allowed into the system.")
        else:
            print("Incorrect username/password. Please try again.")

# Calling the function to run the program
password_protection()

