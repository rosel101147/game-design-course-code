
import pygame, sys
from pygame.locals import *

pygame.init()

RESOLUTION = (400,300)

DISPLAYSURF = pygame.display.set_mode(RESOLUTION) # single tuple arguement
pygame.display.set_caption("Pygame Intro")


# Colors    = (  R,  G,  B)

BLACK       = (  0,   0,   0)
WHITE       = (255, 255, 255)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
BLUE        = (  0,   0, 255)
PURPLE      = (128,   0, 128)

BGCOLOR = WHITE

# Draw some shapes on the screen
DISPLAYSURF.fill(BGCOLOR)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146,0),(291,106), (236,277), (56,277), (0,106))) 
pygame.draw.line(DISPLAYSURF, BLUE, (60,60), (60,120), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120,60), (60,120))
pygame.draw.line(DISPLAYSURF, BLUE, (60,120), (120,120), 2)
pygame.draw.circle(DISPLAYSURF, PURPLE, (300, 50), 20, 4) #(surface, color, center, radius, thickness)
pygame.draw.ellipse(DISPLAYSURF, RED, (40, 80,250,200), 1) #(surface, color, (rect))
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50)) #(surface, color, (rect - verticles of quadrilateral))

# Game loop
while (True):
    # Event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

