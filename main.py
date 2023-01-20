# import things
import pygame, sys
from pygame.locals import QUIT
from time import sleep

#character
character = pygame.image.load("jet.png")
character_x = 200
character_y = 400
x = 0
y = 0

#basic settings
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('GAME')
color = (255, 255, 255)
red = (255, 0, 0)
clock = pygame.time.Clock()

#main
running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running == False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: 
                x -= 1
            elif event.key == pygame.K_d: 
                x += 1
            elif event.key == pygame.K_s: 
                y += 1
            elif event.key == pygame.K_w: 
                y -= 1
    #write your code
    character_x += x
    character_y += y
    DISPLAYSURF.fill(color)
    DISPLAYSURF.blit(character, (character_x, character_y))

    if character_x > 400 or character_x < 0:
        pygame.display.set_caption("GAME OVER")
        DISPLAYSURF.fill(red)
        DISPLAYSURF.blit(character, (character_x, character_y))
        running = False
    if character_y > 400 or character_y < 0:
        pygame.display.set_caption("GAME OVER")
        DISPLAYSURF.fill(red)
        DISPLAYSURF.blit(character, (character_x, character_y))
        running = False
  
    #
    pygame.display.update()

sleep(4)
pygame.quit()
sys.exit()
#fin