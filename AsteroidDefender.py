import pygame
import random


def message(msg, screen, bg_color, msg_color, loc, font_size):  # bg = background
    message_font = pygame.font.SysFont("Arial", font_size)
    message_text = message_font.render(msg, False, msg_color)
    for i in range(3200):
        screen.fill(bg_color)
        screen.blit(message_text, loc)
        pygame.display.update()


def x_checker(start, end, current_x):
    if start <= current_x and end >= current_x:
        return True
    else:
        return False


def y_checker(start, end, current_y):
    if start <= current_y and end >= current_y:
        return True
    else:
        return False


def rect_hitbox(start_x, end_x, start_y, end_y, target_x, target_y, mode, game_screen):
    mode = int(mode)
    if mode == 1:
        # filled
        pygame.draw.rect(game_screen, (255, 255, 255), (start_x, start_y, (end_x - start_x), (end_y - start_y)), 0)
    elif mode == 2:
        # not filled
        pygame.draw.rect(game_screen, (255, 255, 255), (start_x, start_y, (end_x - start_x), (end_y - start_y)), 1)

    if x_checker(start_x, end_x, target_x) and y_checker(start_y, end_y, target_y):
        return True
    else:
        return False


pygame.init()

char_x = 30
char_y = 500
char_width = 20
char_length = 15
speed = 3
changeX = 0

lifes = 3

score = 0

# gun barrel
barrel_width = 6
barrel_length = 8
barrelX = char_x + (char_width / 2 - barrel_width / 2)
barrelY = char_y - barrel_length

# bullet
spawn_pointX = barrelX + barrel_width / 2
spawn_pointY = barrelY
bulletX = 0
bulletY = 0
bullet_centerX = bulletX + (4 / 2)
bullet_centerY = bulletY + (4 / 2)

# bullet2
spawn_pointX2 = barrelX + barrel_width / 2
spawn_pointY2 = barrelY
bulletX2 = 0
bulletY2 = 0
bullet_centerX2 = bulletX2 + (4 / 2)
bullet_centerY2 = bulletY2 + (4 / 2)

# asteroid
asteroidX = random.randint(30, 465)
asteroidY = 15
ast_rad = 6
ast_centerX = asteroidX + (ast_rad / 2)
ast_centerY = asteroidY + (ast_rad / 2)
asteroid = False

gravity = 2

# colors
light_green = (99, 255, 45)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
coin_color = (255, 212, 15)

window = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Asteroid Defender")
clock = pygame.time.Clock()
run = True
fire = False
fired = False
fire2 = False
fired2 = False
life_mod = False

while run is True:
    font1 = pygame.font.SysFont("Arial", 10)
    text1 = font1.render("Score: {0}".format(score), False, white)
    text2 = font1.render("Life: {0}".format(life_mod), False, white)
    text3 = font1.render("X: {0}".format(char_x), False, white)
    text4 = font1.render("Y: {0}".format(char_y), False, white)
    text5 = font1.render("Barrel X: {0}".format(barrelX), False, white)
    text6 = font1.render("Barrel Y: {0}".format(barrelY), False, white)

    font3 = pygame.font.SysFont("Arial", 12)
    text7 = font3.render("SPACE to fire | A/D to move | F to open life mod | E to close life mod", False, black)

    # just to make sure it runs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # print(event)

        # controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                changeX = -1 * speed
            if event.key == pygame.K_d:
                changeX = speed

            if event.key == pygame.K_SPACE and fire is False and fired is False:
                fire = True
            if event.key == pygame.K_SPACE and fired is True and fire2 is False and fired2 is False:
                fire2 = True

            if event.key == pygame.K_ESCAPE:
                quit()
            if event.key == pygame.K_f:
                life_mod = True
            if event.key == pygame.K_e:
                life_mod = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                changeX = 0

    if score > 4 and gravity < 4 and score % 3 == 0:
        gravity = score / 3

    asteroidY += gravity
    ast_centerX = asteroidX + (ast_rad / 2)
    ast_centerY = asteroidY + (ast_rad / 2)

    # displaying
    window.fill(black)
    window.blit(text1, (430, 0))
    window.blit(text2, (430, 10))
    window.blit(text3, (430, 20))
    window.blit(text4, (430, 30))
    window.blit(text5, (430, 40))
    window.blit(text6, (430, 50))

    # bullet
    if fire is True:
        spawn_pointX = barrelX + barrel_width / 2
        spawn_pointY = barrelY
        pygame.draw.circle(window, red, (int(spawn_pointX), int(spawn_pointY)), 4, 0)
        bulletX = spawn_pointX
        bulletY = spawn_pointY
        fire = False
        fired = True

    if fired is True:
        bulletY -= 5
        bullet_centerX = bulletX + (4 / 2)
        bullet_centerY = bulletY + (4 / 2)
        pygame.draw.circle(window, red, (int(bulletX), int(bulletY)), 4, 0)

    if fire2 is True:
        spawn_pointX2 = barrelX + barrel_width / 2
        spawn_pointY2 = barrelY
        pygame.draw.circle(window, red, (int(spawn_pointX2), int(spawn_pointY2)), 4, 0)
        bulletX2 = spawn_pointX2
        bulletY2 = spawn_pointY2
        fire2 = False
        fired2 = True

    if fired2 is True:
        bulletY2 -= 5
        bullet_centerX2 = bulletX2 + (4 / 2)
        bullet_centerY2 = bulletY2 + (4 / 2)
        pygame.draw.circle(window, red, (int(bulletX2), int(bulletY2)), 4, 0)

    # character
    if x_checker(0, 480, char_x):
        char_x += changeX
        barrelX += changeX

    if char_x > 480:
        char_x = 480
    if char_x < 0:
        char_x = 0
    if barrelX > 487:
        barrelX = 487
    if barrelX < 7:
        barrelX = 7

    pygame.draw.rect(window, white, (char_x, char_y, char_width, char_length), 0)
    pygame.draw.rect(window, white, (barrelX, barrelY, barrel_width, barrel_length), 0)

    # skybox
    if rect_hitbox(0, 500, 525, 600, ast_centerX, ast_centerY, 1, window)\
            and asteroid is False:
        score -= 1
        asteroid = True
        if life_mod is True:
            lifes -= 1

    if rect_hitbox(0, 500, 0, 5, bulletX, bulletY, 0, window)\
            and fired is True:
        fired = False
    if rect_hitbox(0, 500, 0, 5, bulletX2, bulletY2, 0, window)\
            and fired2 is True:
        fired2 = False

    # asteroids
    if asteroid is True:
        asteroidX = random.randint(30, 465)
        asteroidY = 15
        ast_rad = 6
        ast_centerX = asteroidX + (ast_rad / 2)
        ast_centerY = asteroidY + (ast_rad / 2)
        asteroid = False

    if rect_hitbox(asteroidX - 9, asteroidX + 10, asteroidY - 6, asteroidY + 6, bullet_centerX, bullet_centerY, 0, window)\
            and asteroid is False:
        score += 1
        asteroid = True
    if rect_hitbox(asteroidX - 9, asteroidX + 10, asteroidY - 6, asteroidY + 6, bullet_centerX2, bullet_centerY2, 0, window)\
            and asteroid is False:
        score += 1
        asteroid = True

    pygame.draw.circle(window, white, (int(asteroidX), int(asteroidY)), ast_rad, 1)

    # lifes
    if lifes == 3:
        pygame.draw.rect(window, light_green, (20, 550, 10, 10), 0)
        pygame.draw.rect(window, light_green, (40, 550, 10, 10), 0)
        pygame.draw.rect(window, light_green, (60, 550, 10, 10), 0)
    if lifes == 2:
        pygame.draw.rect(window, light_green, (20, 550, 10, 10), 0)
        pygame.draw.rect(window, light_green, (40, 550, 10, 10), 0)
    if lifes == 1:
        pygame.draw.rect(window, light_green, (20, 550, 10, 10), 0)
    if lifes == 0:
        run = False

    window.blit(text7, (100, 540))
    # print("X:", x_checker(char_x, (char_x + char_width), 100))
    # print("Y:", y_checker(char_y, (char_y + char_length), 100))

    pygame.display.update()
    clock.tick(60)
for i in range(800):
    if lifes < 1:
        window.fill(black)
        font2 = pygame.font.SysFont("Arial", 50)
        text8 = font2.render("GAME OVER", False, red)
        window.blit(text8, (110, 300))
        pygame.display.update()
pygame.quit()
quit()
