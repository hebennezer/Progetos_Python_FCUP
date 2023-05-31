import turtle


def friso(n, lado):

    turtle.speed(1)
    turtle.color("white")
    turtle.bgcolor("black")

    for i in range(n):
        turtle.forward(lado)
        turtle.left(90)
        turtle.forward(lado)
        turtle.right(90)
        turtle.forward(lado)
        turtle.right(90)
        turtle.forward(lado)
        turtle.left(90)


friso(3, 50)
turtle.exitonclick()
turtle.done()
