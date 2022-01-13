from ctypes.wintypes import RGB
from curses import window
import pygame
import os
import random
import time
pygame.font.init()

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
BG = pygame.transform.scale(pygame.image.load(
    'assets/background-black.png'), (WIDTH, HEIGHT))


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))

        # Make sure game runs at same speed on all PC


def main():
    run = True
    FPS = 60
    level = 1
    lives = 3
    main_font = pygame.font.SysFont('arial', 50)
    player_velocity = 5

    clock = pygame.time.Clock()

    ship = Ship(450, 800)

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f'Lives : {lives}', 1, (255, 255, 255))
        level_label = main_font.render(f'Level : {level}', 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        ship.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ship.x -= player_velocity
        if keys[pygame.K_RIGHT]:
            ship.x += player_velocity
        if keys[pygame.K_UP]:
            ship.y -= player_velocity
        if keys[pygame.K_DOWN]:
            ship.y += player_velocity


main()
