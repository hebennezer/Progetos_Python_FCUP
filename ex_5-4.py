def intervalo(xs, a, b):
    cont = 0
    for i in xs:
        if a <= i <= b:
            cont += 1
    return cont


lista = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
resultado = intervalo(lista, 1, 3)
print(resultado)
