import turtle

screen = turtle.getscreen()
t = turtle.Turtle()
title = turtle.title("Turtle run")

t.speed(10)
t.shape("classic")
t.pencolor('green')
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.fillcolor("orange")
t.begin_fill()
t.circle(100)
t.end_fill()
t.dot(20,"green")
t.pensize(20)
t.right(90)
t.forward(50)
t.pencolor('green')
t.pen(fillcolor="red", pencolor ="green", pensize = 3)
t.stamp()
t.fd(20)
t.stamp()
t.fd(30)

c=t.clone()
t.pen(pencolor="red",fillcolor="brown",pensize=1)
t.circle(100)
c.pen(pencolor="green",fillcolor="cyan",pensize=3)
c.circle(50)
