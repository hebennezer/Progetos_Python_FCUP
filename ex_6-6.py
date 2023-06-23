from typing import List

def transposta(A: List[List[int]]) -> List[List[int]]:
    if not A:
        return []
    
    n = len(A)
    m = len(A[0])

    transposta = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            transposta[j][i] = A[i][j]
    return transposta


A = [[1, 2, 3],
     [4, 5, 6]]

AT = transposta(A)
print(AT)
