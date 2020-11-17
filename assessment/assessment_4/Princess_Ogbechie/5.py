# This is a program that takes any 2 lists L and M of the same size and adds their elements to form list N
# Elements of list N are the sum of corresponding elements of L and M

size = int(input("Enter the size of the lists. "))
print()

count1 = 0 # initiaize variables and lists
count2 = 0
L = []
M = []
N = []

while True:
    Num = int(input("Enter the values for list 1:   ")) # User entering values
    L.append(Num)  #List concatenation
    count1 += 1
    if size == count1 :
        print("\n")
        break

while True:
    Mum = int(input("Enter the values for list 2:   "))
    M.append(Mum)
    count2 += 1
    if size == count2 :
        print("\n\n")
        break

for i in range(size):
    sum = L[i] + M[i]   # adding values of corresponding elements
    N += [sum]

print("The new list is ", N)