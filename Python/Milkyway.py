import pygame
import math

# Initialize Pygame
pygame.init()

# Window size
WIDTH = 800
HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Define the orbits
orbits = [
    {'radius': 100, 'speed': 0.01, 'color': BLUE},  # Mercury
    {'radius': 150, 'speed': 0.008, 'color': GREEN},  # Venus
    {'radius': 200, 'speed': 0.006, 'color': YELLOW},  # Earth
    {'radius': 250, 'speed': 0.005, 'color': YELLOW},  # Mars
    # Add more planets here
]

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Milky Way")

clock = pygame.time.Clock()

# Run the simulation
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(BLACK)

    # Draw the Milky Way
    pygame.draw.circle(window, BLACK, (WIDTH // 2, HEIGHT // 2), 100)

    # Calculate the current position of each planet and draw it
    for orbit in orbits:
        angle = pygame.time.get_ticks() * orbit['speed']  # Calculate the angle based on time
        x = int(WIDTH // 2 + orbit['radius'] * math.cos(angle))
        y = int(HEIGHT // 2 + orbit['radius'] * math.sin(angle))
        pygame.draw.circle(window, orbit['color'], (x, y), 10)

    pygame.display.flip()
    clock.tick(60)

# Quit the program
pygame.quit()
