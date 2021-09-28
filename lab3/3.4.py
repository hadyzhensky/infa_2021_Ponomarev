import turtle as t
import numpy as np

t.shape('circle')
t.speed(100)
x = -300
y = 0
dt = 0.1

print('Введите скорость бросания черепашки')
V = int(input())
print('Введите угол бросания черепашки')
a = float(input())

Vx: float = V*np.cos(np.pi*a/180)
Vy: float = V*np.sin(np.pi*a/180)

i = 0
t.penup()
t.goto(-300, 0)
t.pendown()

while i < 1000:
    if Vy > 0:
        ay = -10 - 0.05*Vy
    else:
        ay = -10 - 0.05*Vy
    x += Vx*dt
    y += Vy*dt
    Vy += ay*dt
    ax = -0.05*Vx
    Vx += ax*dt
    i = i + 1
    if y < 0:
        Vy = -Vy
    t.goto(x, y)
