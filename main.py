# import things
import pygame, sys
from pygame.locals import QUIT

#character
character = pygame.image.load("jet.png")
character_x = 200
character_y = 400

#basic settings
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello World!')
color = (255, 255, 255)
clock = pygame.time.Clock()

#main
running = True
while running:
    dt = clock.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: 
                character_x -= 10
            elif event.key == pygame.K_d: 
                character_x += 10
            elif event.key == pygame.K_s: 
                character_y += 10
            elif event.key == pygame.K_w: 
                character_y -= 10
    #write your code
    DISPLAYSURF.fill(color)
    DISPLAYSURF.blit(character, (character_x, character_y))

    if character_x > 400 or character_x < 0:
        print("gameover")
        DISPLAYSURF.fill(color)
        DISPLAYSURF.blit(character, (character_x, character_y))
        running = False
  
    #
    pygame.display.update()

#fin