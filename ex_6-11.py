from unicodedata import normalize

def conta_letras(txt):
    txt = normalize("NFD", txt.lower())
    conta_letras = {}

    for letra in txt:
        if letra.isalpha():
            conta_letras[letra] = conta_letras.get(letra, 0) + 1
    
    letra_ordenadas = sorted(conta_letras.keys())

    for letra in letra_ordenadas:
        print(letra, ":", conta_letras[letra])    

print(conta_letras("A luz do sol é amarela"))
print(conta_letras(\
                   "As armas e os barões assinalados, \
            Que da ocidental praia Lusitana, \
            Por mares nunca de antes navegados, \
            Passaram ainda além da Taprobana, \
            Em perigos e guerras esforçados," \
                ))