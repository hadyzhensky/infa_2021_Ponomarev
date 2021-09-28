from random import *
import turtle as t

t.shape("turtle")
x = 1
y = 50
a = -360
b = 360

n = 1000
while n > 0:
    t.forward(randint(x, y))
    t.left(randint(a, b))
    n = n-1
