# Credits: Platformer Art Deluxe (Pixel) by Kenney Vleugels (www.kenney.nl)
# Music: Juhani Junkala

import pygame
import os
from sys import exit

# Run init before anything else
pygame.init()

# Setup Screen
scr_wid = 800
scr_hgt = 400
screen = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()
framerate = 60  # Times / second
test_font = pygame.font.Font("".join([os.path.dirname(__file__), "/font/Pixeltype.ttf"]), 50)

# Setup Surface
sur_wid = 100
sur_hgt = 200
sur_pos_origin = (0, 0)
sur_pos_ground = (0, 300)
sur_pos_text = (300, 200)
sky_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/sky.png"])).convert_alpha()
ground_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/ground.png"])).convert_alpha()
text_surface = test_font.render("Hello, World!", False, "White")
snail_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/snail/snail1.png"])).convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (900, 300))
player_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_walk_1.png"])).convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    # Check all possible types of inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')
    
    # Attach surfaces
    screen.blit(sky_surface, sur_pos_origin)
    screen.blit(ground_surface, sur_pos_ground)
    screen.blit(text_surface, sur_pos_text)
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("Collision!")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    # Draw all elements, update everything
    pygame.display.update()
    clock.tick(framerate)  # Do not run the while loop faster than framerate
