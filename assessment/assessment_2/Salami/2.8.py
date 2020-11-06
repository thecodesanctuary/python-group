import random

for i in range(1,11):
    x = random.randint(1,10)
    y = random.randint(1,10)
    print(f"Question {i}: {x} x {y} = ")
    ans = (input(" "))
    if ans == (x*y):
        print("Right!\n")
    else:
        print("Wromg!")
        print(f"The answer is {x*y}\n")
