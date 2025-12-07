import pygame
import os
from sys import exit

# Constants
CAPTION = "Pygame"
GROUND_LEVEL = 300
FPS = 60  # Frames per second
GROUND_X = 0
GROUND_Y = GROUND_LEVEL
JUMP_HEIGHT = -20
ONE = 1
PLAYER_X = 100
PLAYER_Y = GROUND_LEVEL
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_LIMIT_L = 35
SCREEN_LIMIT_R = 40
SKY_X = 0
SKY_Y = 0
ZERO = 0

# Variables
running = True

# Load Image
def load_image(path, default_color=(ZERO, 255, ZERO), default_size=(100, 100)):
    try:
        image = pygame.image.load(path).convert_alpha()
        return image
    except pygame.error as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: File not found in '{path}'")
    placeholder = pygame.Surface(default_size)
    placeholder.fill(default_color)
    return placeholder

# Screen
class Screen():

    def __init__(self, width, height, caption):
        self.scr = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.framerate = FPS
        pygame.display.set_caption(caption)

# Background
class Background():

    def __init__(self, screen, ground_x, ground_y, sky_x, sky_y):
        self.screen = screen
        self.ground_x = ground_x
        self.ground_y = ground_y
        self.sky_x = sky_x
        self.sky_y = sky_y

        self.ground_surf = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "graphics",
                "ground.png"))
        self.sky_surf = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "graphics",
                "sky.png"))

    def draw(self):
        self.screen.scr.blit(self.ground_surf, (self.ground_x, self.ground_y))
        self.screen.scr.blit(self.sky_surf, (self.sky_x, self.sky_y))

# Player
class Player():

    def __init__(self, screen, gravity, walk_index, player_x, player_y,
                ground_level, jump_height):
        self.moving_horizontally = False
        self.screen = screen
        self.gravity = gravity
        self.player_x = player_x
        self.player_y = player_y
        self.ground_level = ground_level
        self.jump_height = jump_height
        self.walk_index = walk_index
        self.jump_image = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "graphics",
                "player",
                "player_jump.png"))
        self.stand_image = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "graphics",
                "player",
                "player_stand.png"))
        walk_image_1 = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "graphics",
                "player",
                "player_walk_1.png"))
        walk_image_2 = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "graphics",
                "player",
                "player_walk_2.png"))
        self.walking = [walk_image_1, walk_image_2]
        self.image = self.stand_image
        # Place rectangle from midbottom
        self.rect = self.image.get_rect(
                    midbottom = (self.player_x, self.player_y))
        self.jump_sound = pygame.mixer.Sound(
            os.path.join(
                os.path.dirname(__file__),
                "audio",
                "jump.mp3"))
        self.jump_sound.set_volume(0.1)

    def player_input(self):
        keys = pygame.key.get_pressed()
        # Move
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            if self.rect.bottom == self.ground_level:
                if keys[pygame.K_LEFT]:
                    self.player_x += -5
                elif keys[pygame.K_RIGHT]:
                    self.player_x += 5
                self.rect = self.image.get_rect(
                    midbottom = (self.player_x, self.player_y))
            if self.player_x > SCREEN_WIDTH - SCREEN_LIMIT_R:
                self.player_x = SCREEN_WIDTH - SCREEN_LIMIT_R
                self.rect = self.image.get_rect(
                    midbottom = (self.player_x, self.player_y))
            elif self.player_x < SCREEN_LIMIT_L:
                self.player_x = SCREEN_LIMIT_L
                self.rect = self.image.get_rect(
                    midbottom = (self.player_x, self.player_y))
            self.moving_horizontally = True
        else:
            self.moving_horizontally = False
        # Jump
        if keys[pygame.K_SPACE] and self.rect.bottom >= self.ground_level:
            self.gravity = self.jump_height
            self.play_sound(self.jump_sound)

    def apply_gravity(self):
        self.gravity += ONE
        self.rect.y += self.gravity
        if self.rect.bottom >= self.ground_level:
            self.rect.bottom = self.ground_level

    def draw(self):
        self.screen.scr.blit(self.image, self.rect)

    def animate(self):
        if self.rect.bottom < self.ground_level:
            self.image = self.jump_image
        elif self.rect.bottom == self.ground_level:
            if self.moving_horizontally:
                self.walk_index += 0.1
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

# Initialize Pygame
pygame.init()

# Create Objects
screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION)
background = Background(screen, GROUND_X, GROUND_Y, SKY_X, SKY_Y)
player = Player(screen, ZERO, ZERO, PLAYER_X, PLAYER_Y, GROUND_LEVEL,
        JUMP_HEIGHT)

# Game Loop
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    # Draw
    background.draw()
    player.draw()

    # Update
    pygame.display.update()
    player.update()

    # Clock
    screen.clock.tick(screen.framerate)

# Exit
pygame.quit()
exit()
