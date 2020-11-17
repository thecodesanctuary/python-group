# This is a function called matches that takes two strings as arguments and returns
# how many matches there are between the strings. 

# A match is where the two strings have the same character at the same index.

def matches(x,y): 
    count = 0  # initiates count
    for i in range(len(x)) :  # counts the length of the string and compares to the other
        if x[i] == y[i] :
            count += 1
        else :
            continue
    print("The number of matches from your entered strings is " + str(count))


str1 = str(input("Please enter your first string:\n"))
str2 = str(input("Please enter your second string:\n"))

matches(str1,str2)