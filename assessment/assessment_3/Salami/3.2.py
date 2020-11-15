def primes(n = 100, start = 2):
    prime = []
    while n != 0:
        for i in range(2,start):
            if start%i == 0:
                break
        else:
            prime.append(start)
            n = n - 1
        start = start + 1
    print(prime)


primes(6)
