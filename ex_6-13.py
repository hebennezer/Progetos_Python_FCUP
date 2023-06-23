def mais_freq(txt):
    txt = txt.upper()
    ocorrencias = {}

    for letra in txt:
        if letra.isalpha():
            if letra in ocorrencias:
                ocorrencias[letra] += 1
            else:
                ocorrencias[letra] = 1
    
    max_ocorrencia = max(ocorrencias.values())
    mais_frequente = min(filter(lambda letra: ocorrencias[letra] == max_ocorrencia, ocorrencias))

    return mais_frequente

print(mais_freq('excecionalmente'))
print(mais_freq('Inconstitucional'))
