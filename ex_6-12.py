def anagramas(txt1, txt2):
    txt1 = "".join(i.lower() for i in txt1 if i.isalpha())
    txt2 = "".join(i.lower() for i in txt2 if i.isalpha())

    if len(txt1) != len(txt2):
        return False
    
    conta_letras = {}
    for letra in txt1:
        conta_letras[letra] = conta_letras.get(letra, 0) + 1
    for letra in txt2:
        conta_letras[letra] = conta_letras.get(letra, 0) - 1
    
    for val in conta_letras.values():
        if val != 0:
            return False
    return True

txt1 = "Quid est veritas?"
txt2 = "Est vir qui adest"

print(anagramas(txt1, txt2))
