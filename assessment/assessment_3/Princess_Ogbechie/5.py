def one_away(x,y):
    count = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
        else:
            continue
    if len(x) == len(y) and count == 1:
        print("\nTrue")
    else:
        print("More than 1 letter differs.")


m = input("First string:\n")
n = input("Second string:\n")

one_away(m,n)