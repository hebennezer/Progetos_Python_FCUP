def soma_colunas(A, x):
    n = len(A)

    m = len(A[0])
    for j in range(m):
        soma = 0
        for i in range(n):
            soma += A[i][j]
        
        if soma != x:
            return False
    return True


A = [[1, 0, 4], 
     [4, 4, 4], 
     [7, 8, 4]]
x = 12
resultado = soma_colunas(A, x)
print(resultado)

B = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
x = 15
resultado = soma_colunas(B, x)
print(resultado)
