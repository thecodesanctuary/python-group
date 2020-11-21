import random
import math
""" for i in range(100):
    list_1=[random.randint(0,100)]
    total=0 
    for element in (list_1):
        total= total + list_1[element]
        while (element<len(list_1)):
            total=total+list_1[element]
        elements+1 
        total= sum(list_1)
    print(total)

    res=sum([random.randrange(1,100)]) #for i in range (100)])
    print (res) """
res = sum(random.sample(range(0,100),5))
