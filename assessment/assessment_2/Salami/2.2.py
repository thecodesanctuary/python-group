def fib(n):
    x,y = 1,1
    for i in range(0,n):
        print(x)
        x,y = y,x+y
    # i = 0
    # while i < n :
    #     print(x)
    #     x,y,i = y, x+y, i+1

running = True
while running:
    try:
        num = int(input("How many fibonacci numbers? "))
        fib(num)
        running = False
    except ValueError as e:
        print("Error! Please enter a valid amount")
        running = True

