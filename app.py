import pygame
from player import Player
from enemy import Enemy
from random import randint, choice, randrange
from button import Button
from sprite import *

pygame.init()

winWidth = 800
winHeight = 600
playerSize = 16
enemySize = 32
bgY = 0
bgY2 = 0
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Dodge Ball")
clock = pygame.time.Clock()

enemySprites = Sprite("assets/fireball.png", 8, 8)
bgSprite = Sprite("assets/bg2.png", 1, 1)
bgSprite = bgSprite.sprites[0][0]
bgY2 = bgSprite.get_height()


def reDrawGame():
    global bgY, bgY2
    win.fill((0, 0, 0, 0))
    #win.blit(pygame.transform.scale(bgSprite.sprites[0][0],(winWidth,winHeight)), (0, 0))
    win.blit(bgSprite, (0, bgY))
    win.blit(bgSprite, (0, bgY2))
    bgY -= 1
    bgY2 -= 1
    if bgY < (bgSprite.get_height() * -1):
        bgY = bgSprite.get_height()
    if bgY2 < (bgSprite.get_height() * -1):
        bgY2 = bgSprite.get_height()
    player.draw(win)
    for en in enemies:
        en.draw(win, player, enemySprites)

    pygame.display.update()

def gameOver():
    #win.fill((0, 0, 0, 0))
    rec = win.get_rect()
    btnWidth = 100
    btnHeight = 50
    btn1 = Button('Try Again', rec.center[0] - (btnWidth//2), rec.center[1] - (btnHeight//2), 100, 50)
    btn2 = Button('Quit', rec.center[0] - (btnWidth//2), rec.center[1] - (btnHeight//2) + (btnHeight * 1.2), 100, 50)

    playAgain = False
    while not playAgain:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            btn1.handle_event(event)
            btn2.handle_event(event)
        btn1.update()
        btn2.update()
        btn1.draw(win)
        btn2.draw(win)
        pygame.display.update()
        if btn2.clicked or btn1.clicked:
            playAgain = True

    if btn2.clicked:
        pygame.quit()
    if btn1.clicked:
        main()

def generateEnemy():
    if len(enemies) > numEnemies:
        return True
    enemyDirection = choice(("up", "down", "left", "right"))
    enemyY = 0
    enemyX = 0
    if enemyDirection == "down":
        enemyY = -enemySize
        enemyX = randint(0, winWidth)
    if enemyDirection == "up":
        enemyY = winHeight + enemySize
        enemyX = randint(0, winWidth)
    if enemyDirection == "left":
        enemyY = randint(0, winHeight)
        enemyX = winWidth + enemySize
    if enemyDirection == "right":
        enemyY = randint(0, winHeight)
        enemyX = -enemySize

    enemies.append(
        Enemy(enemyX, enemyY, enemySize, winWidth, winHeight, enemyDirection))

#MAIN LOOP STARTS HERE

pygame.time.set_timer(pygame.USEREVENT+1, randrange(2000,5000))


def main():
    global run, player, enemies, numEnemies
    run = True
    player = Player(400, 300, playerSize, winWidth, winHeight)
    enemies = []
    numEnemies = 3
    while run:
        clock.tick(60)
        generateEnemy()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.USEREVENT+1:
                numEnemies += 1
        keys = pygame.key.get_pressed()
        player.move(keys)
        for en in enemies:
            if en.deleteMe:
                enemies.pop(enemies.index(en))
        if not player.alive:
            run = False
        reDrawGame()
    gameOver()

main()
#pygame.quit()