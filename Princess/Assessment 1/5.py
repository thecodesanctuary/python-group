#A Phone tip calculator

Bill = float(input("How much is the bill? $"))

PTip = float(input("What percent of a tip do you want to leave? "))

tip = round(float((PTip/100)*Bill), 2)
total = round(float(Bill+tip),2)


print(f"\n \nTip = ${tip}")


print(f"\nTotal bill with tip = ${total}")