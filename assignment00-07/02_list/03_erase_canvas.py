import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BG = (200, 200, 200)

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eraser on Canvas")

# Grid initialization
grid = [[BLUE for _ in range(COLS)] for _ in range(ROWS)]

eraser_size = 40
running = True  # Fixed typo: 'runing' -> 'running'

while running:
    screen.fill(BG)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser_rect = pygame.Rect(mouse_x - eraser_size // 2, mouse_y - eraser_size // 2, eraser_size, eraser_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(ROWS):
        for col in range(COLS):
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            # Erase cell if eraser is over it and mouse is pressed
            if eraser_rect.colliderect(cell_rect) and pygame.mouse.get_pressed()[0]:
                grid[row][col] = WHITE

            # Draw cell
            pygame.draw.rect(screen, grid[row][col], cell_rect)
            pygame.draw.rect(screen, (0, 0, 0), cell_rect, 1)

    # Draw the eraser outline
    pygame.draw.rect(screen, WHITE, eraser_rect, 2)

    pygame.display.flip()

pygame.quit()
