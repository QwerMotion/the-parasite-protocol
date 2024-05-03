import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame App with Transparent Image")

# Load the image with transparency
image = pygame.image.load("textures/grassblockv2.png").convert_alpha()
size = 64
image = pygame.transform.scale(image, (size, size))


# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((20, 20, 20))

    # Blit the image onto the screen
    for y in range((screen_height // size)):
        for x in range((screen_width // size)):
            
            #offsetrng = random.randint(0, 1)
            screen.blit(image, (x * size / 2 - size / 2 * y + 500, x * size / 4 + size / 4 * y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(1)
    fps = clock.get_fps()
    pygame.display.set_caption("per second [frames]" + str(fps))
    

# Quit Pygame
pygame.quit()
sys.exit()
