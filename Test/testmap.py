
import pygame 
from  pygame_functions import *

pygame.init()
bg = pygame.image.load("bg.jpeg")
bg = pygame.transform.scale(bg,(600,600))
screen = pygame.display.set_mode((600,600))
# screensize(600,600)
# setAutoUpdate(False)


i = True
while i:

    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            i = False
        if keyPressed("right"):
            pass
    pygame.display.update()
pygame.quit() 