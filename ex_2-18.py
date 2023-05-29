def classifica(p):
    if (p < 0) or (p > 100):
        return "inválido"
    elif p < 50:
        return "insuficiente"
    elif p < 70:
        return "suficiente"
    elif p < 80:
        return "bom"
    elif p < 90:
        return "muito bom"
    else:
        return "excelente"

print(classifica(-1))
print(classifica(0))
print(classifica(50))
print(classifica(70))
print(classifica(80))
print(classifica(90))
print(classifica(102))

    