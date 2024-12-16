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

# צבעים נפוצים לשימוש
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
REFRESH_RATE = 60  # קצב רענון המסך בפריימים לשנייה

clock = pygame.time.Clock()  # יצירת שעון לניהול קצב הרענון

# הגדרת נתיבי הקבצים לתמונות
IMAGE = 'background_game_1.jpg'  # קובץ הרקע
PLAYER_IMG = 'superman_avatar.png'  # קובץ תמונת האווטאר

# טעינת תמונת הרקע והתאמתה לגודל המסך
img = pygame.image.load(IMAGE)  # טעינת תמונת הרקע
img = pygame.transform.scale(img, (WIDTH, HEIGHT))  # שינוי גודל התמונה כך שתתאים למסך

# טעינת תמונת האווטאר והגדרת רקע שקוף
player_img = pygame.image.load(PLAYER_IMG)
player_img = pygame.transform.scale(player_img, (85, 110))  # הקטנה גודל האווטאר
player_img = pygame.transform.flip(player_img, True, False)  # היפוך התמונה מימין לשמאל
avatar_image = Image.open(PLAYER_IMG)  # פתיחת הקובץ באמצעות PIL כדי לקרוא צבע פיקסל
background_ava = avatar_image.getpixel((0, 0))  # דגימת צבע הפיקסל מהפינה השמאלית העליונה
player_img.set_colorkey(background_ava)  # הפיכת צבע הרקע לתמונה שקוף


# הגדרת לחצני העכבר
LEFT = 1  # לחצן שמאלי
SCROLL = 2  # גלגלת
RIGHT = 3  # לחצן ימני

# רשימה לשמירת מיקומי לחיצות העכבר
mouse_pos_list = []
finished = False  # משתנה לשליטה בלולאה הראשית
addSound = "auughhh(Cutted).mp3"
clearSound = "get-out-sound-effect.mp3"

# לולאה ראשית של המשחק
while not finished:
    # אירועים במערכת (קלטים)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # יציאה מהמשחק כאשר סוגרים את החלון
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:  # לחיצה על כפתור שמאלי בעכבר
            screen.blit(player_img,pygame.mouse.get_pos())# הוספת האוואטר למסך
            pygame.display.flip()  # רענון המסך להצגת השינויים
            mouse_pos_list.append(pygame.mouse.get_pos())# הוספת מיקום הלחיצה לרשימה
            pygame.mixer.music.load(addSound)
            pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # בדיקה אם מקש רווח נלחץ
            mouse_pos_list = []  # איפוס רשימת המיקומים
            screen.blit(img, (0, 0))  # ציור מחדש של הרקע
            pygame.display.flip()  # רענון המסך
            mouse_point = pygame.mouse.get_pos()  # קבלת מיקום נוכחי של העכבר
            screen.blit(player_img, mouse_point)  # הצגת האווטאר במיקום של העכבר
            pygame.display.flip()# רענון המסך
            pygame.mixer.music.load(clearSound)
            pygame.mixer.music.play()


    # הצגת הרקע על המסך
    screen.blit(img, (0, 0))  # הצגת תמונת הרקע על המסך
    for pos in mouse_pos_list:#הצגת הדמויות
        screen.blit(player_img, pos)
    # הצגת האווטאר במיקום של סמן העכבר
    mouse_point = pygame.mouse.get_pos()  # קבלת מיקום נוכחי של העכבר
    screen.blit(player_img, mouse_point)  # הצגת האווטאר במיקום של העכבר

    pygame.display.flip()  # רענון המסך להצגת השינויים
    clock.tick(REFRESH_RATE)  # הגבלת קצב הרענון למספר פריימים לשנייה

pygame.quit()  # סגירת pygame לאחר סיום הלולאה
