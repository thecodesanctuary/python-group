def convert(n):
    minutes = n//60
    seconds = n%60
    if minutes == 1:
        print(f'\n{n} seconds equals {minutes} minute and {seconds} seconds\n')
    elif seconds == 1:
        print(f'\n{n} seconds equals {minutes} minutes and {seconds} second\n')
    elif minutes and seconds == 1:
        print(f'\n{n} seconds equals {minutes} minute and {seconds} second\n')
    else:
        print(f'\n{n} seconds equals {minutes} minutes and {seconds} seconds\n') 
#lol I know, english teacher levels

running = True
while running:
    try:
        time = float(input("Please enter time in seconds: "))
        if time < 0:
            print("Please type a valid time period in seconds \n")
            running = True
        else:
            convert(time)
            running = False
    except ValueError as e:
        print("Na ment fr fr lmao")
        print("Please type a valid time period in seconds \n")
        running = True
