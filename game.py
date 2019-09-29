# import the pygame module, so you can use it
import pygame
from pygame.locals import *

import math
import numpy as np

SQUARE_SIZE = 20
N_PIXELS = 28

SPEED = 5

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK = (  0,   0,  0)
(width, height) = (SQUARE_SIZE*N_PIXELS, SQUARE_SIZE*N_PIXELS)

collision = False

# define a main function
def main():

    global running, screen
    # global x1,x2,y1,y2

    global lefthand, righthand
    global radius
    radius = 20

    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("ImplementAI")

    # create a surface on screen
    screen = pygame.display.set_mode((width, height))

    # set up first frame
    lefthand = {'x':(1/3)*width, 'y':height/2, 'prev':((1/3)*width, height/2), 'on':False}
    righthand = {'x':(2/3)*width, 'y':height/2, 'prev':((2/3)*width, height/2), 'on':False}
    updateHands()

    # main loop
    running = True
    while running:

        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            righthand['y'] -= SPEED
        if keys[pygame.K_DOWN]:
            righthand['y'] += SPEED
        if keys[pygame.K_RIGHT]:
            righthand['x'] += SPEED
        if keys[pygame.K_LEFT]:
            righthand['x'] -= SPEED
        if keys[pygame.K_w]:
            lefthand['y'] -= SPEED
        if keys[pygame.K_s]:
            lefthand['y'] += SPEED
        if keys[pygame.K_d]:
            lefthand['x'] += SPEED
        if keys[pygame.K_a]:
            lefthand['x'] -= SPEED
        collisionDetection()
        updateHands()

def collisionDetection():
    global collision
    distance = math.sqrt((lefthand['x']-righthand['x'])**2 + (lefthand['y']-righthand['y'])**2)
    if distance <= radius*2:
        if not collision:
            collision = True
            righthand['on'] = not righthand['on']
    else:
        if collision:
            collision = False

def updateHands():

    if not lefthand['on']:
        drawCircle(BLACK, (lefthand['prev']))

    if not righthand['on']:
        drawCircle(BLACK, (righthand['prev']))

    drawCircle(BLUE, (lefthand['x'], lefthand['y']))
    drawCircle(RED, (righthand['x'], righthand['y']))

    lefthand['prev'] = (lefthand['x'], lefthand['y'])
    righthand['prev'] = (righthand['x'], righthand['y'])

    pygame.display.update()

def drawCircle(color, position):
    position = (int(position[0]), int(position[1]))
    pygame.draw.circle(screen, color, position, radius)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
