def conta_letras(txt):
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = A.lower()
    for i in txt:
        if (i not in A) and (i not in a):
            return False
    return True


print(conta_letras("Ola, Mundo"))
print(conta_letras("Abracadabra"))