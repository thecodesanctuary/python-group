# This program uses a for loop to print a list containing the squares of integers 1 through 50

sqrList = []

for i in range (1,51):
    sqrList += [i ** 2]

print(sqrList)