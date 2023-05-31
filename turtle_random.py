from random import *
from turtle import *

def passeio(n, a):
    shape("turtle")
    bgcolor("black")
    color("white")
    speed(1)

    step = 10

    for i in range(n):
        forward(step)
        angle =  randint(-a, a)
        left(angle)

passeio(100, 30)
exitonclick()
done()