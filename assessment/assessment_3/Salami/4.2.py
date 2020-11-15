from random import randint

my_list = []
for i in range(20):
    my_list.append(randint(1,100))
print(my_list)
print(sum(my_list)/len(my_list)) #average
my_list.sort()
print(f"{my_list[-1]} and {my_list[0]}") #largest and smallest
print(f"{my_list[-2]} and {my_list[1]}") 

even = 0 #even
for i in range(0, len(my_list)):
    if my_list[i]%2 == 0:
        even = even + 1
print(even)