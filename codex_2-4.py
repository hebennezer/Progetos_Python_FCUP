p = int(input("nota: "))


def classifica(p):
    if (p < 0) or (p > 100):
        return "invalido"
    elif p < 50:
        return "insuficiente"
    elif p < 70:
        return "suficiente"
    elif p < 80:
        return "bom"
    elif p < 90:
        return "muito bom"
    else:
        return "execelente"


print(classifica(p))
