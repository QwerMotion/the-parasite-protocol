import pygame
import sys
from generateTerrain import *
from draw import Drawer



#
generateMap("testwelt", 100, 100)
ground, objects = loadMap("testwelt")
# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Rectangle")

drawer = Drawer()
drawer.loadTextures()



# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the rectangle
    drawer.drawTerrain(screen, ground, objects, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
    fps = clock.get_fps()
    pygame.display.set_caption("per second [frames]" + str(fps))
    

# Quit Pygame
pygame.quit()
sys.exit()
