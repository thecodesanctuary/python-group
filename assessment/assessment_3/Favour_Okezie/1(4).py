#integers=list(int(input('Enter a list of integers here:')))
integers=[1,2,3,4,5]

totalno=integers[0]+integers[1]+integers[2]+integers[3]+integers[4]
print('The total number of numbers in the list is: ',totalno)

lastitem=integers[4]
print('The last number on the list is: ',lastitem)

integers.sort(reverse=True)
print('The reverse sorted integers list is: ',integers)

if 5 in integers:
    print('Yes, five is present.')
else:
    print('No, five is not present.')

five_count=integers.count(5)
print('The number of fives present in this list are: ', five_count)

firstitem=integers[0]
integers.remove(firstitem)
print('New integer list is:',integers)

last_item=integers[3]
integers.remove(last_item)
print('New final integer list is: ', integers)

less=0
for i in integers:
    if integers<5:
        less=less+1
        print('The numbers less than 5 are: ',less)






