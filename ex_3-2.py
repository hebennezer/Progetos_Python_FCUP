# (a):
for i in range(10, 56, 3):
    if i % 7 == 0:
        break
    print(i, end=" ")
print()


# (b):
for i in range(10, 56, 3):
    if i % 7 == 0:
        continue
    print(i, end=" ")
print()


# numero que são multiplos de 7
for i in range(10, 56, 3):
    if i % 7 != 0:
        continue
    print(i, end=" ")
print()
