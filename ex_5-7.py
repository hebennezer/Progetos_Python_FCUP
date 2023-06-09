# (a)
def divisores(n):
    lista = []
    for i in range(1, n):
        if n % i == 0:
            lista.append(i)
    return lista

print(divisores(12))  # Saída: [1, 2, 3, 4, 6]
print(divisores(20))  # Saída: [1, 2, 4, 5, 10]
print(divisores(25), "\n")  # Saída: [1, 5]

# (b)
def perfeito(n):
    soma = 0

    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n

print(perfeito(6))  # True
print(perfeito(10)) # False
