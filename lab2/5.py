import turtle

turtle.shape('turtle')

x = 20
n = 1
while n <= 10:
    n = n+1
    turtle.right(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.pendown()
    x = x+10
