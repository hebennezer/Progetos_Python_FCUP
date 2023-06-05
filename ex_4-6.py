def palindromo_geral(txt):
    filtra = ""
    for i in txt:
        if (i >= "a") and (i <= "z") or (i >= "A") and (i <= "Z"):
            filtra += i
    
    filtra_lower = filtra.lower()
    inver = ""
    
    for i in filtra_lower:
        inver = i + inver
    if inver == filtra_lower:
        return True
    else:
        return False


print(palindromo_geral("Amora me tem aroma."))
print(palindromo_geral("Madam, I’m Adam."))
print(palindromo_geral("A man, a plan, a canal: Panama"))
print(palindromo_geral("Ebenezer Alves de Souza"))
