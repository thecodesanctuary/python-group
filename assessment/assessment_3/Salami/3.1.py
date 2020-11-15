one = ['a', 'b', 'c', 'x', 'y', 'z']
two = ['d', 'e', 'f', 'w']
three = [5,9,11]
four = [3,7,13,22]

def mergeSort(x, y):
    mergeSort = x + y
    mergeSort.sort()
    print(mergeSort)

def merge(x, y):
    merge = x + y
    for i in range(0,len(merge)):
        for j in range(i + 1, len(merge)):
            if merge[i] > merge [j]:
                merge[i],merge[j] = merge[j],merge[i]
            else:
                pass

    print(merge)


mergeSort(one, two)
merge(three, four)
