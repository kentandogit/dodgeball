import pygame, os


class Sprite:

    spriteWidth = 0
    spriteHeight = 0

    def __init__(self, image, rows, columns):
        self.rows = rows
        self.columns = columns
        self.sprites = [[0 for x in range(columns)] for y in range(rows)]
        self.processSprites(image)
        #print(self.sprites)

    def processSprites(self, image):
        img = self.loadImage(image)
        self.spriteWidth = img.get_width() // self.columns
        self.spriteHeight = img.get_height() // self.rows

        y = 0
        for frameRows in range(self.rows):
            x = 0
            for frameCol in range(self.columns):
                frameSurf = pygame.Surface((self.spriteWidth, self.spriteHeight), pygame.SRCALPHA, 32)
                #frameSurf.fill((255,0,0))
                frameSurf.blit(img, (x, y))
                self.sprites[frameRows][frameCol] = frameSurf.copy()
                #self.sprites.append(frameSurf.copy())
                x -= self.spriteWidth
            y -= self.spriteHeight

    def loadImage(self, fileName, useColorKey=False):
        if os.path.isfile(fileName):
            image = pygame.image.load(fileName)
            image = image.convert_alpha()
            # Return the image
            return image
        else:
            raise Exception("Error loading image: " + fileName + " - Check filename and path?")
