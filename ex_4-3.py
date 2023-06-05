def filtra_letras(txt):
    filtra = ""
    for i in txt:
        if (i >= "a") and (i <= "z") or (i >= "A") and (i <= "Z"):
            filtra += i
    return filtra
    
print(filtra_letras("Ola!, -- disse ele, Ebenezer"))
