def combina(xs, ys):
    len_xs = len(xs)  # Determina o comprimento das listas
    len_ys = len(ys)

    num_tuplas = max(len_xs, len_ys)  # Calcula o número de tuplas necessárias

    if len_xs < len_ys:  # Recicla os elementos da lista com menor comprimento
        xs = xs * num_tuplas
    else:
        ys = ys * num_tuplas
    
    combinados = [(xs[i], ys[i]) for i in range(num_tuplas)] # Combina os elementos das duas listas

    return combinados

print(combina(['a', 'b', 'c'], [1, 2, 3, 4, 5]))
print(combina(['a', 'b', 'c', 'd', 'e'], [1, 2, 3]))
