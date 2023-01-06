import pygame, sys
from pygame.locals import QUIT

character = pygame.image.load("jet.png")
character_x = 200
character_y = 400

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello World!')
color = (255, 255, 255)
 
# Changing surface color
DISPLAYSURF.fill(color)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: 
                character_x += 10
            elif event.key == pygame.K_d: 
                print("right")
            elif event.key == pygame.K_s: 
                print("down")
            elif event.key == pygame.K_w: 
                print("up")
    #write your code
    DISPLAYSURF.blit(character, (character_x, character_y))
    #
    pygame.display.update()


print("game finished")
#https://parkjh7764.tistory.com/89?category=1206156