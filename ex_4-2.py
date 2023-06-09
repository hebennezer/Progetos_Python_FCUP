def apenas_letras(txt):
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = A.lower()
    for i in txt:
        if (i not in A) and (i not in a):
            return False
    return True


print(apenas_letras("Ola, Mundo"))
print(apenas_letras("Abracadabra"))
print(apenas_letras("jQ3:mT_"))