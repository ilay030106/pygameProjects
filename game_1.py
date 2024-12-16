import random
import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ball Movement")

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

# Ball 1 position and speed
x_pos1 = WIDTH // 2
y_pos1 = HEIGHT // 2
speed_x1 = 5
speed_y1 = 5

# Ball 2 position and speed
x_pos2 = (WIDTH + 50) // 2
y_pos2 = (HEIGHT + 250) // 2
speed_x2 = 3
speed_y2 = 3

# Ball properties
radius = 10
REFRESH_RATE = 60

# Preload and scale background image
try:
    IMAGE = 'background_game_1.jpg'
    img = pygame.image.load(IMAGE)
    img = pygame.transform.scale(img, (WIDTH, HEIGHT))
except pygame.error:
    img = None

# Function to draw a circle
def drawing_circle(cord, radius1, color):
    pygame.draw.circle(screen, color, (cord[0], cord[1]), radius1)

# Main game loop
def run():
    global x_pos1, y_pos1, speed_x1, speed_y1
    global x_pos2, y_pos2, speed_x2, speed_y2

    finished = False

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        # Draw background
        if img:
            screen.blit(img, (0, 0))
        else:
            screen.fill(BLACK)

        x_pos1 += speed_x1
        y_pos1 += speed_y1
        if x_pos1 - radius <= 0 or x_pos1 + radius >= WIDTH:
            speed_x1 *= -1
        if y_pos1 - radius <= 0 or y_pos1 + radius >= HEIGHT:
            speed_y1 *= -1

        x_pos2 += speed_x2
        y_pos2 += speed_y2
        if x_pos2 - radius <= 0 or x_pos2 + radius >= WIDTH:
            speed_x2 *= -1
        if y_pos2 - radius <= 0 or y_pos2 + radius >= HEIGHT:
            speed_y2 *= -1

        # Check for collision between balls
        dist = ((x_pos1 - x_pos2) ** 2 + (y_pos1 - y_pos2) ** 2) ** 0.5
        if dist <= radius * 2:
            screen.fill(WHITE)
            try:
                go_IMG = 'game_over_pic.jpg'
                go_img = pygame.image.load(go_IMG)
                go_img = pygame.transform.scale(go_img, (WIDTH, HEIGHT))
                screen.blit(go_img, (0, 0))
            except pygame.error:
                pass
            pygame.display.flip()
            pygame.time.delay(10000)
            finished = True

        # Draw both balls
        drawing_circle((x_pos1, y_pos1), radius, RED)
        drawing_circle((x_pos2, y_pos2), radius, WHITE)

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(REFRESH_RATE)

    pygame.quit()

run()
