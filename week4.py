import pygame

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

    pygame.display.flip()
pygame.quit()