def bissexto(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


for i in range(2000, 2021):
    tabela = bissexto(i)
    print(i, tabela)

