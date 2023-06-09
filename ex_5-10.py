import math

def pascal(n):
    lista = []

    for k in range(n + 1):
        coefficient = math.comb(n, k)
        lista.append(coefficient)
    return lista 

print(f"     {pascal(0)}")
print(f"    {pascal(1)}")
print(f"   {pascal(2)}")
print(f"  {pascal(3)}")
print(pascal(4))