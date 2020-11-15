a = []
b = []
c = []
for i in range(0,50):
    a.append(i)
print(a)

for i in range(0,50):
    square = i * i
    b.append(square)
print(b)

alpha = 'a'
for i in range(1,27):
    mult = alpha * i
    c.append(mult)
    alpha = chr(ord(alpha) + 1)
print(c)
