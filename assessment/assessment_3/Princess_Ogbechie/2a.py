# This is a function called primes that is given a number n and returns a list of the first n primes


import itertools # itertools module allows the use of .count function

def primes(n): # function definition

    primeN = [] # initialize Prime number list
    time = 0 # time here is used as a counter
    
    for ANum in itertools.count(2,1): # itertools.count is used instead of range as there is no definite range till the counter is finished. It counts infinitely beginning from 2 in steos of 1
        Prime = True 

        for num in range (2,ANum):
            if ANum % num == 0: # if a number is perfectly divisible by other numbers except itself and 1
                Prime = False # it is not prime
        
        if Prime: 
            primeN.append(ANum) # this adds the prime number to the list
            time += 1
        
        if time == n : 
            break
    print(primeN) # prints the list of n prime numbers

try:
    primes(int(input("Enter a number: ")))
except ValueError : # if no value is entered, the function has a default value for the first 100 prime numbers.
    primes(100)
