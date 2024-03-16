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

# create a delta time variable for use in framerate-independent physics
dt = 0

# set player position to the middle of the screen
player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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

    # draw a red circle with a radius of 40 to player_pos on screen to represent the player
    pg.draw.circle(screen, "red", player_pos, 40)

    # -------------------------------------------------------- #

    # obtain information on key pressed
    keys = pg.key.get_pressed()
    
    # move player position based on key pressed and dt
    if keys[pg.K_w]:
        player_pos.y -= 300 * dt
    if keys[pg.K_s]:
        player_pos.y += 300 * dt
    if keys[pg.K_a]:
        player_pos.x -= 300 * dt
    if keys[pg.K_d]:
        player_pos.x += 300 * dt

    # flip() display to put work on screen
    pg.display.flip()

    # limit fps to 60 and sets dt
    dt = clock.tick(60) / 1000

# ------------------------------------------------------- #

# if execution reaches here: quit
pygame.quit()
