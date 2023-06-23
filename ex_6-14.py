def morse(txt):
    tabela_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..'
    }

    morse_txt = ""
    for letra in txt:
        upper_letra = letra.upper()
        if upper_letra in tabela_morse:
            morse_txt += tabela_morse[upper_letra] + " | "
    
    return morse_txt.strip()

print(morse('ABC'))
print(morse('ATTACK AT DAWN')) 
