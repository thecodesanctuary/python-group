# This program generates a list of 20 random numbers betweeen 1 and 100 and carries out some instructions on it.

import random   # imports module that calls random integers
import statistics   # imports module that calls mean

ranNum = []

for i in range(20):
    ranNum.append(random.randint(1,100))

print(ranNum)   # print the list

print("\nThe average of the elements in the list above is ", round(statistics.mean(ranNum),2))  # Prints the average of all elements on the list

print(f"\nThe largest value on the list is {max(ranNum)}.\nThe smallest value on the list is {min(ranNum)}.") # Prints largest and smallest values on the list

ranNum.sort()       # sorts the list

print(f"\nThe second largest value on the list is {ranNum[-2]}.\nThe second smallest value on the list is {ranNum[1]}")     # Prints second largest value on the list and the second smallest value on the list based on their positions in the now sorted list

count = 0
for i in range(len(ranNum)-1):
    if ranNum[i] % 2 == 0 :     # Checks for even numbers
        count += 1      # counts the even numbers in the list
    else :
        continue
print(f"\nThere are {count} even numbers in the list.")