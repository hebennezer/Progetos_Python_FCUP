import math


def area_triangulo(a, b, c):
    s = (a + b + c) / 2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return A


print(f"{area_triangulo(5, 7, 9):.2f}")
