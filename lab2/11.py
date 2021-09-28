import turtle as t
t.shape('turtle')
a=50
while a < 120:
 t.left(90)
 t.circle(a)
 t.circle(-a)
 t.right(90)
 a = a + 10