def ocorrencias(txt, c):
    ocorr_indices = []

    for i in range(len(txt)):
        if txt[i] == c:
            ocorr_indices.append(i)
    return ocorr_indices


txt = "Ebenezer"
c = "e"
indices = ocorrencias(txt.lower(), c)
print(indices)  # [1, 3, 5]
