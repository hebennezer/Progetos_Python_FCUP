def quadrado_perfeito(n):
    soma = 0
    k = 1

    while soma < n:
        soma += k
        k+= 2

    if soma == n:
        return True
    else:
        return False


print(quadrado_perfeito(25))