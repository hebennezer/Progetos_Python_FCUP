import math

xs = [5, 0, 42, 10, 24, 30, 81]
# (a)
for i in xs:
    print(i)

# (b)
for i in xs:
    print(i, int(math.pow(i, 2)), round(math.sqrt(i), 2))

# (c)
total = 0
for i in xs:
    total += i
    print(i, total)
