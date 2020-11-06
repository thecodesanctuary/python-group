def level(credits):
    if credits <= 23:
        print("Freshman!")
    elif credits > 23 and credits < 54:
        print("Sophomore!")
    elif credits > 54 and credits < 84:
        print("Junior!")
    elif credits > 84:
        print("Senior!")
    else:
        print("Omo you no be student lmao!")

running = True
while running:
    try:
        c = int(input("How many credits have you taken? "))
        if c <= 0:
            print("you dy whine me?")
            print("Enter valid number of credits")
            running = True
        else:
            level(c)
            running = False
    except ValueError as e:
        print("you dy whine me?")
        print("Enter valid number of credits")
        running = True