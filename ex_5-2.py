def media_geom(xs):
    produto = 1
    for i in xs:
        produto *= i
    media = produto ** (1/len(xs))
    return media

print(f"{media_geom([2, 4, 8]):.2f}")