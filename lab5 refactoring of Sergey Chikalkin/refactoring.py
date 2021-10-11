import pygame as p
import numpy as np
p.init()

FPS = 30
screen = p.display.set_mode((400, 600))
screen.fill((200, 200, 200))
#p.draw.rect(surface, (0, 0, 0), (0, 0, 0, 0))
#p.draw.circle(screen, (0, 0, 0), (0, 0), 50)
#p.draw.line(screen, (0, 0, 0), (0, 0), (0, 0), 0)
#p.p.draw.polygon(screen, (255, 255, 0), [(100,100), (200,50), (300,100), (100,100)])

p.draw.aalines(screen, (0, 0, 0), False, [(0, 0), (50, 0), (70, 30), (70, 50)])
p.draw.polygon(screen, (0, 255, 255), [(0, 200), (80, 120), (120, 150), (250, 250), (300, 80), (320, 120), (400, 30), (400, 0), (0, 0)])
p.draw.polygon(screen, (0, 255, 0), [(400, 350),(200, 370), (195, 350),(100, 350), (0, 355), (0, 600), (400, 600)])



def ell(x, y, m, n, surf):
	'''
	Функция рисует овал, x,y- координаты верхней верхней вершины прямоугольника, в который 
	заключен овал, m,n - стороны этого прямоугольника, surf - поверхность, на которую 
	"отправляется" овал
	'''
	p.draw.ellipse(surf, (255, 255, 255), (x, y, m, n), 0)
def draw_lama(x, y, width, height, surf):
	'''
	Функция рисует ламу на поверхности surf, вписанную в прямоугольник с координатами
	левой верхней вершины (x,y) и сторонами width (соответствует ширине овцы) и height
	(ее высоте)
	'''
	h=height/250
	w=width/200
	ell(x, y+int(125*h), int(150*w), int(50*h), surf)#туловище
	ell(x, y+int(155*h), int(20*w), int(40*h), surf)#заднее левое бедро
	ell(x, y+int(191*h), int(20*w), int(40*h), surf)#задняя левая голень
	ell(x+int(100*w), y+int(155*h), int(20*w), int(40*h), surf)#переднее левое бедро
	ell(x+int(100*w), y+int(191*h), int(20*w), int(40*h), surf)#передняя левая голень
	ell(x+int(120*w), y+int(165*h), int(20*w), int(40*h), surf)#заднее правое бедро
	ell(x+int(120*w), y+int(201*h), int(20*w), int(40*h), surf)#задняя правая голень
	ell(x+int(20*w), y+int(165*h), int(20*w), int(40*h), surf)#переднее правое бедро
	ell(x+int(20*w), y+int(201*h), int(20*w), int(40*h), surf)#передняя правая голень
	ell(x+int(100*w), y+int(227*h), int(30*w), int(10*h), surf)#передняя левая ступня
	ell(x+int(120*w), y+int(237*h), int(30*w), int(10*h), surf)#передняя правая ступня
	ell(x, y+int(227*h), int(30*w), int(10*h), surf)#задняя левая ступня
	ell(x+int(20*w), y+int(237*h), int(30*w), int(10*h), surf)#задняя правая ступня
	ell(x+int(110*w), y+int(45*h), int(40*w), int(110*h), surf)#шея
	ell(x+int(110*w), y+int(20*h), int(50*w), int(30*h), surf)#голова
	p.draw.ellipse(surf, (255, 0, 255), (x+int(125*w), y+int(20*h), int(15*w), int(15*h)), 0)#глаз#
	p.draw.ellipse(surf, (0, 0, 0), (x+int(133*w), y+int(23*h), int(6*w), int(6*h)), 0)#зрачок#
	p.draw.polygon(surf, (255, 255, 255), [(x+int(126*w), y+int(21*h)), (x+int(126*w), y+int(6*h)), (x+int(124*w), y+int(23*h))])#рог#
	p.draw.polygon(surf, (255, 255, 255), [(x+int(123*w), y+int(29*h)), (x+int(103*w), y+int(14*h)), (x+int(121*w), y+int(31*h))])#рог#

d=[0]*5 #блок создания поверхностей,на которых помещаем лам
for i in range(5):
	if i==1:
		d[i]=p.Surface((300, 300),p.SRCALPHA)
		x=200
		y=250
	if i==0:
		d[i]=p.Surface((700, 700),p.SRCALPHA)
		x=460
		y=580
	if i>1:
		d[i]=p.Surface((100, 100),p.SRCALPHA)
		x=65
		y=82
	draw_lama(0, 0, x, y, d[i])
	if (i==1) or (i==3):
		d[i]=p.transform.flip(d[i], True, False)

 
def g (a, d, x, y):#функция, рисующая лепесток с характерным размером d с координатами
	#x,y верхней левой вершины описанного вокруг лепестка прямоугольника в поверхности a
	p.draw.ellipse(a, (255, 255, 255), (x, y, 20*d//60, 10*d//60), 0)

def flower(d, surf):#функция, рисующая одну ромашку
	g(surf, d, 10*d//60, 0)
	g(surf, d, 30*d//60, 0)
	g(surf, d, 0, 8*d//60)
	g(surf, d, 40*d//60, 8*d//60)
	g(surf, d, 10*d//60, 16*d//60)
	g(surf, d, 30*d//60, 16*d//60)
	p.draw.ellipse(surf, (255, 255, 0), (20*d//60, 8*d//60, 20*d//60, 10*d//60), 0)
	
def cir(a, scr):#функция, рисующая 1 круг с ромашками диаметром a на пов-сти scr   
	b=[0]*5
	p.draw.ellipse(scr, (0, 155, 0), (0, 0, a, a))
	for i in range (5):
		b[i]=p.Surface((60*a//150, 30*a//150),p.SRCALPHA)
		flower(60*a//150, b[i])
		b[i]=p.transform.rotate(b[i], 30*i)
		if i==4:
			scr.blit(b[4], (75*a//150, 10*a//150))
		if i==0:
			scr.blit(b[0], (40*a//150, 95*a//150))
		if i==1:
			scr.blit(b[1], (15*a//150, 20*a//150))
		if i==2:
			scr.blit(b[2], (95*a//150, 65*a//150))
		if i==3:
			scr.blit(b[3], (15*a//150, 65*a//150))

sc=[0]*5 #блок создания поверхностей, на которые помещаем круги с ромашками 
for i in range(5):
	sc[i]=p.Surface((150, 150),p.SRCALPHA)
	if i!=0:
		sc[i]=p.transform.smoothscale(sc[i], (int(150/(i+2)), int(150/(i+2))))
		a=int(150/(i+2))
	else:
		a=150
	cir(a, sc[i])
    
#блок вывода полей ромашек на экран
screen.blit(sc[0], (150, 450))
screen.blit(sc[1], (350, 350))
screen.blit(sc[2], (50, 360))
screen.blit(sc[3], (150, 400))
screen.blit(sc[4], (370, 520))

#блок вывода лам на экран
screen.blit(d[0], (-240, 380))
screen.blit(d[1], (140, 300))
screen.blit(d[2], (100, 300))
screen.blit(d[3], (-10, 290))
screen.blit(d[4], (180, 350))

	
	


							   
p.display.update()
clock = p.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in p.event.get():
		if event.type == p.QUIT:
			finished = True

p.quit()