from typing import List

def triang_sup(A: List[List[float]], eps: float) -> bool:
    n = len(A)

    for i in range(n):
        for j in range(i+1, n):
            if abs(A[i][j]) >= eps:
                return False
    return True


A = [[1.0, 2.0, 3.0],
     [0.0, 4.0, 5.0],
     [0.0, 0.0, 6.0]]

eps = 1e-6

print(triang_sup(A, eps))
