def algarismos(n):
    cont = 0
    while n != 0:
        n //= 10
        cont += 1
    return cont


print(algarismos(9733))
