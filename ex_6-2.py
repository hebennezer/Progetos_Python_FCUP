lista = [2, 2, 3, 1, 4, 4]
lista_2 = ['a', 'b', 'b', 'b', 'a']

def remadj(xs):
    nova_lista = []
    for i in range(len(xs)-1):
        if xs[i] != xs[i+1]:
            nova_lista.append(xs[i])
    nova_lista.append(xs[-1])
    return nova_lista

print(remadj(lista))
print(remadj(lista_2))