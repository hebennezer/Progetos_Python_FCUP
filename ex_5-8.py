def repetidos(lista):
    if len(lista) == len(set(lista)):
        return False
    else:
        return True


print(repetidos(["ole", "oli", "ole", "abba"]))
print(repetidos(["ole", "oli", "ola", "abba"]))
print(repetidos([1, 2, 3, 4, 5, 6]))
print(repetidos([1, 2, 3, 2, 4, 5]))
