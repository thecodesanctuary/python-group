temp=float(input('Enter your temperature in celsius:'))
if temp<-273.15:
    print('This temperature is invalid as it is below absolute zero.')
if temp==-273.15:
    print('This temperature is absolute 0.')
if temp>-273.15 and temp<=0:
    print('This temperature is below freezing.')
if temp==0:
    print('The temperature is at the freezing point.')
if temp>=0 and temp<=100:
    print('The temperature is in the normal range.')
if temp==100:
    print('This temperature is at the boiling point.')
if temp>100:
    print('This temperature is above the boiling point.')