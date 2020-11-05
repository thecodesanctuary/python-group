mealprice=float(input('How much is your meal sir/ma? '))
tip_percent=int(input('What percentage of tip would you like to give sir/ma? '))
tip=(tip_percent/100)*mealprice
print ('Tip is: ', tip)
Total_amount=tip+mealprice
print('Your total cost is: ', Total_amount)