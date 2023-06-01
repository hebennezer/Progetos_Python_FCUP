from math import *

lista_numeros = [5, 6, 8, 10, 6, 12, 9]

def media_geom(xs):
    produto = 1
    n = len(xs)

    for i in xs:
        produto *= i
    
    return pow(produto, 1/n)


print(media_geom(lista_numeros))