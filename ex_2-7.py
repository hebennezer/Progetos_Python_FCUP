def tabela_quadrado(n):
    for i in range(n+1):
        quadrado = i ** 2
        print(f"{i} {quadrado}")


tabela_quadrado(int(input("N: ")))
