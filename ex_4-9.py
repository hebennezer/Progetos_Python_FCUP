def rem_vogais(txt):
    vogais = "aeiouAEIOU"
    sem_vagais = ""
    
    for i in txt:
        if i not in vogais:
            sem_vagais += i
    return sem_vagais 

print(rem_vogais("Abracadabra!"))