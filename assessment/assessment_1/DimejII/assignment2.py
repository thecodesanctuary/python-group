#this program asks for degrees in Cesius and converts it to Farenheit
print("Kindy enter temperature in Farenheit")
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))