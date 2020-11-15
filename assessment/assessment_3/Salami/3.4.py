a = "python"
b = "path"

def matches(x,y):
    x, y = x.lower(), y.lower()
    i = 0
    match = 0
    if len(x) > len(y):
        while i < len(y):
            if x[i] == y[i]:
                match = match + 1
                i = i + 1
            else:
                i = i + 1
    else:
        while i < len(x):
            if x[i] == y[i]:
                match = match + 1
                i = i + 1
            else:
                i = i + 1

    print(match)

matches(a,b)
