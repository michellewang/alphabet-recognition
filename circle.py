import pygame
from pygame import gfxdraw

WHITE = (255, 255, 255)

class Circle(pygame.sprite.Sprite):

    def __init__(self, pos, color, radius=20):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        pos = (int(pos[0]), int(pos[1]))
        self.image = pygame.Surface(pos)
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw
        pygame.gfxdraw.filled_circle(self.image, radius, radius, radius, color)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        # Store location
        self.prev = self.image.get_rect()

        self.traceOn = False
        self.radius = radius

    def toggleTrace(self):
        self.traceOn = not self.traceOn

    def getPos(self):
        return (self.rect.x, self.rect.y)

    def getPrev(self):
        print(self.prev.x, self.prev.y)
        return (self.prev.x, self.prev.y)

    def moveRight(self, pixels=5):
        self.prev.x = self.rect.x
        self.rect.x += pixels

    def moveLeft(self, pixels=5):
        self.prev.x = self.rect.x
        self.rect.x -= pixels

    def moveUp(self, pixels=5):
        self.prev.y = self.rect.y
        self.rect.y -= pixels

    def moveDown(self, pixels=5):
        self.prev.y = self.rect.y
        self.rect.y += pixels
