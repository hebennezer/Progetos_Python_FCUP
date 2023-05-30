tempC = [-5, 0, 5, 10, 15, 20, 25]
""" 
#(a)
for i in tempC:
    print(i)

#(b)
for i in range(len(tempC)):
    print(tempC[i])

#(c)
i = 0
while i < len(tempC):
    print(tempC[i])
    i += 1 """

#(d)
def celsius():
    for celsius in tempC:
        fahrenheit = celsius*(5 / 9) + 32
        print(f"Graus Celcios: {celsius}\tGraus Fahrenheit: {fahrenheit:.1f}")

celsius()
