distance = float(input("what's distance traveled in kilometers? "))
liters_consumed = float(input("How mane liters of fuel consumed by the car? "))

AVG = distance / liters_consumed
AVG_aredondado = round(AVG, 3)

print(AVG_aredondado)
