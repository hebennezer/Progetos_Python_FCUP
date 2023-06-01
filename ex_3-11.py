#(a)
def mindiv(n):
    for d in range(2, n):
        if n % d == 0:
            return d


print(mindiv(25))


#(b)
def primo(n):
    n1 = int(n ** 0.5)
    for i in range(2, n1+1):
        if n % i == 0:
            return False
    return True


print(primo(29))


#(c)
def mindiv(n):
    for d in range(2, int(n ** 0.5 + 1)):
        if n % d == 0:
            return d


print(mindiv(25))
