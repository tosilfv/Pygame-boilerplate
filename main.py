# Credits: Platformer Art Deluxe (Pixel) by Kenney Vleugels (www.kenney.nl)
# Music: Juhani Junkala

import pygame
import os
from sys import exit
from random import randint

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f"Score: {current_time // 1000}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return (score_surf, score_rect, current_time // 1000)


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

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
# Game
game_active = False
start_time = 0
score = 0

# Setup Surface
sur_wid = 100
sur_hgt = 200
sur_pos_origin = (0, 0)
sur_pos_ground = (0, 300)
sur_pos_text = (300, 200)
sky_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/sky.png"])).convert_alpha()
ground_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/ground.png"])).convert_alpha()

# Obstacles
snail_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/snail/snail1.png"])).convert_alpha()
# snail_rect = snail_surface.get_rect(bottomright = (900, 300))

fly_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/fly/fly1.png"])).convert_alpha()

obstacle_rect_list = []


player_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_walk_1.png"])).convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_stand.png"])).convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))
text_title = test_font.render("Jumper Game", False, (64, 64, 64))
text_title_rect = text_title.get_rect(center = (400, 50))
text_instr = test_font.render("Press Space to Start", False, (64, 64, 64))
text_instr_rect = text_instr.get_rect(center = (400, 350))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    # Check all possible types of inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if player_rect.bottom == 300:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
                    # print('jump')
                # print('key pressed')
            # if event.type == pygame.KEYUP:
            #     print('key released')

            # if event.type == pygame.MOUSEMOTION:
            #     # print(event.pos)
            #     if player_rect.collidepoint(event.pos):
            #         print('collision')

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.bottom == 300:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    # snail_rect.left = 800
                    start_time = pygame.time.get_ticks()
        if event.type == obstacle_timer:
            if game_active:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 210)))

    if game_active:
        # Attach surfaces
        screen.blit(sky_surface, sur_pos_origin)
        screen.blit(ground_surface, sur_pos_ground)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 15)
        # pygame.draw.line(screen, '#c0e8ec', (0,0), (800, 400), 15)
        # pygame.draw.ellipse(screen, 'white', pygame.Rect(50, 200, 100, 100))
        # screen.blit(score_surface, score_rect)

        # snail_rect.x -= 4
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surface, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        game_active = collisions(player_rect, obstacle_rect_list)

        # if player_rect.colliderect(snail_rect):
        #     game_active = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        # if player_rect.colliderect(snail_rect):
        #     print("Collision!")

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())
        score_surf, score_rect, score = display_score()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        if score > 0:
            screen.blit(score_surf, score_rect)
        else:
            screen.blit(text_title, text_title_rect)
            screen.blit(text_instr, text_instr_rect)


    # Draw all elements, update everything
    pygame.display.update()
    clock.tick(framerate)  # Do not run the while loop faster than framerate

print("Game Over.")
