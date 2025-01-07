import pygame
from PIL import Image

class Dancer(pygame.sprite.Sprite):
    def __init__(self, gender="M", x=0, y=0, veloX=3):
        super(Dancer, self).__init__()
        if gender.lower() == "w":  # Fixed condition to use `.lower()` for case-insensitivity
            PLAYER_IMG = 'female_dancer.png'
        else:
            PLAYER_IMG = 'male_dancer.png'

        self.image = pygame.image.load(PLAYER_IMG).convert_alpha()  # Set self.image for rendering
        if gender.lower() != "w":  # Flip only for male dancers
            self.image = pygame.transform.flip(self.image, True, False)

        # Open image using PIL to get transparent background color
        avatar_image = Image.open(PLAYER_IMG)
        transparent_color = avatar_image.getpixel((0, 0))  # Get the pixel at (0, 0)
        self.image.set_colorkey(transparent_color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = veloX

    def update(self):
        self.rect.x += self.__vx

    def scale(self, width=85, height=110):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=self.rect.center)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update_v(self, vx):
        self.__vx = vx

    def update_loc(self):
        self.rect.x += self.__vx

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.__vx


# Constants for screen size
WIDTH = 800
HEIGHT = 600

# Initialize pygame
pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(True)  # Show mouse cursor
size = (WIDTH, HEIGHT)  # Screen size
screen = pygame.display.set_mode(size)  # Create screen
pygame.display.set_caption("Dance Floor")  # Game window title

# Load and scale the background image
IMAGE = 'dance_bg.png'
img = pygame.image.load(IMAGE).convert()
img = pygame.transform.scale(img, (WIDTH, HEIGHT))

# Create a Dancer instance
dancer = Dancer(gender="M", x=WIDTH // 2, y=HEIGHT // 2, veloX=3)
dancer.scale(100, 120)  # Scale dancer to appropriate size

# Sprite group for updating and drawing the dancer
all_sprites = pygame.sprite.Group()
all_sprites.add(dancer)

# Game loop control
finished = False

# Game loop
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exit game
            finished = True

    all_sprites.update()

    # Draw background and sprites
    screen.blit(img, (0, 0))  # Redraw the background
    all_sprites.draw(screen)

    pygame.display.flip()


    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
