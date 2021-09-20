import turtle

turtle.shape('turtle')
k = 1
print('Введите число лап паука')

n = int(input())
a = 360/n
while k <= n:
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(a)
    k = k+1
