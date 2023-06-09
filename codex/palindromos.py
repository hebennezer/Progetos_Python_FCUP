def palindromos(txt):
    txt = "".join(i for i in txt if i.isalpha())
    txt = txt.lower()
    return txt == txt[::-1]

print(palindromos("Ebenezer"))
