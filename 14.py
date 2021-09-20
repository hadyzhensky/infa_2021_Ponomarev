import turtle as t

t.shape('turtle')
def st(n):
 t.penup()
 t.goto(10,0)
 t.pendown()
 i=0
 while i<n:
  t.forward(100)
  t.left(180-180/n)
  i=i+1
n=input('Введите n')
n=int(n)
st(n)