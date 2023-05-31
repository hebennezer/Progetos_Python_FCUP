quantia_euros = int(input("Qunatia em EUROS: "))


def pagar_quantia(quantia):
    notas_20 = quantia // 20
    quantia %= 20

    notas_10 = quantia // 10
    quantia %= 10

    notas_5 = quantia // 5
    quantia %= 5

    moedas_1 = quantia

    print("Notas de 20:", notas_20)
    print("Notas de 10:", notas_10)
    print("Notas de 5:", notas_5)
    print("Moedas:", moedas_1)


pagar_quantia(quantia_euros)
