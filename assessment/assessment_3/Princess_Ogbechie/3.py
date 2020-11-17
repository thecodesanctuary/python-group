# This is a function that given a string
# it returns a string with each uppercasse letter replaced by a lowercase letter and a lowercase letter replaced by an uppercase letter

def change_case(test):

    for char in test: # Checks each character in the inputted string

        if char.isupper(): # checks for uppercase letters
            print(char.lower(), end = "") # switches to lowercase letter
        
        if char.islower(): # checks for lowercase letters
            print(char.upper(), end = "") # switches to uppercase letter
        
        if char == " ": # leaves spaces where there are spaces
            print(" ", end = "")

change_case(input("Enter your desired string: \n"))