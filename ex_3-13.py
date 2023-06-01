def binom(n, k):
    numerador = 1
    denominador = 1

    if (k < 0) or (k > n): # Verifica se k está fora do intervalo válido
        return 0
    
    for i in range(k):     # Calcula o numerador: n * (n-1) * ... * (n-k+1)
        numerador *= n - i
    
    for i in range(1, k+1):  # Calcula o denominador: k!
        denominador *= i
    
    return numerador // denominador   # Calcula o coeficiente binomial: numerador / denominador


print(binom(10, 3))
print(binom(5, 2))
print(binom(7, 0))
print(binom(4, 5))