import random

list1=random.sample(range(1,100),20)
print('The random list is: ',list1)

average=sum(list1)/len(list1)
print('The average of the list is: ',average)

max_no=max(list1)
print('The largest number in this random list is: ', max_no)

min_no=min(list1)
print('The smallest number in this random list is: ', min_no)

list1.remove(max_no)
max_no1=max(list1)
print('The second largest number in this random list is: ', max_no1)

list1.remove(min_no)
min_no1=min(list1)
print('The second smallest number in this random list is: ', min_no1)

even_no=0
for i in list1:
    if i%2==0:
        even_no=even_no+1
print('The number of even numbers in list1 is: ',even_no)