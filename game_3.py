import pygame
from PIL import Image

# הגדרת רוחב וגובה המסך
WIDTH = 800
HEIGHT = 600

# אתחול pygame והגדרת המסך
pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(True)  # הצגת סמן העכבר
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
PLAYER_IMG1 = 'superman_avatar.png'  # קובץ תמונת האווטאר
PLAYER_IMG2 = 'ironman_avatar.png'  # קובץ תמונת האווטאר

# טעינת תמונת הרקע והתאמתה לגודל המסך
img = pygame.image.load(IMAGE)
img = pygame.transform.scale(img, (WIDTH, HEIGHT))

# טעינת תמונת האווטאר 1
player_img1 = pygame.image.load(PLAYER_IMG1)
player_img1 = pygame.transform.scale(player_img1, (85, 110))  # שינוי גודל האווטאר
player_img1.set_colorkey(player_img1.get_at((0, 0)))  # הסרת הרקע של האווטאר
player1_pos = [WIDTH // 4, HEIGHT // 2]  # מיקום התחלתי של שחקן 1

# טעינת תמונת האווטאר 2
player_img2 = pygame.image.load(PLAYER_IMG2)
player_img2 = pygame.transform.scale(player_img2, (85, 110))  # שינוי גודל האווטאר
player_img2 = pygame.transform.flip(player_img2, True, False)  # היפוך התמונה מימין לשמאל
player2_pos = [WIDTH * 3 // 4, HEIGHT // 2]  # מיקום התחלתי של שחקן 2

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
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (player1_pos[0] <= mouse_x <= player1_pos[0] + 85 and
                            player1_pos[1] <= mouse_y <= player1_pos[1] + 110):
                        mouse_pos_list.append((player1_pos[0], player1_pos[1], player_img1))
                        add_sound.play()  # הפעלת סאונד להוספה
                    elif (player2_pos[0] <= mouse_x <= player2_pos[0] + 85 and
                          player2_pos[1] <= mouse_y <= player2_pos[1] + 110):
                        mouse_pos_list.append((player2_pos[0], player2_pos[1], player_img2))
                        add_sound.play()  # הפעלת סאונד להוספה
                case RIGHT:  # לחיצה על כפתור ימני בעכבר
                    if not pygame.mixer.music.get_busy():  # הפעלת המוזיקה אם היא לא מנוגנת
                        pygame.mixer.music.load("bg_music_game3.mp3")  # טעינת מוזיקת הרקע
                        pygame.mixer.music.play(-1)  # הפעלת מוזיקת הרקע בלולאה אינסופית
                    else:  # עצירת המוזיקה אם היא כבר מנוגנת
                        pygame.mixer.music.stop()

        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_SPACE:# לחיצה על מקש רווח
                    mouse_pos_list = []  # איפוס רשימת מיקומי הלחיצות
                    screen.blit(img, (0, 0))  # ציור מחדש של הרקע
                    pygame.display.flip()  # רענון המסך
                    pygame.display.flip()  # רענון המסך
                    clear_sound.play()  # הפעלת סאונד לניקוי

                #תזוזת השחקן עם החצים
                case pygame.K_UP:
                    player1_pos[1] -= 10
                case pygame.K_DOWN:
                    player1_pos[1] += 10
                case pygame.K_LEFT:
                    player1_pos[0] -= 10
                case pygame.K_RIGHT:
                    player1_pos[0] += 10

                # תנועת שחקן 2 עם WASD
                case pygame.K_w:
                    player2_pos[1] -= 10
                case pygame.K_s:
                    player2_pos[1] += 10
                case pygame.K_a:
                    player2_pos[0] -= 10
                case pygame.K_d:
                    player2_pos[0] += 10

    # ציור הרקע והדמויות על המסך
    screen.blit(img, (0, 0))  # הצגת תמונת הרקע
    screen.blit(player_img1, player1_pos)  # הצגת אווטאר 1
    screen.blit(player_img2, player2_pos)  # הצגת אווטאר 2

    # הצגת האווטארים המוכפלים במיקומים שנלחצו
    for x, y, avatar in mouse_pos_list:
        screen.blit(avatar, (x, y))

    pygame.display.flip()  # רענון המסך להצגת השינויים
    clock.tick(REFRESH_RATE)  # הגבלת קצב הרענון

pygame.quit()  # סיום המשחק וסגירת pygame