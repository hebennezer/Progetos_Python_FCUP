from turtle import *


def square(side):
    for c in ["red", "blue", "green", "black"]:
        color(c)
        forward(side)
        left(90)


reset()
speed(15)

for i in range(50):
    square(50 + i * 5)
    left(10)
done()
