# 1
#With sort method
def sortArray(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3
#Without sort method
def mergeArrays(list1, list2):
    n1 = len(list1)
    n2 = len(list2)
    list3 = [None] * (n1 + n2) 
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2: 
       if list1[i] < list2[j]: 
            list3[k] = list1[i] 
            k = k + 1
            i = i + 1
        else: 
            list3[k] = list2[j] 
            k = k + 1
            j = j + 1
    while i < n1: 
        list3[k] = list1[i]; 
        k = k + 1
        i = i + 1
    while j < n2: 
        list3[k] = list2[j]; 
        k = k + 1
        j = j + 1
    print("Array after merging") 
    for i in range(n1 + n2): 
        print(str(list3[i]), end=" ")
        
# 2a
def primes(n):
    n = int(input("First N prime number, N ? "))
    p = [2]
    c = 2
    while len(p) < n:
        j = 0
        c += 1
        while j < len(p):
            if c % p[j] == 0:
                break
            elif j == len(p) - 1:
                p.append(c)
            j += 1
    return p

#2b
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

def chosenPrimes(n):
    n = int(input("First N prime number, N ? "))
    start = int(input("First, start? "))
    p = []
    c = start
    while len(p) < n:
        if isPrime(c):
            p.append(c)
            c += 1

    return p
#3 
def change_case(str):
    len1 = len(str)
    newStr = ''
    for i in range(len1):
        if str[i].islower() == True:
            newStr += str[i].upper()
        else:
            newStr += str[i].lower()
    return newStr
        


#4
def matches(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    count = 0
    if len1 < len2:
        len3 = len1
    else:
        len3 = len2
    for i in range(len3):
        if str1[i] == str2[i]:
            count += 1
    return count

#5
def one_way(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    count = 0
    if len1 != len2:
        return False
    for i in range(len1):
        if str1[i] != str2[i]:
            count += 1
    if count == 1:
        return True
        