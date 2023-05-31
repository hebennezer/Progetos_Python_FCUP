import random
""" 
d = random.randint(1, 6)
maximo = d
minimo = d

soma = 0
for i in range(1000):
    d = random.randint(1, 6)
    maximo = max(maximo, d)
    minimo = min(minimo, d)
    soma += d
    media = soma / 1000

print(f"Valor {maximo = }")
print(f"Valor {minimo = }")
print(f"{media = :.1f}")
 """
random.seed(0)

for i in range(10):
    print(random.randint(1, 6))
