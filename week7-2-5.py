import math
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


    # 선형 변환 실습 2-1
    _matrix7_2 = np.array([
        [0, 0, 1],
        [0, 100, 1],
        [100, 100, 1],
        [100, 0, 1],
        ])
    
    _matrix7_2_point = np.array([
        [100],
        [100],
        [1],
        ])

    # 전단 변환
    _matrix7_2_shear = np.array([
        [1, 0, 50],
        [0, 1, 50],
        [0, 0, 1]
        ])


    # 변환값
    _matrix7_2_shear_result = np.array([
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        ])

    for i in range (0, 4, 1):
        _matrix7_2_shear_result[i] = np.matmul(_matrix7_2_shear, _matrix7_2[i])
    print(_matrix7_2_shear_result)

    # 변환값
    _matrix7_2_shear_result_nonZ = np.array([
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        ])

    # 좌표계 변경
    for i in range (0, 4, 1):
        _matrix7_2_shear_result_nonZ[i] = (
            screenWidth/2 + _matrix7_2_shear_result[i][0],
            screenHeight/2 - _matrix7_2_shear_result[i][1]
        )

    # 선형 변환 실습 2-2
    pygame.draw.polygon(screen, (255, 0, 0), _matrix7_2_shear_result_nonZ)


    pygame.display.flip()
pygame.quit()