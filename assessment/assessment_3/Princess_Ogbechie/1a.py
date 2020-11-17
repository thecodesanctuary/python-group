# This is a function called merge that takes 2 already sorted lists of possibly different lengths
# and merges them into a single sorted list using the sort method


def merge(): # defining the function
    list1 = [] #initiate lists
    list2 = []
    while True:
        print("Enter values for List 1. (Type . to end list)")
        val1 = input()
        if val1 == ".": # used to show the end of the list
            break
        list1 = list1 + [val1] # adds new values to the list
        list1.sort() #sorting of the first list
    while True:
        print("Enter values for List 2. (Type . to end list)")
        val2 = input()
        if val2 == ".":
            break
        list2 = list2 + [val2]
        list2.sort()
    mergeList = list1 + list2 # list concatenation
    mergeList.sort(key = str.lower) # sorting of the newly merged list in alpabetical order
    print(mergeList, sep =", ")

merge()
