print('How much is the bill?')
bill = float(input())
print('How much tip do you want to give')
Tip = float(input())
TipAmt = bill * Tip / 100
print('Tip: ' + str(int(TipAmt)))
Total = int(bill) + int(TipAmt)
print('Total amount paid: ' + str(int(Total)))