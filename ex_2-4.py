def segundos(horas, mins, segs):
    segs_horas = horas * 3600
    segs_minutos = mins * 60
    segs_total = segs_horas + segs_minutos + segs
    return segs_total

print(segundos(1, 1, 1))