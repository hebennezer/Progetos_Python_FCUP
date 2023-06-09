import math

def desvio_padrao(xs):
    n = len(xs)
    media = sum(xs) / n

    soma_deferenca_de_quadrados = sum((x - media) ** 2 for x in xs)

    desvio_padrao_amostral = math.sqrt(soma_deferenca_de_quadrados / (n - 1))

    return desvio_padrao_amostral

