fmt = " *|" + 10 * "%3d "

print(fmt % tuple(range(1, 11)))
print(43 * "=")

fmt = "%2d|" + 10 * "%3d "
for i in range(1, 11):
    linha = [i]
    for j in range(1, 11):
        linha.append(i * j)
    print(fmt % tuple(linha))
