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

print("2000", bissexto(2000))
print("2004", bissexto(2004))
print("2008", bissexto(2008))
print("2032", bissexto(2032))
print("2048", bissexto(2048))
print("2040", bissexto(2040))