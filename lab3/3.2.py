import turtle as t
import numpy as np
t.shape("turtle")
m = -300
n = 0
t.penup()
t.goto(m, n)
t.pendown()
t.left(90)
x = 40
print('Введите индекс через пробелы')
A = input().split()

def cif():
    if a == 0:
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(2 * x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
    if a == 1:
        t.right(45)
        t.forward(np.sqrt(2) * x)
        t.right(135)
        t.forward(2 * x)
        t.right(180)
    if a == 2:
        t.penup()
        t.forward(x)
        t.pendown()
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(45)
        t.forward(np.sqrt(2) * x)
        t.left(135)
        t.forward(x)
        t.left(90)
    if a == 3:
        t.penup()
        t.forward(x)
        t.pendown()
        t.right(90)
        t.forward(x)
        t.right(135)
        t.forward(np.sqrt(2) * x)
        t.left(135)
        t.forward(x)
        t.right(135)
        t.forward(np.sqrt(2) * x)
        t.right(135)
    if a == 4:
        t.penup()
        t.forward(x)
        t.pendown()
        t.left(180)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(180)
        t.forward(2 * x)
        t.left(180)
    if a == 5:
        t.penup()
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.left(180)
        t.pendown()
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
    if a == 6:
        t.penup()
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(135)
        t.pendown()
        t.forward(np.sqrt(2) * x)
        t.left(45)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.right(90)
    if a == 7:
        t.penup()
        t.forward(x)
        t.pendown()
        t.right(90)
        t.forward(x)
        t.right(135)
        t.forward(np.sqrt(2) * x)
        t.left(45)
        t.forward(x)
        t.right(180)
    if a == 8:
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(2 * x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.left(90)
    if a == 9:
        t.right(90)
        t.penup()
        t.forward(x)
        t.left(180)
        t.pendown()
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(45)
        t.forward(np.sqrt(2) * x)
        t.right(135)


for i in range(len(A)):
    A[i] = int(A[i])
    a = A[i]
    cif()
    t.penup()
    t.goto(m, n)
    t.right(90)
    t.forward((x*(i+1)) + ((x/2)*(i+1)))
    t.left(90)
    t.pendown()

