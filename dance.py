import pygame
from PIL import Image

class dancer:
    def __init__(self,gender):
        if gender==1:
            PLAYER_IMG = 'female_dancer.png'
            player_img = pygame.image.load(PLAYER_IMG)

        else:
            PLAYER_IMG = 'male_dancer.png'
            player_img = pygame.image.load(PLAYER_IMG)
            player_img = pygame.transform.flip(player_img, True, False)  # היפוך התמונה מימין לשמאל
        player_img = pygame.transform.scale(player_img, (85, 110))  # הקטנה גודל האווטאר
        avatar_image = Image.open(PLAYER_IMG)  # פתיחת הקובץ באמצעות PIL כדי לקרוא צבע פיקסל
        background_ava = avatar_image.getpixel((0, 0))  # דגימת צבע הפיקסל מהפינה השמאלית העליונה
        player_img.set_colorkey(background_ava)  # הפיכת צבע הרקע לתמונה שקוף



