import turtle


def poligono_reg(n, lado):
    angulo = 360 / n  # furmula para o poligano

    turtle.shape("turtle")  # para mudar o icone para uma tartaruga
    turtle.speed(1)  # controla a velociade com a qual se desloca
    turtle.color("white")  # muda a cor do rastro
    turtle.bgcolor("black")  # muda a cor do brackground

    for i in range(n):
        turtle.forward(lado)
        turtle.left(angulo)


def casa(lado):
    poligono_reg(3, 100)
    turtle.right(90)
    poligono_reg(4, 100)


casa(100)

turtle.exitonclick()
turtle.done()
