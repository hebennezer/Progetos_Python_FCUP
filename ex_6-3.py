def soma_linhas(A, x):
    n = len(A)
    for linha in A:
        if sum(linha) != x:
            return False
    return True

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

x = 6
print(soma_linhas(A, x))

B = [[1, 2, 3],
     [0, 1, 5],
     [2, 2, 2]]

x = 6
print(soma_linhas(B, x))

