import math

def coprimos(n):
    coprimes = []
    for i in range(1, n+1):
        if math.gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

print(coprimos(14))