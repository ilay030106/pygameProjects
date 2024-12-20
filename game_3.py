import pygame
from PIL import Image

# הגדרת רוחב וגובה המסך
WIDTH = 800
HEIGHT = 600

# אתחול pygame והגדרת המסך
pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)  # הסתרת סמן העכבר
size = (WIDTH, HEIGHT)  # קביעת גודל המסך
screen = pygame.display.set_mode(size)  # יצירת המסך
pygame.display.set_caption("Mouse Avatar")  # כותרת חלון המשחק

# צבעים
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
REFRESH_RATE = 60  # קצב רענון המסך בפריימים לשנייה

clock = pygame.time.Clock()  # שעון לניהול קצב הרענון

# טעינת תמונות
IMAGE = 'background_game_1.jpg'  # קובץ הרקע
PLAYER_IMG = 'superman_avatar.png'  # קובץ תמונת האווטאר

# טעינת תמונת הרקע והתאמתה לגודל המסך
img = pygame.image.load(IMAGE)
img = pygame.transform.scale(img, (WIDTH, HEIGHT))

# טעינת תמונת האווטאר
player_img = pygame.image.load(PLAYER_IMG)
player_img = pygame.transform.scale(player_img, (85, 110))  # שינוי גודל האווטאר
player_img = pygame.transform.flip(player_img, True, False)  # היפוך התמונה מימין לשמאל
avatar_image = Image.open(PLAYER_IMG)  # פתיחת התמונה באמצעות PIL
background_ava = avatar_image.getpixel((0, 0))  # דגימת צבע פיקסל מהפינה השמאלית העליונה
player_img.set_colorkey(background_ava)  # הפיכת צבע הרקע של האווטאר לשקוף

# טעינת קבצי סאונד
add_sound = pygame.mixer.Sound("auughhh(Cutted).mp3")  # סאונד להוספה
clear_sound = pygame.mixer.Sound("get-out-sound-effect.mp3")  # סאונד לניקוי

# הגדרת כפתורי העכבר
MOUSE_BUTTONS = (1, 2, 3)  # (LEFT, SCROLL, RIGHT)
LEFT, SCROLL, RIGHT = MOUSE_BUTTONS

# רשימת מיקומי לחיצות עכבר
mouse_pos_list = []
finished = False  # משתנה לשליטה בלולאת המשחק

# לולאת המשחק
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # יציאה מהמשחק
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            match event.button:
                case 1:  # לחיצה על כפתור שמאלי בעכבר
                    screen.blit(player_img, pygame.mouse.get_pos())  # הצגת האווטאר במיקום הלחיצה
                    pygame.display.flip()  # רענון המסך
                    mouse_pos_list.append(pygame.mouse.get_pos())  # הוספת מיקום הלחיצה לרשימה
                    add_sound.play()  # הפעלת סאונד להוספה
                case RIGHT:  # לחיצה על כפתור ימני בעכבר
                    if not pygame.mixer.music.get_busy():  # הפעלת המוזיקה אם היא לא מנוגנת
                        pygame.mixer.music.load("bg_music_game3.mp3")  # טעינת מוזיקת הרקע
                        pygame.mixer.music.play(-1)  # הפעלת מוזיקת הרקע בלולאה אינסופית
                    else:  # עצירת המוזיקה אם היא כבר מנוגנת
                        pygame.mixer.music.stop()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # לחיצה על מקש רווח
            mouse_pos_list = []  # איפוס רשימת מיקומי הלחיצות
            screen.blit(img, (0, 0))  # ציור מחדש של הרקע
            pygame.display.flip()  # רענון המסך
            mouse_point = pygame.mouse.get_pos()  # קבלת מיקום העכבר
            screen.blit(player_img, mouse_point)  # הצגת האווטאר במיקום הנוכחי של העכבר
            pygame.display.flip()  # רענון המסך
            clear_sound.play()  # הפעלת סאונד לניקוי

    # ציור הרקע והדמויות על המסך
    screen.blit(img, (0, 0))  # הצגת תמונת הרקע
    for pos in mouse_pos_list:  # הצגת האווטארים במיקומי הלחיצות
        screen.blit(player_img, pos)

    mouse_point = pygame.mouse.get_pos()  # קבלת מיקום העכבר
    screen.blit(player_img, mouse_point)  # הצגת האווטאר במיקום הנוכחי של העכבר

    pygame.display.flip()  # רענון המסך להצגת השינויים
    clock.tick(REFRESH_RATE)  # הגבלת קצב הרענון

pygame.quit()  # סיום המשחק וסגירת pygame
