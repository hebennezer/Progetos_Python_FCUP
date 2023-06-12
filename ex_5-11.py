def anagramas(txt1, txt2):
    txt1 = "".join(i.lower() for i in txt1 if i.isalpha())
    txt2 = "".join(i.lower() for i in txt2 if i.isalpha())

    if len(txt1) != len(txt2):
        return False
    
    for i in txt1:
        if i not in txt2:
            return False
        
        txt2 = txt2.replace(i, "", 1)

    return True


print(anagramas("Anibal Cavaco", "cabala nociva"))