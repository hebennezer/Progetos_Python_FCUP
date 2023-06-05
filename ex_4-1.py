def conta_letras(txt):
    cont = 0
    for i in txt:
        if i >= "A" and i <= "z":
            cont += 1
    return cont


print(conta_letras("Ola, Mundo!"))