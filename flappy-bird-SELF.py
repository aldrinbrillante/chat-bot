# import all modules needed
import pygame
import neat
import time
import os
import random # needed to randomly placing the tubes

# first, set dimension of screen
WIN_WIDTH = 600 #constant 
WIN_HEIGHT = 800 #constant

# next, load all your images
''' code below explained:
scale2x makes image two times bigger 
pygame.image.load loads the image within () '''

#Sidenote: all variable that I code in UPPER_CASE means that they are my constant variables

# line below stores the 3 bird images 
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))) , pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))) , pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
# store the pipe images
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
# store the base image
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
# store the background image
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

''' now that images have stored, i can start programming the first class '''

# making bird class
class Bird:
    #class variables, which are the constants for this class 
    IMGS = BIRD_IMGS
    # variable: max bird rotation is 25 degrees. 
    #used to allow the bird to tilt depending on the direction of movement 
    MAX_ROTATION = 25
    #ROTATION_VELOCITY: how much we're going to rotate on each frame or every time the bird moves 
    ROT_VEL = 20
    # how long we are going to show each bird animation. number of larger or smaller results in how often it shows that the bird will "flap" wings 
    ANIMATION_TIME = 5

    def __init__(self, x, y)