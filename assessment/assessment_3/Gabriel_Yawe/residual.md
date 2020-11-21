
if str_1[0:len(str_1)]==str_2[0:len(str_2)]:
            print("This is a maatch")
    else:
        print("This is not a match")

matches("yawe","jam")


def matches(str_1,str_2):
    match=0
    for i in range(0,len(str_1)):
        if str_1[i] in str_2:
            match=match+1
        #if str_1[1]==str_2[1]:
            print("This is a maatch")
    else:
        pass
        #print("This is not a match")
        return match

matches("yawe","yam")


""" def contains_a_letter(s):
    for c in s:
        if c in s:
            return True
        return False
print(contains_a_letter("12abc"))
contains_a_letter("@341&&") """