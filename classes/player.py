import pygame
import os
from utils.constants.constants import FIVE, GRAVITY_MAX, GROUND_LEVEL,\
    PLAYER_X, PLAYER_Y, POINT_ONE, SCREEN_WIDTH, SCREEN_LIMIT_L,\
    SCREEN_LIMIT_R, TEN, ZERO
from utils.helpers import helpers

# Initialize Pygame
pygame.init()

# Player
class Player():

    def __init__(self, mediator, screen):
        self.mediator = mediator
        self.moving_horizontally = False
        self.moving_up = False
        self.moving_down = False
        self.screen = screen
        self.gravity = ZERO
        self.player_x = PLAYER_X
        self.player_y = PLAYER_Y
        self.walk_index = ZERO
        self.jump_image = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_jump_normal.png"))
        self.stand_image = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_stand_normal.png"))
        walk_image_1 = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_walk1_normal.png"))
        walk_image_2 = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_walk2_normal.png"))
        self.walking = [walk_image_1, walk_image_2]
        self.image = self.stand_image

        # Place rectangle from midbottom
        self.rect = self.image.get_rect(
                    midbottom = (self.player_x, self.player_y))

        # Music and sounds
        self.music = pygame.mixer.Sound(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "audio",
                "musa1.wav"))
        self.music.set_volume(POINT_ONE)
        self.music.play(loops=-1)
        self.jump_sound = pygame.mixer.Sound(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "audio",
                "hyppy.mp3"))
        self.jump_sound.set_volume(POINT_ONE)
        self.notify('Player was created.')

    @property
    def rect_x(self):
        return self.rect.x

    @property
    def rect_y(self):
        return self.rect.y

    @rect_y.setter
    def rect_y(self, val):
        self.rect.y = val

    def player_input(self):
        keys = pygame.key.get_pressed()

        # Move
        if keys[pygame.K_LEFT]:
            self.player_x += -FIVE
            self.moving_horizontally = True
        elif keys[pygame.K_RIGHT]:
            self.player_x += FIVE
            self.moving_horizontally = True
        else:
            self.moving_horizontally = False
        if self.player_x > SCREEN_WIDTH - SCREEN_LIMIT_R:
            self.player_x = SCREEN_WIDTH - SCREEN_LIMIT_R
        elif self.player_x < SCREEN_LIMIT_L:
            self.player_x = SCREEN_LIMIT_L

        # Jump
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_LEVEL + FIVE:
            self.moving_up = True
            self.play_sound(self.jump_sound)
            self.notify('Player jumped')

        self.rect = self.image.get_rect(
                    midbottom = (self.player_x, self.player_y))

    def apply_gravity(self):
        # BEGINNING:
            # Gravity = 0
        if self.moving_up:
            # JUMP:
                # Gravity Cumulative -10
                # Fly Until At Vertical Top Max
            self.gravity += -TEN
            self.rect.bottom += self.gravity
        if self.gravity <= GRAVITY_MAX:
            # At Vertical Top Max
                # Gravity <= -100
                # Start Descending
            self.rect.bottom += -self.gravity
            self.moving_up = False
            self.moving_down = True
        if self.moving_down:
            # Descending:
                # Gravity Cumulative +10
                # Fly Until At Ground Level
            self.gravity += TEN
            self.rect.bottom += self.gravity
        if self.moving_down and self.rect.bottom >= GROUND_LEVEL + FIVE:
            # At Ground Level:
                # Gravity = 0
            self.rect.bottom = GROUND_LEVEL + FIVE
            self.moving_down = False
            self.gravity = ZERO

    def draw(self):
        self.screen.scr.blit(self.image, self.rect)

    def animate(self):
        if self.rect.bottom < GROUND_LEVEL + FIVE:
            self.image = self.jump_image
        elif self.rect.bottom == GROUND_LEVEL + FIVE:
            if self.moving_horizontally:
                self.walk_index += POINT_ONE
                if self.walk_index >= len(self.walking):
                    self.walk_index = ZERO
                self.image = self.walking[int(self.walk_index)]
            else:
                self.image = self.stand_image

    def play_sound(self, sound):
        sound.play()

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate()

    def notify(self, message):
        self.mediator.notify(message)
