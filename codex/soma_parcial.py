def soma_parcial(lista, n):
    return sum(lista[:n+1])

print(soma_parcial([1,2,3], 2))
# Saída: 6

print(soma_parcial([1,2,3], 1))
# Saída: 3

print(soma_parcial([1,2,3], 0))
# Saída: 1
