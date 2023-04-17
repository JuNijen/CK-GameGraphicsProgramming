import pygame
import numpy as np


pygame.init()

screenWidth = 1280
screenHeight = 720


BACKGROUND_COLOR = (217, 217, 217)
LINE_COLOR = (200, 200, 200)
STANDARD_LINE_COLOR_X = (0, 0, 200)
STANDARD_LINE_COLOR_Y = (200, 0, 0)

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Graphics Programming")

running = True;

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOR)

    for x in range (0, 720, 10):
        pygame.draw.line(screen, LINE_COLOR , (0, x), (1280, x), 1)

    for y in range (0, 1280, 10):
        pygame.draw.line(screen, LINE_COLOR , (y, 0), (y, 720), 1)

    pygame.draw.line(screen, STANDARD_LINE_COLOR_X , (0, 360), (1280, 360), 2)
    pygame.draw.line(screen, STANDARD_LINE_COLOR_Y , (640, 0), (640, 720), 2)


    drawRectPoints = [(0,0),(100,0),(100,100),(0,100)]

    for i in range (0, 4, 1):
        drawRectPoints[i] = (screenWidth/2 + drawRectPoints[i][0], screenHeight/2 - drawRectPoints[i][1])

    # drawRectPoints = [
    #     (0 + screenWidth/2,screenHeight/2 - 0),
    #     (100 + screenWidth/2, screenHeight/2 - 0),
    #     (100 + screenWidth/2, screenHeight/2 - 100),
    #     (0 + screenWidth/2, screenHeight/2 - 100)
    #     ]

    _matrixA = np.array(
        [1, 0],
        [0, 1]
        )
    _matrixB = np.array(
        [2, 0],
        [0, 2]
        )
    _pos = np.array([
        [1],
        [1]
        ])

    pygame.draw.polygon(screen, (255,0,0), drawRectPoints, 1)


    pygame.display.flip()
pygame.quit()