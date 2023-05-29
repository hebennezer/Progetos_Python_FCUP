def triangulo(a, b, c):
    if ((a + b) > c) and ((b + c) > a) and ((c + a) > b):
        return True
    else:
        return False

print(triangulo(1, 7, 9))