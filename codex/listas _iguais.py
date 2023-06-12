def lista_iguais(xs, ys):
    for i in range(len(xs)):
        if xs[i] != ys[i]:
            return i
    return -1


print(lista_iguais([1, 2], [1, 2]))
print(lista_iguais([1, 3], [1, 2]))
print(lista_iguais([1, 2, 3], [1, 2, 4]))