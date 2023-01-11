import pygame, sys
from pygame.locals import QUIT

character = pygame.image.load("jet.png")
character_x = 200
character_y = 400

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello World!')
color = (255, 255, 255)
clock = pygame.time.Clock()

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
    #
    pygame.display.update()


print("game finished")
#https://parkjh7764.tistory.com/89?category=1206156