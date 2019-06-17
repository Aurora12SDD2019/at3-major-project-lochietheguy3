import pygame
import time
import random
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
brown = (115,75,15)

ship_width = 65
ship_height = 65

clock = pygame.time.Clock()

shipImg = pygame.image.load('spaceship.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameWindow, color, [thingx, thingy, thingw, thingh])
    

def ship(x,y):
    gameWindow.blit(shipImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',120)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameWindow.blit(TextSurf,TextRect)
    
    pygame.display.update() 
    
    time.sleep(2)
    
    game_loop()
    
    
def dead():
    message_display('ded')

def game_loop():
    x = (display_width * 0.05)
    y = (display_height * 0.40)

    x_change = 0 
    y_change = 0
    
    thing_starty = random.randrange(0, display_height)
    thing_startx = 1100
    thing_speed = -3
    thing_width = 140
    thing_height = 140
    
    
    gameExit = False
    while not gameExit:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
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
    
      
      
      things(thing_startx, thing_starty, thing_width, thing_height, brown)
      thing_startx += thing_speed
      
      
      ship(x,y)
      
      xcross = 0
      ycross = 0 
      
      if x > display_width - ship_width or x < 0:
          dead()
      if y > display_height - ship_height - 10 or y < -25:
          dead()
      if thing_startx < display_width - 1500:
          thing_startx = 1100 - thing_width
          thing_starty = random.randrange(0,display_height)
      
      if y > thing_starty and y < thing_starty + ship_height + 47 or y + ship_height > thing_starty and y < thing_starty + thing_height - ship_height:
            print('y crossover')
            xcross = 1 
    
    
      if x > thing_startx and x < thing_startx + thing_width or x+ship_width > thing_startx and x + ship_width < thing_startx+thing_width:
            print('x crossover')
            ycross = 1
     
      if xcross and ycross == 1:
        print ("double crossover")
        dead()
        
        
         

      pygame.display.update()
      clock.tick(60)



game_loop()
pygame.quit()
quit()  