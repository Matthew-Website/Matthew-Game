import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Pac-Man setup
pacman_radius = 12
pacman_x = 1 * CELL_SIZE + CELL_SIZE // 2
pacman_y = 1 * CELL_SIZE + CELL_SIZE // 2
pacman_speed = 3
direction = pygame.Vector2(0, 0)

# Simple Maze Layout (1 = wall, 0 = empty)
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# Place dots (1 = dot)
dots = [[1 if cell == 0 else 0 for cell in row] for row in maze]

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = pygame.Vector2(-1, 0)
    elif keys[pygame.K_RIGHT]:
        direction = pygame.Vector2(1, 0)
    elif keys[pygame.K_UP]:
        direction = pygame.Vector2(0, -1)
    elif keys[pygame.K_DOWN]:
        direction = pygame.Vector2(0, 1)

    # Calculate new position
    new_x = pacman_x + direction.x * pacman_speed
    new_y = pacman_y + direction.y * pacman_speed

    # Wall collision
    grid_x = int(new_x // CELL_SIZE)
    grid_y = int(new_y // CELL_SIZE)
    if maze[grid_y][grid_x] == 0:
        pacman_x, pacman_y = new_x, new_y

    # Dot collection
    current_cell_x = int(pacman_x // CELL_SIZE)
    current_cell_y = int(pacman_y // CELL_SIZE)
    if dots[current_cell_y][current_cell_x] == 1:
        dots[current_cell_y][current_cell_x] = 0

    # Draw maze
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw dots
    for y in range(len(dots)):
        for x in range(len(dots[0])):
            if dots[y][x] == 1:
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 3)

    # Draw Pac-Man
    pygame.draw.circle(screen, GREEN, (int(pacman_x), int(pacman_y)), pacman_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
