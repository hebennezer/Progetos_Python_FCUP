"""
    Calcula o somatório dos primeiros k termos da série de Leibniz.

    A série de Leibniz é uma série infinita que aproxima o valor de pi/4:

    1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...

    A função leibniz(k) retorna a soma dos primeiros k termos dessa série.

    Parâmetros:
    - k (int): O número de termos a serem somados. Deve ser um número inteiro positivo.

    Retorno:
    - float: A soma dos primeiros k termos da série de Leibniz.

    Exemplos:
    >>> leibniz(5)
    0.8666666666666667
    >>> leibniz(10)
    0.7604599047323508
    >>> leibniz(0)
    0.0

    Nota:
    - A série de Leibniz converge para pi/4 à medida que mais termos são adicionados.
    """

def leibniz(k):
    total = 0.0
    sign = 1

    for i in range(k):
        term = 4 * (1 / (2 * i + 1))
        total += sign * term
        sign *= -1
    return total


print(leibniz(1000))