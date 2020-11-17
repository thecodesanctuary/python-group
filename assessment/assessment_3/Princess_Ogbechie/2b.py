# This is the modified primes function that allows the user enter what number the primes should start from and how many the user wants

import itertools

def primes(start, n): # uses 2 arguments to indicate start point and the number of primes
    primeN = []
    time = 0
    for ANum in itertools.count(start,1):   #itertools.count is used to count to infinity while the numbers are used by ANum to be divided by Num to find out if ANum can be divided by any number in between.
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
    x = int(input("Enter your first number. ")) # This value indicates the start point for the prime numbers
    y = int(input("Enter number of primes you want. ")) # this is the number of the primes the user wants
    primes(x, y) 
except ValueError :     # uses a default value of the first 100 prime numbers if no value is given
    primes(2,100)
