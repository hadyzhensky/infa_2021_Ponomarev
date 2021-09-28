import turtle as t
import numpy as np
t.shape("turtle")

m = -300
n = 0
x = 40

t.penup()
t.goto(m, n)
t.pendown()
t.left(90)

print('Введите индекс через пробелы')
A = input().split()

for i in range(len(A)):
    A[i] = int(A[i])
    a = A[i]
    d = ('shrift' + str(a) + '.txt')
    shr = open(d, 'r')
    s = shr.read()
    exec(s)
    shr.close()
    t.penup()
    t.goto(m, n)
    t.right(90)
    t.forward((x*(i+1)) + ((x/2)*(i+1)))
    t.left(90)
    t.pendown()