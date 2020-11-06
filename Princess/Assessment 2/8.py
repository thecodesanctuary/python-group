import random

p = 1
for i in range(10):
    a = random.randint(0,10)
    b = random.randint(0,10)
    c = a * b
    d = int(input("Question %d: %d X %d = " %(p, a, b)))
    if d == c:
        print("Correct!")
    elif d != c:
        print("Wrong. The correct answer is %d." %(c))
    p = p + 1