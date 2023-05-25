import math

def P(P0, r, t):
    Pt = P0 * math.e**(r * t)
    return round(Pt, 2)

print("$", P(1000, 0.05, 2))