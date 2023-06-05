def vigenere(chave, txt):
    chave = chave.upper()
    txt = txt.upper()
    cifrado = ""
    chave_idx = 0

    for letra in txt:
        if letra.isalpha():
            deslocamento = ord(chave[chave_idx]) - ord("A")
            letra_cifrada = chr((ord(letra) - ord("A") + deslocamento) % 26 + ord("A"))
            cifrado += letra_cifrada
            chave_idx = (chave_idx + 1) % len(chave)
        else:
            cifrado += letra
    return cifrado

print(vigenere("LUAR", "ATAQUEDEMADRUGADA"))
print(vigenere("LUAR", "LNAHFYDVXUDIFAAUL"))

            