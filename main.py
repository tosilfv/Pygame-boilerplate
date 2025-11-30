import pygame
import os
from sys import exit

# Screen
class Screen():

    def __init__(self):
        self.scr_wid = 800
        self.scr_hgt = 400
        self.scr = pygame.display.set_mode((self.scr_wid, self.scr_hgt))
        self.caption = pygame.display.set_caption("TODO")
        self.clock = pygame.time.Clock()
        self.framerate = 60  # 1/[s]

screen = Screen()

# Background Surface
ground_surf = pygame.image.load(
            "".join(
                [os.path.dirname(__file__), "/graphics/ground.png"]
                )).convert_alpha()

sky_surf = pygame.image.load(
            "".join(
                [os.path.dirname(__file__), "/graphics/sky.png"]
                )).convert_alpha()

# Background Position
ground_pos = (0, 300)
sky_pos = (0, 0)

# Player Surface
player_surf = pygame.image.load(
            "".join(
                [os.path.dirname(__file__), "/graphics/player/"
                "player_stand.png"]
                )).convert_alpha()

# Player Rectangle
player_rect = player_surf.get_rect(midbottom = (100, 300))

# Game Loop
while True:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.scr.blit(sky_surf, sky_pos)
    screen.scr.blit(ground_surf, ground_pos)
    screen.scr.blit(player_surf, player_rect)
    pygame.display.update()
    screen.clock.tick(screen.framerate)
