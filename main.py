import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello World!')

color = (255, 255, 255)
 
# Changing surface color
DISPLAYSURF.fill(color)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #write your code
    
    #
    pygame.display.update()

#https://parkjh7764.tistory.com/88