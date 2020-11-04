def leap(year):
    r = 1600
    total = 0
    while r <= year:
        if r%4 == 0 and r%100 != 0:
            print(r)
            total = total + 1
            r = r + 1
        elif r%400 == 0:
            print(r)
            total = total + 1
            r = r + 1
        else:
            r = r + 1
    print(f"There are a total of {total} leap years betweeen 1600 and {year}")
    

running = True
while running:
    try:
        y = int(input("Show leap years between 1600 and ?... "))
        if y < 0:
            print("Please enter a valid year!")
            running = True
        elif y <= 1600:
            print("Insufficient data! Please enter a year not less than 1600")
        else:
            leap(y)
            running =False
    except ValueError as e:
        print("Please enter a valid year!")
        running = True