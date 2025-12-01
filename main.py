import pygame
import os
from sys import exit

# Screen
class Screen():

    def __init__(self):
        self.scr_wid = 800
        self.scr_hgt = 400
        self.scr = pygame.display.set_mode((self.scr_wid, self.scr_hgt))
        self.clock = pygame.time.Clock()
        self.framerate = 60  # 1/[s]

# Background
class Background():

    def __init__(self):
        try:
            self.ground_surf = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "graphics", "ground.png")
            ).convert_alpha()
            self.sky_surf = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "graphics", "sky.png")
            ).convert_alpha()
        except FileNotFoundError:
            print("Background files not found")
        self.ground_pos = (0, 300)
        self.sky_pos = (0, 0)

    def draw(self, screen):
        screen.blit(self.sky_surf, self.sky_pos)
        screen.blit(self.ground_surf, self.ground_pos)

# Player
class Player():

    def __init__(self):
        try:
            self.player_surf = pygame.image.load(
                os.path.join(os.path.dirname(__file__), "graphics", "player",
                "player_stand.png")).convert_alpha()
            self.player_rect = self.player_surf.get_rect(
                midbottom = (100, 300))
        except FileNotFoundError:
            print("Player file not found")

    def draw(self, screen):
        screen.blit(self.player_surf, self.player_rect)

# Initialize Pygame
pygame.init()
pygame.display.set_caption("TODO")
screen = Screen()
background = Background()
player = Player()

# Game Loop
while True:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            exit()

    background.draw(screen.scr)
    player.draw(screen.scr)
    pygame.display.update()
    screen.clock.tick(screen.framerate)
