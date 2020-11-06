#Program to print certain statements depending on the value of the temperature given

temp = float(input("Please enter the temperature: "))

if temp < -273.15:
    print("\nInvalid temperature below Absolute Zero.")
elif temp == -273.15:
    print("\nTemperature is Absolute Zero.")
elif temp > -273.15 and temp < 0 :
    print("\nTemperature is below Freezing point.")
elif temp == 0 :
    print("\nTemperature is at Freezing point")
elif temp > 0 and temp < 100:
    print("\nTemperature is Normal")
elif temp == 100:
    print("\nTemperature is at Boiling point")
elif temp > 100:
    print("\nTemperature is above Boiling point")