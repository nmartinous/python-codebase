'''
Creates an empty pygame window that can be used as a starting point for any project
'''

import pygame
import pygame as pg

# -------------------- WINDOW SET UP -------------------- #

# initialize pygame
pg.init()

# create screen with a 1280x720 resolution
screen = pg.display.set_mode((1280, 720))

# create a game clock
clock = pg.time.Clock()

# set running bool to true
running = True

# ------------------------------------------------------- #

# ---------------------- GAME LOOP ---------------------- #

# game loop
while running:

    # poll for events
    for event in pg.event.get():

        # the user clicks X to close the window
        if event.type == pygame.QUIT:

            # set running to false to end game loop
            running = False

    # fill the screen to wipe away last frame
    screen.fill("black")

    # -------------------- GAME RENDERING -------------------- #

    # -------------------------------------------------------- #

    # flip() display to put work on screen
    pg.display.flip()

    # limit fps to 60
    clock.tick(60)

# ------------------------------------------------------- #
