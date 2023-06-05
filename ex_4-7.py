def rem_espacos(txt):
    while "  " in txt:
        txt = txt.replace("  ", " ")
    return txt


print(rem_espacos("Ola,    tudo  bem     !"))