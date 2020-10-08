# # import all modules needed
# import pygame
# import neat
# import time
# import os
# import random # needed to randomly placing the tubes

# # first, set dimension of screen
# WIN_WIDTH = 600 #constant 
# WIN_HEIGHT = 800 #constant

# # next, load all your images
# ''' code below explained:
# scale2x makes image two times bigger 
# pygame.image.load loads the image within () '''

# #Sidenote: all variable that I code in UPPER_CASE means that they are my constant variables

# # line below stores the 3 bird images 
# BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))) , pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))) , pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
# # store the pipe images
# PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
# # store the base image
# BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
# # store the background image
# BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

# ''' now that images have stored, i can start programming the first class '''

# # bird class
# class Bird:
#     #class variables, which are the constants for this class 
#     IMGS = BIRD_IMGS
#     # variable: max bird rotation is 25 degrees. 
#     MAX_ROTATION = 25
#     #
#     ROATION_VELOCITY 