def merge():
    list1 = []
    list2 = []
    while True:
        print("Enter values for List 1. (Type . to end list)")
        val1 = input()
        if val1 == ".":
            break
        list1 = list1 + [val1]
        list1.sort()
    while True:
        print("Enter values for List 2. (Type . to end list)")
        val2 = input()
        if val2 == ".":
            break
        list2 = list2 + [val2]
        list2.sort()
    mergeList = list1 + list2
    mergeList.sort(key = str.lower)
    print(mergeList, sep =", ")

merge()
