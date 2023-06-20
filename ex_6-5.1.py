def magico(A):
    n = len(A)
    
    # Calcular a soma de referência (soma das linhas)
    soma_linhas = sum(A[0])
    
    # Verificar a soma das linhas, colunas e diagonais simultaneamente
    for i in range(1, n):
        if sum(A[i]) != soma_linhas:
            return False
        
        soma_coluna = 0
        for j in range(n):
            soma_coluna += A[j][i]
        if soma_coluna != soma_linhas:
            return False
        
        soma_diagonal_principal = 0
        soma_diagonal_secundaria = 0
        for k in range(n):
            soma_diagonal_principal += A[k][k]
            soma_diagonal_secundaria += A[k][n-k-1]
        if soma_diagonal_principal != soma_linhas or soma_diagonal_secundaria != soma_linhas:
            return False
    
    # Se todas as somas forem iguais, é um quadrado pseudo-mágico
    return True
