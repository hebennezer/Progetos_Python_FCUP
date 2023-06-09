# beatles = [1, 2, 3]
# print(beatles, "\n")
# beatles[0] = "Ebenezer"
# beatles[2] = "Souza"
# print(beatles, "\n")

# beatles[1:2] = ["Alves", "de"]

# print(beatles, "\n")

# del beatles[0]
# print(beatles, "\n")

# beatles[0:1] = []
# print(beatles, "\n")

# beatles = [15, 5, 1, 6, 14, 9]
# beatles.sort()
# print(beatles)

agenda = []

def acrescentar(agenda, nome, email):
    agenda.append((nome, email))

acrescentar(agenda, "benne", "tes@gmail.com")
acrescentar(agenda, "alves", "muito@gmail.com")

print(agenda, "\n")

def procurar(agenda, txt):
    email = []
    for i in agenda:
        if txt in i[0]:
            email.append(i[1])
    return email

print(procurar(agenda, "alves"))


