def triangular(n):
    soma = 0
    k = 1
    while soma < n:
        soma += k
        k += 1
    if soma == n:
        return True
    else:
        return False

print(triangular(10))