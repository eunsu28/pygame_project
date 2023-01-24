# import things
import pygame, sys
from pygame.locals import QUIT
from time import sleep

#character
character = pygame.image.load("jet.png")
character_x = 350
character_y = 725
x = 0
y = 0

#basic settings
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 800))
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
                x -= 0.01
            elif event.key == pygame.K_d: 
                x += 0.01
            elif event.key == pygame.K_s: 
                y += 0.01
            elif event.key == pygame.K_w: 
                y -= 0.01
    #change x y
    character_x += x * dt
    character_y += y * dt
    DISPLAYSURF.fill(color)
    DISPLAYSURF.blit(character, (character_x, character_y))

    #gameover
    if character_x > 725 or character_x < -25:
        pygame.display.set_caption("GAME OVER")
        DISPLAYSURF.fill(red)
        running = False
    if character_y > 725 or character_y < -25:
        pygame.display.set_caption("GAME OVER")
        DISPLAYSURF.fill(red)
        running = False
  
    #
    pygame.display.update()

#finish
sleep(4)
pygame.quit()
sys.exit()