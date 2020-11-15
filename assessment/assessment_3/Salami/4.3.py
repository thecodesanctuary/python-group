start = [8,9,10]

start[1] = 17
start.append(4)
start.append(5)
start.append(6)
del start[0]
start.sort()
start = start * 2
start.insert(3, 25)

print(start)