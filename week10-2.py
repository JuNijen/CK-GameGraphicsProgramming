import pygame

#브레젠험 알고리즘을 사용해서 선을 그리는 함수를 작성해보세요
#- input : surface, x1, y1, x2, y2, color
screenWidth = 1280
screenHeight = 720

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
            surface.set_at(world_to_screen_coordinates(x, y), color)

            if (P >= 0):
                P += (-2 * dy)
            else:
                y += sy
                P += (-2 * dy) + (2 * dx)
    else:
        P = (-2 * dx) + dy
        for y in range(round(y1), round(y2 + 1)):
            surface.set_at(world_to_screen_coordinates(x, y), color)

            if (P >= 0):
                P += (-2 * dx)
            else:
                x += sx
                P += (-2 * dx) + (2 * dy)
    return

def triangle(surface, vertices, color1, color2):
    # bresenham(surface, 100, 50, 50, 200, color)
    # bresenham(surface, 50, 200, 150, 250, color)
    # bresenham(surface, 100, 50, 150, 250, color)
    
    trianglePoints = [(vertices[0][0], vertices[0][1]), (vertices[1][0], vertices[1][1]), (vertices[2][0], vertices[2][1])]
    scanline(surface, trianglePoints, color1)

    bresenham(surface, vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1], color2)
    bresenham(surface, vertices[1][0], vertices[1][1], vertices[2][0], vertices[2][1], color2)
    bresenham(surface, vertices[0][0], vertices[0][1], vertices[2][0], vertices[2][1], color2)

    return

def scanline(surface, vertices, color):
    vertices.sort(key = lambda x : x[1])

    start = vertices[0]
    second = vertices[1]
    end = vertices[2]

    a12 = (second[0] - start[0]) / (second[1] - start[1]) if (start[1] != second[1]) else 0
    a13 = (end[0] - start[0]) / (end[1] - start[1]) if (start[1] != second[1]) else 0
    a23 = (end[0] - second[0]) / (end[1] - second[1]) if (second[1] != end[1]) else 0

    for y in range(start[1], end[1] + 1):
        rightX = a13 * (y - start[1]) + start[0]
        leftX = 0

        if(y > second[1]):
            leftX = a23 * (y - second[1]) + second[0]
        else:
            leftX = a12 * (y - start[1]) + start[0]
        if(leftX > rightX):
            leftX, rightX = rightX, leftX

        bresenham(surface, leftX, y, rightX, y, color)
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

    trianglePoints1 = ((100, 50), (50, 200), (150, 250))
    trianglePoints2 = ((-150, 150), (100, 200), (150, 200))
    trianglePoints3 = ((0, -50), (-50, 150), (50, 150))

    triangle(screen, trianglePoints1, LINE_COLOR, LINE_COLOR2)
    triangle(screen, trianglePoints2, LINE_COLOR, LINE_COLOR2)
    triangle(screen, trianglePoints3, LINE_COLOR2, LINE_COLOR)

    pygame.display.flip()

pygame.quit()