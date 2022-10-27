
import sys
from tkinter import CENTER
from urllib.parse import SplitResult
from webbrowser import get
import pygame 
pygame.init()
sh = 1500
sw = 1500
FPS = 60
FPS_clock = pygame.time.Clock()


screen = pygame.display.set_mode((sh,sw))
pygame.display.set_caption("car game")

# bgimage = pygame.image.load("bg.jpeg")  Test the background picture 
icon = pygame.image.load('/Users/gilber/Documents/code/pygame-main/pygame/vehicle.png')
pygame.display.set_icon(icon)
#making the class of the player 
car_player = pygame.image.load("Pngegg.png")
class Background(pygame.sprite.Sprite):
      def __init__(self): 
          super().__init__()
          self.bgimage = pygame.image.load("bg.jpeg")
          self.bgY = 0 
          self.bgX = 0

      def render(self):
          screen.blit(self.bgimage, (self.bgX, self.bgY))

 
 
class Ground(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.image = pygame.image.load("bg.jpeg")
          self.rect =self.image.get_rect(center = (350,350))
          
     def render(self):
          screen.blit(self.image,(self.rect.x, self.rect.y))
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
     
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()


BG = Background()
GR =Ground()
while True:
     screen.fill((0,0,0))
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               sys.exit()
               pygame.QUIT
          if event.type == pygame.KEYDOWN:
               pass
     
     # screen.blit(bgimage,(0,0))
     GR.render()
     
     pygame.display.update()
     FPS_clock.tick(FPS)