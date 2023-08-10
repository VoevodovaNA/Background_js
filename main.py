import turtle
from random import uniform

screen = turtle.Screen()
screen.register_shape("cat.gif") 
turtle.shape("cat.gif")
turtle.penup()
turtle.setheading(90)
turtle.speed(1)
turtle.tracer(1)
for i in range (1,100):
    a=uniform(-90,90)
    turtle.left(a)
    turtle.update()
    d=uniform(-100,100)
    turtle.forward(d)
    turtle.update()
turtle.exitonclick()
