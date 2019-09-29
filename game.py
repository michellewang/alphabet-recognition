# import the pygame module, so you can use it
import pygame
from pygame.locals import *

from circle import Circle
from ocr import ocr_core

import math

SPEED = 5

WHITE = (254, 254, 254)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
(width, height) = (500, 500)

collision = False

# define a main function
def main():

    global screen
    global trace_sprites
    global hands_sprites

    global word
    word = []

    radius = 20

    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("ImplementAI")

    # create a surface on screen
    screen = pygame.display.set_mode((width, height))
    screen.fill(WHITE)

    # set up first frame

    lefthand = Circle(((1/3)*width, height/2), BLUE)
    righthand = Circle(((2/3)*width, height/2), RED)

    #This will be a list that will contain all the sprites we intend to use in our game.
    hands_sprites = pygame.sprite.Group()
    trace_sprites = pygame.sprite.Group()

    # Add the car to the list of objects
    hands_sprites.add(lefthand)
    hands_sprites.add(righthand)

    # main loop
    running = True
    while running:

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                screenshot()
                guess()
                # change the value to False, to exit the main loop
                running = False

        updateTrace(righthand)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            righthand.moveUp()
        if keys[pygame.K_DOWN]:
            righthand.moveDown()
        if keys[pygame.K_RIGHT]:
            righthand.moveRight()
        if keys[pygame.K_LEFT]:
            righthand.moveLeft()
        if keys[pygame.K_w]:
            lefthand.moveUp()
        if keys[pygame.K_s]:
            lefthand.moveDown()
        if keys[pygame.K_d]:
            lefthand.moveRight()
        if keys[pygame.K_a]:
            lefthand.moveLeft()
        if keys[pygame.K_SPACE]:
            trace_sprites = pygame.sprite.Group()
        if keys[pygame.K_RETURN]:
            word.append(guess())
            print('word: ' + "".join(word))
        collisionDetection(lefthand, righthand)

        #Game Logic
        hands_sprites.update()
        trace_sprites.update()

        #Drawing on Screen
        screen.fill(WHITE)

        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        trace_sprites.draw(screen)
        hands_sprites.draw(screen)

        #Refresh Screen
        pygame.display.flip()

def collisionDetection(hand1, hand2):
    global collision
    x1 = hand1.rect.x
    x2 = hand2.rect.x
    y1 = hand1.rect.y
    y2 = hand2.rect.y

    max = hand1.radius + hand2.radius
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance <= max:
        if not collision:
            collision = True
            hand2.toggleTrace()
            if not hand2.traceOn:
                screenshot()
                guess()

    else:
        if collision:
            collision = False

def screenshot():
    #Game Logic
    hands_sprites.update()
    trace_sprites.update()

    #Drawing on Screen
    screen.fill(WHITE)

    #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    trace_sprites.draw(screen)

    #Refresh Screen
    pygame.display.flip()
    pygame.image.save(screen, 'screenshot.jpeg')

def guess():
    guess = ocr_core('screenshot.jpeg')
    print('guess: ' + guess)
    return guess

def updateTrace(hand):
    if hand.traceOn:
        newCircle = Circle(hand.getPos(), BLACK)
        trace_sprites.add(newCircle)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
