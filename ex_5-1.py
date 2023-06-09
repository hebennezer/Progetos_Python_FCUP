def media_arit(xs):
    soma = 0
    for i in xs:
        soma += i

    return soma / len(xs)

print(media_arit([2, 3, 1]))