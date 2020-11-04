#program to print fibonacci numbers

i, j, inc = 0, 1, 0


Num = int(input("How many numbers in Fibonacci sequence to print? "))

if Num <= 0:
    print("Unable to display less than 1")
elif Num == 1:
    print(j)
else:
    while inc < Num:
        print(j)
        x = i + j
        i = j
        j = x
        inc = inc + 1