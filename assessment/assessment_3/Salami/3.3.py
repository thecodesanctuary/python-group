name = "SaLaMi"

def change_case(x):
    y = ""
    for i in range(0, len(x)):
        if x[i] == x[i].upper():
            y = y + x[i].lower()
        else:
            y = y + x[i].upper()
    print(y)
    
def change_case_two(x):
    x = x.swapcase()
    print(x)

change_case(name)
change_case_two(name)

