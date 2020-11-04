def temp(t):
    if t < -273.15:
        print("Invalid because it is below absolute zero")
    elif t == -273.15:
        print("Absolute Zero!")
    elif t > -273.15 and t < 0:
        print("Below freezing!")
    elif t == 0:
        print("Freezing point!")
    elif t == 100:
        print("Boiling point!")
    elif t > 100:
        print("Above boiling point!")
    else: 
        print("Insufficient Data!")

running = True
while running:
    try:
        cel = float(input("Enter temperature in celcius: "))
        temp(cel)
        running = False
    except ValueError as e:
        print("Invalid temperature!")
        running = True
