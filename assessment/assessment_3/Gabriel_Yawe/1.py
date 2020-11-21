
uno=[5,3,7]
duo=[1,22,25]

def merge():
    merge=uno+duo
    merge.sort()
    print(merge)

merge()

""" one=["a","b","c"]
two=["d","e","f"]
#three=[1,4,3,7]
#four=[9,5,6,4]

def mergeSort(x,y):
    mergeSort = x+y
    mergeSort.sort()
    print(mergeSort) """

""" def merge(x,y):
    merge =x+y
    for i in range(0,len(merge)):
        for j in range (i+i, len(merge)):
            if merge[i]>merge[j]:
                merge[i],merge[j]=merge[j],merge[i]
    print(merge) """

#mergeSort(one,two)