def segundo_Maior(xs):
    maior = max(xs[0], xs[1])
    segundo_maior = min(xs[0], xs[1])

    for i in xs[2:]:
        if i > maior:
            segundo_maior = maior
            maior = i
        elif i > segundo_maior:
            segundo_maior = i

    return segundo_maior

print(segundo_Maior([22, 2, 35, 10]))