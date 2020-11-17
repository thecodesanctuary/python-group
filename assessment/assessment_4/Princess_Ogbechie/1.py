# This program asks the user to enter a list of integers and carries our some commands on them.

line = []

while True :
    try :   # Makes sure that only intergers are entered.
        number = int(input("Enter a number: "))
        line += [number]
    except ValueError:      #if anything other than an integer is entered, the list ends.
        break
    

print("\nThe total number of items in the list is ", len(line))   # Tells user the total number of items in the list
print("\nThe last item in the list is ", line[len(line)-1])     # Tells user the last item in the list
line.reverse()
print("\nThis is the list in reverse order \n", line)   # Prints the lists in the reverse order

if 5 in line:   # checks if the list contains a 5
    print("\nYes, there is a 5 in the list.")   
else:
    print("\nNo, there is no 5 in the list.")

count = 0
for i in range(len(line)):  # Tells user the number of 5's in the list
    if line[i] == 5 :
        count += 1
print ("\nThe number of 5's in the list is ", count)

line.remove(line[0])    # removes the first item from the list
line.remove(line[len(line)-1])  #removes the last item from the ist

line.sort()     # sorts the remaining items in the list
print("\nThis is the newly sorted list without the first and the last items\n", line)   # Print new list

less = 0
for i in range(len(line)):
    if line[i] < 5 :    # prints the number of integers on list that are less than 5
        less += 1
print ("\nThe number of integers in the list less than 5 are ", less)
    