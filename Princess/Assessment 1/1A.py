#This program converts temperature from Fahrehnheit to Celsius

print('Conversion from Fahrenheit to Celsius \n')


Fahrehn=int(input('Enter the temperature in Fahrehnheit: '))

Cel=round((Fahrehn-32)* 5/9, 2)

print('\n The temperature in Celsius is ', Cel)