from random import *
from turtle import *

def visivel():
    # Verifica se a turtle esta dentro da janela.
    w = 0.5 * window_width()
    h = 0.5 * window_height()
    x = xcor()
    y = ycor()
    return ((x <= w) and (x >= -w) and (y <= h) and (y >= -h))

def passeio(n, a):
    shape("turtle")
    bgcolor("black")
    color("white")
    speed()

    step = 10

    for i in range(n):
        forward(step)
        if visivel():
            angle =  randint(-a, a)
            left(angle)
        else:
            angle = towards(0, 0)
            setheading(angle)

passeio(300, 30)
exitonclick()
done()
