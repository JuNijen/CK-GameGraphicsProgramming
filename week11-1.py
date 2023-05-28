import pygame
import numpy as np

#브레젠험 알고리즘을 사용해서 선을 그리는 함수를 작성해보세요
#- input : surface, x1, y1, x2, y2, color
screenWidth = 1280
screenHeight = 720
cameraX = 20
cameraY = 20
 

# 좌표계 변경
def world_to_view_coordinates(x, y):
    vertex_world = np.array([
        (x),
        (y),
        (1)
    ])
    view_matrix = np.array([
        (1, 0, -cameraX),
        (0, 1, -cameraY),
        (0, 0, 1),
    ])
    vertex_world = np.matmul(view_matrix, vertex_world)
    
    return (vertex_world[0], vertex_world[1])

# 좌표계 변경
def world_to_screen_coordinates(x, y):
    screen_x = round(screenWidth / 2 + x)
    screen_y = round(screenHeight / 2 - y)
    return (screen_x, screen_y)

def bresenham(surface, x1, y1, x2, y2, color):  
    x = round(x1)
    y = round(y1)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1


    if(dx >= dy):
        P = (-2 * dy) + dx
        for x in range(round(x1), round(x2 + 1)):
            wX, wY = world_to_screen_coordinates(x, y)
            vX, vY = world_to_view_coordinates(wX, wY)
            surface.set_at((vX, vY), color)

            if (P >= 0):
                P += (-2 * dy)
            else:
                y += sy
                P += (-2 * dy) + (2 * dx)
    else:
        P = (-2 * dx) + dy
        for y in range(round(y1), round(y2 + 1)):
            wX, wY = world_to_screen_coordinates(x, y)
            vX, vY = world_to_view_coordinates(wX, wY)
            surface.set_at((vX, vY), color)

            if (P >= 0):
                P += (-2 * dx)
            else:
                x += sx
                P += (-2 * dx) + (2 * dy)
    return

def square(surface, vertices, color1, color2):
    squarePoints = [(vertices[0][0], vertices[0][1]), (vertices[1][0], vertices[1][1]), (vertices[2][0], vertices[2][1]), (vertices[3][0], vertices[3][1])]

    scanline(surface, squarePoints, color1)

    bresenham(surface, vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1], color2)
    bresenham(surface, vertices[1][0], vertices[1][1], vertices[2][0], vertices[2][1], color2)
    bresenham(surface, vertices[2][0], vertices[2][1], vertices[3][0], vertices[3][1], color2)
    bresenham(surface, vertices[3][0], vertices[3][1], vertices[0][0], vertices[0][1], color2)

    return

def scanline(surface, vertices, color):
    vertices.sort(key = lambda x : x[1])

    start = vertices[0]
    end = vertices[3]

    for y in range(start[1], end[1] + 1):
        rightX = end[0]
        leftX = start[0]

        bresenham(surface, leftX, y, rightX, y, color)
    return


pygame.init()

BACKGROUND_COLOR = (217, 217, 217)
LINE_COLOR = (200, 200, 200)
LINE_COLOR2 = (100, 100, 100)
COLOR_RED = (255, 0, 0)

screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Graphics Programming")
running = True;

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_UP]:
            cameraY = cameraY + 10
            print("up")
        if key_input[pygame.K_LEFT]:
            cameraX = cameraX + 10
            print("left")
        if key_input[pygame.K_DOWN]:
            cameraY = cameraY - 10
            print("down")
        if key_input[pygame.K_RIGHT]:
            cameraX = cameraX - 10
            print("right")

    screen.fill(BACKGROUND_COLOR)

    for x in range (0, 720, 10):
        pygame.draw.line(screen, LINE_COLOR , world_to_view_coordinates(0, x), world_to_view_coordinates(1280, x), 1)

    for y in range (0, 1280, 10):
        pygame.draw.line(screen, LINE_COLOR , world_to_view_coordinates(y, 0), world_to_view_coordinates(y, 720), 1)

    pygame.draw.line(screen, LINE_COLOR2 , (0, 360), (1280, 360), 2)
    pygame.draw.line(screen, LINE_COLOR2 , (640, 0), (640, 720), 2)

    rectanglePoints1 = ((-50, -50),(-50, 50), (50, 50), (50, -50))
    rectanglePoints2 = ((250, 300), (250, 400), (350, 400), (350, 300))
    rectanglePoints3 = ((-350, 250), (-350, 350), (-250, 350), (-250, 250))

    square(screen, rectanglePoints1, COLOR_RED, BACKGROUND_COLOR)
    square(screen, rectanglePoints2, COLOR_RED, BACKGROUND_COLOR)
    square(screen, rectanglePoints3, COLOR_RED, BACKGROUND_COLOR)

    # screen.onkeypress(left, "a")
    # screen.onkeypress(right, "d")
    # screen.onkeypress(up, "w")
    # screen.onkeypress(down, "s")
    # screen.listen()

    pygame.display.flip()

pygame.quit()