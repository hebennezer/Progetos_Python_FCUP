c_i = float(input("Capital incial: "))
taxa_de_juros = int(input("Taxa de juros: "))

r = taxa_de_juros / 100

def catital_final(c_i, r):
    for i in range(0, 25):
        c_f = c_i * (1 + r / 12)**i
        print(f"Meses {i} Capital final é ${c_f:.2f}")

catital_final(c_i, r)