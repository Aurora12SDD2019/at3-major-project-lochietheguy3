"""a simple sidescrolling game where you are a small spaceship and
you have to shoot enemies and avoid being hit
"""

__author__ = "lochie stoddart"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Alpha, Beta or Release"

#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows
from mods import *

    
   
        
        
        
# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1000, 600  # sets size of screen/window
screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen

# set variables for some colours if you wnat them RGB (0-255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

Player = spaceship()
screen.blit(Spaceship.image, Spaceship.postiton)

play = True  # controls whether to keep playing

# game loop - runs loopRate times a second!
while play==True:  # game loop - note:  everything in this loop is indented one tab

    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
        
        # your code starts here #
        if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
            # change this to do something if user clicks mouse
            # or touches screen
            print("someone clicked a mouse button")
            print(event)


    # your code ends here #
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
P.quit()   # stops the game engine
sys.exit()  # close operating system window
