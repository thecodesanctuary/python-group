user_list = eval(input("Enter a list in the format [integer, integer,...]: "))




print(user_list)
print(user_list[-1])
user_list.reverse()
print(user_list)
if 5 in user_list:
    print("Yes")
else:
    print("No")
# count = 0
# for i in range(0, len(user_list)):
#     if user_list[i] == 5:
#         count = count + 1
#     else:
#         pass
# print(count)
print(user_list.count(5))
del user_list[0]
del user_list[-1]
user_list.sort()
print(user_list)
count_two = 0
for i in range(0, len(user_list)):
    if user_list[i] < 5:
        count_two = count_two + 1
    else:
        pass
print(count_two)

