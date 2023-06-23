from unicodedata import normalize

def histograma(txt):
    txt = normalize("NFD", txt.lower())
    count = {}

    for letra in txt:
        if letra.isalpha():
            count[letra] = count.get(letra, 0) + 1
    
    letras_ordenadas = sorted(count.keys())

    for letra in letras_ordenadas:
        print(letra, ":", count[letra])


print(histograma("As armas e os barões assinalados, \
            Que da ocidental praia Lusitana, \
            Por mares nunca de antes navegados, \
            Passaram ainda além da Taprobana, \
            Em perigos e guerras esforçados,"))
