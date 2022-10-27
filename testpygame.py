from sys import displayhook
import pygame 
pygame.init()
screen = pygame.display.set_mode((800,600))
time = pygame.time.Clock()
while True:
     screen.fill((0,0,255))
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               sys.exit()
               pygame.QUIT
     time.tick(200)

     
     pygame.display.update()
