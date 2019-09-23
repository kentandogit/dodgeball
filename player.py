import pygame


class Player:
    velSpeed = 5
    dashSpeed = 10
    alive = True

    def __init__(self, x, y, radius, winWidth, winHeight):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = self.velSpeed
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.hitbox = (self.x - radius, self.y - radius, radius * 2, radius * 2)

    def move(self, keys):
        if keys[pygame.K_SPACE]:
            self.dash()
        if keys[pygame.K_w]:
            self.moveUp()
        if keys[pygame.K_s]:
            self.moveDown()
        if keys[pygame.K_d]:
            self.moveRight()
        if keys[pygame.K_a]:
            self.moveLeft()
        self.vel = self.velSpeed
        self.updateHitBox()

    def updateHitBox(self):
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def dash(self):
        self.vel = self.dashSpeed
    def moveUp(self):
        if (self.y - self.radius) - self.vel > 0:
            self.y -= self.vel

    def moveDown(self):
        if self.y + self.radius + self.vel < self.winHeight:
            self.y += self.vel

    def moveRight(self):
        if self.x + self.radius + self.vel < self.winWidth:
            self.x += self.vel

    def moveLeft(self):
        if (self.x - self.radius) - self.vel > 0:
            self.x -= self.vel

    def collide(self):
        self.alive = False

    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.radius)
        #pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)