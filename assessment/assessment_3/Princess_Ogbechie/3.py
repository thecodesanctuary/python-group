def change_case(test):

    for char in test:
        if char.isupper():
            print(char.lower(), end = "")
        if char.islower():
            print(char.upper(), end = "")
        if char == " ":
            print(" ", end = "")

change_case(input("Enter your desired string: \n"))