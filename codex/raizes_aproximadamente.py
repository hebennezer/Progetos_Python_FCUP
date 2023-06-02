def raiz(q, epsilon):
    x_n = q / 2
    x_n1 = 0

    while abs(x_n - x_n1) >= epsilon:
        x_n1 = x_n
        x_n = 0.5 * (x_n + q / x_n)
    return x_n

print(raiz(16, 0.0001))