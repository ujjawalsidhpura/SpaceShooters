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
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.max_health = health
        self.mask = pygame.mask.from_surface(self.ship_img)


class Enemy(Ship):
    COLOR_MAP = {
        'red': (RED_SPACE_SHIP, RED_LASER),
        'green': (GREEN_SPACE_SHIP, GREEN_LASER),
        'blue': (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, velocity):
        self.y += velocity


def main():
    run = True
    FPS = 60
    level = 1
    lives = 3
    main_font = pygame.font.SysFont('arial', 50)
    player_velocity = 5

    enemies = []
    enemy_velocity = 1
    wave_length = 5

    clock = pygame.time.Clock()

    player = Player(450, 800)

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f'Lives : {lives}', 1, (255, 255, 255))
        level_label = main_font.render(f'Level : {level}', 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        player.draw(WIN)

        for enemy in enemies:
            enemy.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100),
                              random.randrange(-1500, -100), random.choice(['red', 'blue', 'green']))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_velocity > 0:
            player.x -= player_velocity
        if keys[pygame.K_RIGHT] and player.x + player_velocity + player.get_width() < WIDTH:
            player.x += player_velocity
        if keys[pygame.K_UP] and player.y - player_velocity > 0:
            player.y -= player_velocity
        if keys[pygame.K_DOWN] and player.y + player_velocity + player.get_height() < HEIGHT:
            player.y += player_velocity

        for enemy in enemies:
            enemy.move(enemy_velocity)

        redraw_window()


main()
