import pygame
import os
from sys import exit
from random import randint

class Screen():
    def __init__(self):
        self.scr_wid = 800
        self.scr_hgt = 400
        self.screen = pygame.display.set_mode((self.scr_wid, self.scr_hgt))
        self.caption = pygame.display.set_caption("Pygame")
        self.clock = pygame.time.Clock()
        self.framerate = 60  # Times / second

class Game():
    def __init__(self):
        self.game_active = False
        self.start_time = 0
        self.score = 0
        self.bg_music = pygame.mixer.Sound("".join([os.path.dirname(__file__), "/audio/music.wav"]))
        self.bg_music.set_volume(0.1)
        self.bg_music.play(loops=-1)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_walk_1.png"])).convert_alpha()
        player_walk_2 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_walk_2.png"])).convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_jump.png"])).convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("".join([os.path.dirname(__file__), "/audio/jump.mp3"]))
        self.jump_sound.set_volume(0.1)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_frame_1 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/fly/fly1.png"])).convert_alpha()
            fly_frame_2 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/fly/fly2.png"])).convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/snail/snail1.png"])).convert_alpha()
            snail_frame_2 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/snail/snail2.png"])).convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill

screen = Screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    screen.clock.tick(screen.framerate)
