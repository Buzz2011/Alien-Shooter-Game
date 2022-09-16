# This is a modified version of a game from a tutourial

# Importing Modules
import pygame
import math
import random

# Initialize
pygame.init()

clock = pygame.time.Clock()

# Screen
screen = pygame.display.set_mode((800, 600))

# background for game
bg = pygame.image.load('bgg.jpg')

# Caption And Icon
pygame.display.set_caption('Alien Shooter')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('rocket.png')
px = 370
py = 500
x_change = 0

# Alien
alienimg = pygame.image.load('alien.png')
ax = random.randint(4, 736)
ay = 45
ax_change = 0
ay_change = 0
pos_underlevel = False

# Other Alien
alien1img = pygame.image.load('alien1.png')
a1x = random.randint(4, 736)
a1y = 45
a1x_change = 0
a1y_change = 0
pos_underlevel = False

# Bullet
bulimg = pygame.image.load('bullet.png')
bulx = 0
buly = 480
bulx_change = 0
buly_change = 0.40
bul_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10

# Game Over
font2 = pygame.font.Font('freesansbold.ttf', 32)


def show_score(textx, texty):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (textx, texty))


def game_over():
    over = font2.render("GAME OVER, GOOD LUCK NEXT TIME:)",
                        True, (255, 255, 255))
    screen.blit(over, (100, 250))


def player(px, py):
    screen.blit(playerimg, (px, py))


def alien(ax, ay):
    screen.blit(alienimg, (ax, ay))


def alien1(a1x, a1y):
    screen.blit(alien1img, (a1x, a1y))


def fire_bullet(bulx, buly):
    global bul_state
    bul_state = "fire"
    screen.blit(bulimg, (bulx + 16, buly + 10))


def iscollision(ax, ay, bulx, buly):
    distance = math.sqrt((math.pow(ax - bulx, 2)) + (math.pow(ax - buly, 2)))
    if distance < 27:
        return True
    else:
        return False


def iscollision1(a1x, a1y, bulx, buly):
    distance1 = math.sqrt((math.pow(a1x - bulx, 2)) +
                          (math.pow(a1x - buly, 2)))
    if distance1 < 27:
        return True
    else:
        return False


# Main Loop
run = True
while run:

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # PLayer Movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -0.3
            if event.key == pygame.K_d:
                x_change = 0.3
            if event.key == pygame.K_LEFT:
                x_change = -0.3
            if event.key == pygame.K_RIGHT:
                x_change = 0.3
            if event.key == pygame.K_SPACE:
                if bul_state is "ready":
                    bulx = px
                    fire_bullet(bulx, buly)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0

    if px <= 0:
        px = 0
    elif px >= 736:
        px = 736

    # Alien Movements
    if run == True:
        ay_change = 0.06

    ax += ax_change
    ay += ay_change

    if run == True:
        a1y_change = 0.06

    a1x += a1x_change
    a1y += a1y_change

    # Game over
    if ay > 736 or 736 < 2:
        pos_underlevel = False

    if a1y > 736 or 736 < 2:
        pos_underlevel = False
        game_over()

    # Bullet Movement
    if buly <= 0:
        buly = 480
        bul_state = "ready"

    if bul_state is "fire":
        fire_bullet(bulx, buly)
        buly -= buly_change

    # Collision
    collision = iscollision(ax, ay, bulx, buly)
    if collision:
        buly = 480
        bul_state = "ready"
        score_value += 1
        ax = random.randint(4, 736)
        ay = 45

    collision1 = iscollision1(a1x, a1y, bulx, buly)
    if collision1:
        buly = 480
        bul_state = "ready"
        score_value += 1
        a1x = random.randint(4, 736)
        a1y = 45

    px += x_change
    player(px, py)
    alien(ax, ay)
    alien1(a1x, a1y)
    show_score(textx, texty)
    pygame.display.update()
