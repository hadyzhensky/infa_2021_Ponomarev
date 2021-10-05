import pygame

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 800))

WHITE = (255, 255, 255)
GREEN = (0, 200, 64)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
LIGHT_LIGHT_BLUE = (106, 253, 254)
BROWN1 = (106, 81, 0)
BROWN2 = (168, 143, 0)
kot = (250, 159, 68)

pygame.draw.polygon(sc, BROWN1,                      # фон
                    [[0, 0], [600, 0],
                     [600, 400], [0, 400]])
pygame.draw.polygon(sc, BROWN2,
                    [[0, 400], [600, 400],
                     [600, 800], [0, 800]])

pygame.draw.polygon(sc, LIGHT_LIGHT_BLUE,                # окна
                    [[320, 20], [580, 20],
                     [580, 380], [320, 380]])
pygame.draw.polygon(sc, LIGHT_BLUE,
                    [[340, 40], [440, 40],
                     [440, 160], [340, 160]])
pygame.draw.polygon(sc, LIGHT_BLUE,
                    [[460, 40], [560, 40],
                     [560, 160], [460, 160]])
pygame.draw.polygon(sc, LIGHT_BLUE,
                    [[340, 180], [440, 180],
                     [440, 360], [340, 360]])
pygame.draw.polygon(sc, LIGHT_BLUE,
                    [[460, 180], [560, 180],
                     [560, 360], [460, 360]])

pygame.draw.ellipse(sc, kot,                       # хвост
                    (410, 450, 280, 70))
pygame.draw.ellipse(sc, BLACK,
                    (410, 450, 280, 70), 1)
pygame.draw.ellipse(sc, kot,               # туловище
                    (100, 400, 380, 200))
pygame.draw.ellipse(sc, BLACK,
                    (100, 400, 380, 200), 1)
pygame.draw.circle(sc, kot,                   # голова
                   (120, 500), 70)
pygame.draw.circle(sc, BLACK,
                   (120, 500), 70, 1)
pygame.draw.ellipse(sc, kot,               # ноги
                    (155, 565, 90, 40))
pygame.draw.ellipse(sc, BLACK,
                    (155, 565, 90, 40), 1)
pygame.draw.circle(sc, kot,
                   (450, 560), 60)
pygame.draw.circle(sc, BLACK,
                   (450, 560), 60, 1)
pygame.draw.ellipse(sc, kot,
                    (480, 575, 35, 100))
pygame.draw.ellipse(sc, BLACK,
                    (480, 575, 35, 100), 1)



pygame.draw.circle(sc, GREEN,                   # глаза
                   (90, 500), 15)
pygame.draw.circle(sc, BLACK,
                   (90, 500), 15, 1)
pygame.draw.circle(sc, GREEN,
                   (150, 500), 15)
pygame.draw.circle(sc, BLACK,
                   (150, 500), 15, 1)
pygame.draw.ellipse(sc, BLACK,
                    (155, 490, 5, 23))
pygame.draw.ellipse(sc, BLACK,
                    (95, 490, 5, 23))
pygame.draw.ellipse(sc, WHITE,
                    (145, 488, 5, 15))
pygame.draw.ellipse(sc, WHITE,
                    (85, 488, 5, 15))

pygame.draw.polygon(sc, BLACK,                 # ушки
                    [[50, 435], [80, 450],
                     [57, 472]])
pygame.draw.polygon(sc, GRAY,
                    [[52, 437], [77, 452],
                     [58, 470]])
pygame.draw.polygon(sc, BLACK,
                    [[168, 430], [145, 450],
                     [166, 465]])
pygame.draw.polygon(sc, GRAY,
                    [[166, 432], [147, 452],
                     [164, 463]])

pygame.draw.polygon(sc, BLACK,                     # носик
                    [[113, 523], [127, 523],
                     [120, 532]])
pygame.draw.polygon(sc, GRAY,
                    [[115, 525], [125, 525],
                     [120, 530]])

pygame.draw.aaline(sc, BLACK,            # усики
                   [140, 532],
                   [250, 515])
pygame.draw.aaline(sc, BLACK,
                   [140, 538],
                   [250, 535])
pygame.draw.aaline(sc, BLACK,
                   [140, 543],
                   [250, 555])
pygame.draw.aaline(sc, BLACK,
                   [100, 531],
                   [0, 515])
pygame.draw.aaline(sc, BLACK,
                   [100, 537],
                   [0, 535])
pygame.draw.aaline(sc, BLACK,
                   [100, 541],
                   [0, 555])

pygame.draw.aaline(sc, BLACK,            # ротик
                   [120, 530],
                   [130, 550])
pygame.draw.aaline(sc, BLACK,
                   [120, 530],
                   [110, 550])

pygame.draw.circle(sc, GRAY,                   # клубок
                   (350, 700), 50)
pygame.draw.circle(sc, BLACK,
                   (350, 700), 50, 1)
pygame.draw.aaline(sc, BLACK,
                   [350, 680],
                   [380, 710])
pygame.draw.aaline(sc, BLACK,
                   [350, 690],
                   [380, 730])
pygame.draw.aaline(sc, BLACK,
                   [350, 670],
                   [380, 700])
pygame.draw.aaline(sc, BLACK,
                   [350, 685],
                   [310, 715])
pygame.draw.aaline(sc, BLACK,
                   [350, 695],
                   [320, 725])
pygame.draw.aaline(sc, BLACK,
                   [350, 750],
                   [300, 750])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
