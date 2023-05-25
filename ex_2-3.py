import math

def radianos(graus, mins, segs):
    angulo_decimal = graus + mins / 60 + segs / 3600
    rad = angulo_decimal * (math.pi / 180)
    return rad

print(radianos(45, 30, 0))
