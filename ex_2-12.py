import math


def sdq(d):
	soma_quadrada = sum([i**2 for i in d])
	return soma_quadrada

valor = [-6.9, 4.7,]
resultado = sdq(valor)
print(f"{resultado:.1f}")