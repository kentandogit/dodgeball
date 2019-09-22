import pygame
from player import Player
from enemy import Enemy
from random import randint, choice, randrange
from button import Button

pygame.init()

winWidth = 800
winHeight = 600
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Dodge Ball")
clock = pygame.time.Clock()


def reDrawGame():
    win.fill((0, 0, 0, 0))
    player.draw(win)
    for en in enemies:
        en.draw(win, player)
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
        enemyY = -20
        enemyX = randint(0, winWidth)
    if enemyDirection == "up":
        enemyY = winHeight + 20
        enemyX = randint(0, winWidth)
    if enemyDirection == "left":
        enemyY = randint(0, winHeight)
        enemyX = winWidth + 20
    if enemyDirection == "right":
        enemyY = randint(0, winHeight)
        enemyX = -20

    enemies.append(
        Enemy(enemyX, enemyY, 20, winWidth, winHeight, enemyDirection))

#MAIN LOOP STARTS HERE
run = True
player = Player(400, 300, 20, winWidth, winHeight)
enemies = []
enemy = Enemy(200, 200, 20, winWidth, winHeight, 'down')
enemies = [enemy]
numEnemies = 3
pygame.time.set_timer(pygame.USEREVENT+1, randrange(2000,5000))

def main():
    global run, player, enemies, numEnemies
    run = True
    player = Player(400, 300, 20, winWidth, winHeight)
    enemies = []
    numEnemies = 3
    while run:
        clock.tick(30)
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