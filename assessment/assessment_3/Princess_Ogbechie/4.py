def matches(x,y):
    count = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            count += 1
        else:
            continue
    print("The number of matches from your entered strings is " + str(count))


str1 = str(input("Please enter your first string:\n"))
str2 = str(input("Please enter your second string:\n"))

matches(str1,str2)