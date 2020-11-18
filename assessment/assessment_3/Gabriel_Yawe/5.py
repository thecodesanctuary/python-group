""" def one_away(str_1,str_2):
    if len(str_1) == len(str_2):
        print("True")

    else:
        print (str_1," and " ,str_2 ," don't have the same number of characters")

one_away("Yawe","Gabriel") """


def one_away(str_1,str_2):
    matches =0
    if str_1[0:len(str_1)]==str_2[0:len(str_2)]:
        print("This is a match")
        matches +=1
    else:
        print("This is not a match")
print ("There are",matches,"in the strings")
one_away("Jam","Jam")