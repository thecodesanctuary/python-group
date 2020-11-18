#1
integers = input("Enter a list element separated by space ")
list  = integers.split()
print('There are ', len(list), ' numbers in the list')
print('The last number in the list is: ', list[-1])
print(list[::-1])
if 5 in list:
    print("Yes")
else:
    print('No')
count = 0
for i in range(len(list)):
    if list[i] == 5:
        count += 1
print('There are ', count, 'fives(s) in the list')
list.remove(list[0])
list.remove(list[-1])
list.sort()
print(list)
less = 0
for i in range(len(list)):
    if list[i] < 5:
        less += 1
print('There are ', less, 'fives(s) in the list')

#2
import random
import statistics

randomlist = []
for i in range(0,20):
    n = random.randint(1,100)
    randomlist.append(n)
print(randomlist)
print('The mean of the numbers is' round(statistics.mean(randomlist), 2))
randomlist.sort()
print("The largest number in the list is:", randomlist[-1])
print("The smallest number in the list is:", randomlist[0])
print("The second largest number in the list is:", randomlist[-2])
print("The second smallest number in the list is:", randomlist[1])
count = 0
for i in range(len(randomlist)):
    if randomlist[i] % 2 == 0:
        count += 1
print('There are', count, 'even number(s) in the list')

#3
list = [8, 9, 10]
list[1] = 17
list.append(4)
list.append(5)
list.append(6)
list.remove(list[0])
list.sort()
for i in range(len(list)):
    list.append(list[i])
list.insert(3, 25)

list = []
for i in range(0, 50):
    list.append(i)
print(list)
for i in range(0, 51):
    list.append(i * i)
print(list)

#4
import string

test_list = list(string.ascii_lowercase)
for i in range(len(test_list)):
    test_list[i] = test_list[i] * (i+1)
print(test_list)

#5
def summer(L, M):
    N = []
    for i in range(len(L)):
        N.append(L[i] + M[i])
    print(N)


    
