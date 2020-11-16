import itertools

def primes(start, n): 
    primeN = []
    time = 0
    for ANum in itertools.count(start,1):
        Prime = True
        for num in range (2,ANum):
            if ANum % num == 0:
                Prime = False
        if Prime:
            primeN.append(ANum)
            time += 1
        if time == n :
            break
    print(primeN)

try:
    x = int(input("Enter your first number. "))
    y = int(input("Enter number of primes you want. "))
    primes(x, y)
except ValueError :
    primes(2,100)
