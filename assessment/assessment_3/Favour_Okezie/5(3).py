string1=str(input('Input your string here: '))
string2=str(input('Input your 2nd string here: '))

def one_away():
    a=len(string1)
    b=len(string2)

    if a==b:
        print('True')
    if a!=b:
        print('False')

one_away()        
