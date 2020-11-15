a = "bike"
b = "hike"

def one_away(x,y):
    check = 0
    i = 0
    if len(x) == len(y):
        while i < len(x):
            if x[i].lower() == y[i].lower():
                i = i + 1
            else:
                i = i + 1
                check = check + 1
        if check == 1:
            print("True")
    else:
        print("False")

one_away(a,b)