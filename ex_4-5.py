def palindromo(txt):
    txt_lower = txt.lower()
    inver = ""
    
    for i in txt_lower:
        inver = i + inver
    if inver == txt_lower:
        return True
    else:
        return False
    

print(palindromo("Reviver"))
print(palindromo("reviver"))
print(palindromo("Ebenezer"))

