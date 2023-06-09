import re

def palavras(txt):
    palavras_encon = re.findall(r"\b[A-Za-z]+\b", txt)
    return palavras_encon


print(palavras("---A Maria tinha um cordeirinho?"))
