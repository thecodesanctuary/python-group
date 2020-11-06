for i in range(8, 90, 3):
    print(i)

for i in range(100, 0, -2):
    print(i)


nterms = int(input("How many terms? "))
n1, n2 = 1, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

height = int(input("Enter height of triangle: "))
for i in range(0, height): 
        for j in range(0, i+1): 
            print("* ",end="") 
        print("\r") 

seconds = int(input("Enter number of seconds: "))
minutes = seconds // 60
remSeconds = seconds % 60
print(seconds, ' seconds is ', minutes, ' minutes and ', remSeconds, 'seconds.')

year = int(input('Enter a year of your choice:'))
leapYear = 0
for i in range(1600, year):
    if i % 100 == 0:
        leapYear = leapYear + 0
    elif i % 4 == 0 or i % 4 == 0:
        leapYear = leapYear + 1
        print(i, leapYear)
print('There are {leapYear} leap years between 1600 and {year}'.format(leapYear=leapYear, year=year))
    


temp = float(input("Enter temperature in Celsius: "))
if temp < -273.15:
    print('The temperature is invalid because it is below absolute zero.')
elif temp == -273.15:
    print('The temperature is absolute 0.')
elif -273.15 <= temp <= 0:
    print('The temperature is below freezing.')
elif temp == 0:
    print('The temperature is at the freezing point.')
elif 0 <= temp <= 100:
    print('The temperature is in the normal range.')
elif temp == 100:
    print('The temperature is at the boiling point.')
else:
    print('The temperature is above the boiling point.')

credit = int(input('Enter how many credits you have taken: '))
if credit <= 23:
    print('You are a freshman.')
elif 24 <= credit <= 53:
    print('You are a sophmore.')
elif 54 <= credit <= 83:
    print('You are a junior.')
else:
    print('You are a senior.')

from random import randint
for num in range(10):
    value1 = randint(0, 10)
    value2 = randint(0, 10)
    result = value1 * value2
    answer = int(input("Question {num}: {value1} X {value2} = ".format(num=num+1,value1=value1, value2=value2)))
    if answer == result:
        print('Right!')
    else:
        print('Wrong!')