import pygame, sys
from pygame.locals import *

pygame.init()

display_width = 1000
display_height = 600


gameWindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('not gradius')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

clock = pygame.time.Clock()
dead = False
shipImg = pygame.image.load('C:\\Users\\lochi\\OneDrive\\Documents\\SDD\\not_gradius\\thing\\spaceship.png')

def ship(x,y):
    gameWindow.blit(shipImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)




while not dead:
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        dead = True
    
    print(event)
    
  gameWindow.fill(white)
  ship(x,y)  
  pygame.display.update()
  clock.tick(60)

pygame.quit()
quit() 