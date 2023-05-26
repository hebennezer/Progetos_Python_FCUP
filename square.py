from turtle import *


def square(side):
    for c in ["red", "blue", "green", "white"]:
        color(c)
        forward(side)
        left(90)


reset()
speed(15)
bgcolor("black")

for i in range(50):
    square(50 + i * 5)
    left(10)
    
exitonclick()
done()
