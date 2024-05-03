import pygame
import sys
from generateTerrain import *
from paesslerNoise import generateNoisemap
import time

class Drawer:
    
    

    def __init__(self):
        self.textures = []
        
        pass

    def loadTextures(self, size=64):
        size = size
        
        texturegrass = pygame.image.load("textures/grassblockv2.png").convert_alpha()
        texturegrass = pygame.transform.scale(texturegrass, (size, size))

        texturesand = pygame.image.load("textures/sandblock.png").convert_alpha()
        texturesand = pygame.transform.scale(texturesand, (size, size))

        texturetree0 = pygame.image.load("textures/tree3.png").convert_alpha()
        texturetree0 = pygame.transform.scale(texturetree0, (size, size*2))

        texturetree1 = pygame.image.load("textures/tree3.png").convert_alpha()
        texturetree1 = pygame.transform.scale(texturetree1, (size, size*2))
        
        bush0 = pygame.image.load("textures/bush0.png").convert_alpha()
        bush0 = pygame.transform.scale(bush0, (size, size))
        
        self.textures.append(texturegrass)
        self.textures.append(texturesand)
        self.textures.append(texturetree0)
        self.textures.append(texturetree1)
        self.textures.append(bush0)
        
    def drawTerrain(self, screen, ground, objects, screenwidth, screenheight):
        
        
       
        texture = self.textures[0]
        texturewidth = texture.get_width()
        textureheight = texture.get_height()
        """
        texture = pygame.transform.scale(texture, (texturewidth // 2, textureheight // 2))  # Replace "// 2" with the desired scaling factor
        texturewidth = texture.get_width()
        textureheight = texture.get_height()
        """

        
        screen.fill((50, 50, 50))
        
        for y in range(len(ground)):
            for x in range(len(ground[0])): 

                # Blit the texture onto the screen at the desired position
                    
                    
                #screen.blit(self.textures[0], (startx + x * texturewidth, starty + y * textureheight))
                #rect(surface, color, rect)
                if (ground[y][x] > 0.2):
                
                    screen.blit(self.textures[1], (x * texturewidth / 2 - texturewidth / 2 * y, x * texturewidth / 4 + texturewidth / 4 * y))
                else:
                    screen.blit(self.textures[0], (x * texturewidth / 2 - texturewidth / 2 * y, x * texturewidth / 4 + texturewidth / 4 * y))

        for y in range(len(objects)):
            for x in range(len(objects[0])): 

                # Blit the texture onto the screen at the desired position
                    
                    
                #screen.blit(self.textures[0], (startx + x * texturewidth, starty + y * textureheight))
                #rect(surface, color, rect)
                if (objects[y][x] > 0.4):
                
                    screen.blit(self.textures[3], (x * texturewidth / 2 - texturewidth / 2 * y, x * texturewidth / 4 + texturewidth / 4 * y + texturewidth))
                elif (objects[y][x] == 0.3):
                
                    screen.blit(self.textures[4], (x * texturewidth / 2 - texturewidth / 2 * y, x * texturewidth / 4 + texturewidth / 4 * y + 2 * texturewidth))
               


                # Update the display
        pygame.display.flip()
        
