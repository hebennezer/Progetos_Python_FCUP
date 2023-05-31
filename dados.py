import random

numexpr = 1000
soma7 = 0

for i in range(numexpr):
    # lancar dois dados
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    if d1 + d2 == 7:
        soma7 += 1

print("Frequancia = ", soma7/numexpr)
