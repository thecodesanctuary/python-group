def triangle(n):
    x = '*'
    for i in range(0,n):
        print(x)
        x = x + '*'

running = True
while running:
    try:
        num = int(input("How many levels do you want your triangle? (e.g 1,2,3)... "))
        triangle(num)
        running = False
    except ValueError as e:
        print("Na ment?")
        print("Ogbeni type number jare!")
        running = True

