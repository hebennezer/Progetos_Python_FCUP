def pseudo_magico(A):
    n = len(A)

    for linha in A:
        if len(linha) != n:
            return False
        
    soma_magica = sum(A[0])

    for linha in A:
        if sum(linha) != soma_magica:
            return False
    
    for coluna in range(n):
        soma_coluna = 0
        for linha in range(n):
            soma_coluna += A[linha][coluna]
        if soma_coluna != soma_magica:
            return False
    
    soma_diagonal_principal = 0
    for i in range(n):
        soma_diagonal_principal += A[i][i]
    if soma_diagonal_principal != soma_magica:
        return False
    
    soma_diagonal_secundaria = 0
    for i in range(n):
        soma_diagonal_secundaria += A[i][n -1 -i]
    if soma_diagonal_secundaria != soma_magica:
        return False
    
    return True


matriz = [[2, 7, 6],
          [9, 5, 1],
          [4, 3, 8]]

resultado = pseudo_magico(matriz)
print(resultado)
