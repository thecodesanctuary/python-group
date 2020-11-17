# This function is that takes two strings and returns True if the strings are of the same length and differ in exactly one letter.

def one_away(x,y):
    count = 0 # initialize counter
    for i in range(len(x)): # checks and compares letters in both strings
        if x[i] != y[i]:
            count += 1
        else:
            continue
    if len(x) == len(y) and count == 1: # conditional comparison statement
        print("\nTrue")
    else :
        print("More than 1 letter differs.")


m = input("First string:\n")
n = input("Second string:\n")

one_away(m,n)