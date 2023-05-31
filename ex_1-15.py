from math import *


def hypotenuse(a, b):
    C = sqrt(a**2 + b**2)
    return round(C, 2)


print(hypotenuse(2, 3))
