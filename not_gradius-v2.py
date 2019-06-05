import pygame, sys
from pygame.locals import *

pygame.init()

display_width = 1000
display_height = 600


gameWindow = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('not gradius')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
grey = (60,60,60)

clock = pygame.time.Clock()
dead = False
shipImg = pygame.image.load('spaceship.png')

def ship(x,y):
    gameWindow.blit(shipImg, (x,y))

x = (display_width * 0.05)
y = (display_height * 0.40)

x_change = 0 
y_change = 0


while not dead:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        dead = True
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        x_change = -5
      if event.key == pygame.K_d:
        x_change = 5
      if event.key == pygame.K_s:
        y_change = 5
      if event.key == pygame.K_w:
        y_change = -5
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key ==pygame.K_d or event.key ==pygame.K_w or event.key ==pygame.K_s:
          x_change = 0
          y_change = 0
          
  x += x_change
  y += y_change
  
  
  gameWindow.fill(grey)
  ship(x,y)  
  pygame.display.update()
  clock.tick(60)

pygame.quit()
quit() 