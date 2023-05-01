def world_to_screen_coordinates(world_coordinates, screen_width, screen_height):
    screen_coordinates = []

    for coord in world_coordinates:
        x, y = coord
        screen_x = screen_width / 2 +x
        screen_y = screen_height/ 2 - y
        screen_coordinates.append((screen_x, screen_y))
    return screen_coordinates

screen_width = 800
screen_height = 600

world_coordinates = [ 
    (-100, 100), 
    (-50, 50),
    (0, 0),
    (50, 50),
    (100, 100),
    (-100, -100),
    (-50, -50),
    (0, -50),
    (50, -50),
    (100, -100)
]
screen_coordinates = world_to_screen_coordinates(
    world_coordinates,
    screen_width, screen_height
)

print(screen_coordinates)