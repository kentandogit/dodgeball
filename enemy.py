import pygame


class Enemy:
    velSpeed = 10
    dashSpeed = 20

    def __init__(self, x, y, radius, winWidth, winHeight, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = self.velSpeed
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.direction = direction
        self.deleteMe = False
        self.hitbox = (self.x - radius, self.y - radius, radius * 2, radius * 2)

    def move(self):
        if self.direction == 'down':
            self.moveDown()
        if self.direction == 'up':
            self.moveUp()
        if self.direction == 'left':
            self.moveLeft()
        if self.direction == 'right':
            self.moveRight()
        self.updateHitBox()


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

    def draw(self, win, player):
        self.move()
        colition = self.checkColition(player)
        if colition:
            player.collide()
        pygame.draw.circle(win, (0, 0, 255), (self.x, self.y), self.radius)
        #pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)