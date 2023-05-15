import pygame
import math

#브레젠험 알고리즘을 사용해서 선을 그리는 함수를 작성해보세요
#- input : surface, x1, y1, x2, y2, color
screenWidth = 1280
screenHeight = 720

# 좌표계 변경
def world_to_screen_coordinates(x, y):
    screen_x = math.ceil(screenWidth / 2 + x)
    screen_y = math.ceil(screenHeight / 2 - y)
    return (screen_x, screen_y)

def bresenham(surface, x1, y1, x2, y2, color):
    y = y1
    
    dx = x2 - x1
    dy = y2 - y1

    P = (-2 * dy) + dx

    for x in range(x1, x2 + 1):
        surface.set_at(world_to_screen_coordinates(x, y), color)

        if (P >= 0):
            P += (-2 * dy)
        else:
            y += 1
            P += (-2 * dy) + (2 * dx)
    return

pygame.init()

BACKGROUND_COLOR = (217, 217, 217)
LINE_COLOR = (200, 200, 200)
LINE_COLOR2 = (255, 0, 0)

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

    pygame.draw.line(screen, LINE_COLOR , (0, 360), (1280, 360), 2)
    pygame.draw.line(screen, LINE_COLOR , (640, 0), (640, 720), 2)
    bresenham(screen, 1, 3, 80, 70, LINE_COLOR2)

    pygame.display.flip()

pygame.quit()