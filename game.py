# import the pygame module, so you can use it
import pygame
import numpy as np

SQUARE_SIZE = 20

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)
(width, height) = (SQUARE_SIZE*28, SQUARE_SIZE*28)

# define a main function
def main():

    global running, screen

    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("ImplementAI")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((width, height))

    # define a variable to control the main loop
    running = True

    # set up first frame
    pos1 = ((1/3)*width,height/2)
    drawCircle(BLUE, pos1)
    pos2 = ((2/3)*width,height/2)
    drawCircle(RED, pos2)
    pygame.display.update()

    # main loop
    while running:

        # event handling, gets all event from the event queue
        for event in pygame.event.get():



            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawCircle(color, position, radius=20):
    position = (int(position[0]), int(position[1]))
    pygame.draw.circle(screen, color, position, radius)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
