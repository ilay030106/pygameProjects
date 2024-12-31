import pygame
from PIL import Image

class Dancer(pygame.sprite.Sprite):
    def __init__(self,gender="M",x=0,y=0,veloX=3):
        super(Dancer,self).__init__()
        if gender.equals("w") or gender.equals("W"):
            PLAYER_IMG = 'female_dancer.png'
            self.player_img = pygame.image.load(PLAYER_IMG).convert_alpha()

        else:
            PLAYER_IMG = 'male_dancer.png'
            self.player_img = pygame.image.load(PLAYER_IMG).convert_alpha()
            self.player_img = pygame.transform.flip(self.player_img, True, False)  # היפוך התמונה מימין לשמאל
        avatar_image = Image.open(PLAYER_IMG)  # פתיחת הקובץ באמצעות PIL כדי לקרוא צבע פיקסל
        self.player_img.set_colorkey(avatar_image.getpixel((0, 0)))  # הפיכת צבע הרקע לתמונה שקוף
        self.rect = self.player_img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = veloX

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def scale(self, width=85, height=110):
        self.player_img = pygame.transform.scale(self.player_img, (width, height))
        self.rect = self.image.get_rect(center=self.rect.center)

    def rotate(self, angle):
        self.player_img = pygame.transform.rotate(self.player_img, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    def update_v(self, vx):
        self.__vx = vx

    def update_loc(self):
        self.rect.x += self.__vx

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.__vx, self.__vy


WIDTH = 800
HEIGHT = 600


pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(True)  # הצגת סמן העכבר
size = (WIDTH, HEIGHT)  # קביעת גודל המסך
screen = pygame.display.set_mode(size)  # יצירת המסך
pygame.display.set_caption("Mouse Avatar")  # כותרת חלון המשחק

IMAGE = 'dance_background.png'  # קובץ הרקע

# טעינת תמונת הרקע והתאמתה לגודל המסך
img = pygame.image.load(IMAGE)
img = pygame.transform.scale(img, (WIDTH, HEIGHT))
finished = False  # משתנה לשליטה בלולאת המשחק

#לולאת המשחק
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # יציאה מהמשחק
            finished = True
