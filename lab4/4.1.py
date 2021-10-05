import pygame

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 600))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (225, 0, 0)

sc.fill(WHITE)
pygame.draw.circle(sc, YELLOW,
                   (300, 300), 150)
pygame.draw.circle(sc, RED,
                   (350, 250), 30)
pygame.draw.circle(sc, RED,
                   (250, 250), 20)
pygame.draw.circle(sc, BLACK,
                   (350, 250), 15)
pygame.draw.circle(sc, BLACK,
                   (250, 250), 10)
pygame.draw.line(sc, BLACK,
                 [180, 190],
                 [280, 240], 15)
pygame.draw.line(sc, BLACK,
                 [320, 235],
                 [420, 185], 15)
pygame.draw.line(sc, BLACK,
                 [230, 360],
                 [370, 360], 20)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()



