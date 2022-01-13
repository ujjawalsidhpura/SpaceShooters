import pygame
import os
import random
import time

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SpaceShooter')

# Load Images
RED_SPACE_SHIP = pygame.image.load('assets/pixel_ship_red_small.png')
GREEN_SPACE_SHIP = pygame.image.load('assets/pixel_ship_green_small.png')
BLUE_SPACE_SHIP = pygame.image.load('assets/pixel_ship_blue_small.png')

# Player Ships
YELLOW_SPACE_SHIP = pygame.image.load('assets/pixel_ship_yellow.png')

# Lasers
RED_LASER = pygame.image.load('assets/pixel_laser_red.png')
GREEN_LASER = pygame.image.load('assets/pixel_laser_green.png')
BLUE_LASER = pygame.image.load('assets/pixel_laser_blue.png')
YELLOW_LASER = pygame.image.load('assets/pixel_laser_yellow.png')

# Background
BG = pygame.image.load('assets/background-black.png')