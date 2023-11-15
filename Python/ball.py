import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Stickman position and size
stickman_x, stickman_y = 100, HEIGHT - 100
stickman_size = 40

# Ball position and size
ball_x, ball_y = 300, HEIGHT - 100
ball_size = 20

# Goal post dimensions
goal_width = 100
goal_height = 50
goal_x = WIDTH - goal_width
goal_y = 0

# Ball velocity
ball_velocity = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stick-man Kicking a Ball")

def draw_stickman(x, y, size):
    # Draw the stickman
    pygame.draw.circle(screen, BLUE, (x, y - size), size)  # Head
    pygame.draw.line(screen, BLUE, (x, y), (x, y - size), 2)  # Body
    pygame.draw.line(screen, BLUE, (x, y - size), (x - size, y - 2 * size), 2)  # Left leg
    pygame.draw.line(screen, BLUE, (x, y - size), (x + size, y - 2 * size), 2)  # Right leg
    pygame.draw.line(screen, BLUE, (x, y - 2 * size), (x - size, y - 3 * size), 2)  # Left arm
    pygame.draw.line(screen, BLUE, (x, y - 2 * size), (x + size, y - 3 * size), 2)  # Right arm

def draw_goal_post():
    # Draw the goal post
    pygame.draw.rect(screen, RED, (goal_x, goal_y, goal_width, goal_height))

def main():
    clock = pygame.time.Clock()

    ball_kicked = False

    while not ball_kicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Kick the ball
        ball_x += ball_velocity
        if ball_x >= goal_x - ball_size:
            ball_kicked = True

        # Clear the screen
        screen.fill(WHITE)

        # Draw the stickman
        draw_stickman(stickman_x, stickman_y, stickman_size)

        # Draw the ball
        pygame.draw.circle(screen, GREEN, (ball_x, ball_y), ball_size)

        # Draw the goal post
        draw_goal_post()

        pygame.display.flip()
        clock.tick(60)

    # Wait for a few seconds and then quit
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
