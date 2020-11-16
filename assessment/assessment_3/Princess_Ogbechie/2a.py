import itertools

def primes(n): 
    primeN = []
    time = 0
    for ANum in itertools.count(2,1):
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
    primes(int(input("Enter a number: ")))
except ValueError :
    primes(100)
