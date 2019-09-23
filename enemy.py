import pygame


class Enemy:
    velSpeed = 5
    dashSpeed = 10

    def __init__(self, x, y, radius, winWidth, winHeight, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = self.velSpeed
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.direction = direction
        self.spriteRow = 0
        self.spriteCol = 0
        self.moveCount = 0
        self.deleteMe = False
        self.hitbox = (self.x - radius, self.y - radius, radius * 2, radius * 2)

    def move(self):
        if self.direction == 'down':
            self.spriteRow = 6
            self.moveDown()
        if self.direction == 'up':
            self.spriteRow = 2
            self.moveUp()
        if self.direction == 'left':
            self.spriteRow = 0
            self.moveLeft()
        if self.direction == 'right':
            self.spriteRow = 4
            self.moveRight()
        self.updateHitBox()
        if self.moveCount >= 23:
            self.moveCount = 0
        else:
            self.moveCount += 1

    def dash(self):
        self.vel = self.dashSpeed

    def moveUp(self):
        if (self.y - self.radius) - self.vel > 0:
            self.y -= self.vel
        else:
            self.delete()

    def moveDown(self):
        if self.y + self.radius + self.vel < self.winHeight:
            self.y += self.vel
        else:
            self.delete()

    def moveRight(self):
        if self.x + self.radius + self.vel < self.winWidth:
            self.x += self.vel
        else:
            self.delete()

    def moveLeft(self):
        if (self.x - self.radius) - self.vel > 0:
            self.x -= self.vel
        else:
            self.delete()
    def delete(self):
        self.deleteMe = True

    def checkColition(self, player):
        if (self.x - self.radius) > (player.x + player.radius) or (player.x - player.radius) > (self.x + self.radius):
            return False
        if (self.y - self.radius) > (player.y + player.radius) or (player.y - player.radius) > (self.y + self.radius):
            return False
        return True
    def updateHitBox(self):
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, win, player, enemySprites):
        self.move()
        colition = self.checkColition(player)
        if colition:
            player.collide()
        #circle = pygame.draw.circle(win, (0, 0, 255), (self.x, self.y), self.radius)
        win.blit(pygame.transform.scale(enemySprites.sprites[self.spriteRow][self.moveCount // 3], (self.radius * 2, self.radius * 2)), (self.x - self.radius, self.y - self.radius))
        #pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)