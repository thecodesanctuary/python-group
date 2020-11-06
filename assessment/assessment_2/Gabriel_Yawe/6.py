temperature= float(input("Please Enter a Teperature Value in Celsius:"))
if(temperature < -273.15):
    print("Invalid temperature. Value is below absolute zero.")
elif (temperature == -273.15):
    print("Temperature is absolute 0 celsius")
elif (temperature > -273.15 and temperature < 0.0):
    print("Temperature is below freezing Point")
elif (temperature == 0.0):
    print("Temperature is at freezing point")
elif (temperature >0.0 and temperature <100.0):
    print("Temperature is in normal Range")
elif (temperature ==100.0):
    print("Temperatue is at the boiling point")
elif (temperature >100.0):
    print("Temperature is above boiling point")

