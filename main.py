import pygame
import os
from sys import exit

# Constants
CAPTION = "Pygame"
FIVE = 5
FPS = 60  # Frames per second
GRAVITY_MAX = -150
GROUND_LEVEL = 300
GROUND_X = 0
GROUND_Y = GROUND_LEVEL
ONE = 1
PLAYER_X = 100
PLAYER_Y = GROUND_LEVEL
POINT_ONE = 0.1
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800
SCREEN_LIMIT_L = 35
SCREEN_LIMIT_R = 40
SKY_X = 0
SKY_Y = 0
TEN = 10
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

    def __init__(self, screen, walk_index, player_x, player_y):
        self.moving_horizontally = False
        self.moving_up = False
        self.moving_down = False
        self.screen = screen
        self.gravity = ZERO
        self.player_x = player_x
        self.player_y = player_y
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
        self.jump_sound.set_volume(POINT_ONE)

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
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_LEVEL:
            self.moving_up = True
            self.play_sound(self.jump_sound)

        self.rect = self.image.get_rect(
                    midbottom = (self.player_x, self.player_y))

    def apply_gravity(self):
        # BEGINNING:
            # Gravity = 0
        if self.moving_up:
            print('1')
            # JUMP:
                # Gravity Cumulative -10
                # Fly Until At Vertical Top Max
            self.gravity += -TEN
            self.rect.bottom += self.gravity
        if self.gravity <= GRAVITY_MAX:
            print('2')
            # At Vertical Top Max
                # Gravity <= -100
                # Start Descending
            self.rect.bottom += -self.gravity
            self.moving_up = False
            self.moving_down = True
        if self.moving_down:
            print('3')
            # Descending:
                # Gravity Cumulative +10
                # Fly Until At Ground Level
            self.gravity += TEN
            self.rect.bottom += self.gravity
        if self.moving_down and self.rect.bottom >= GROUND_LEVEL:
            print('4')
            # At Ground Level:
                # Gravity = 0
            self.rect.bottom = GROUND_LEVEL
            self.moving_down = False
            self.gravity = ZERO

    def draw(self):
        self.screen.scr.blit(self.image, self.rect)

    def animate(self):
        if self.rect.bottom < GROUND_LEVEL:
            self.image = self.jump_image
        elif self.rect.bottom == GROUND_LEVEL:
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

# Initialize Pygame
pygame.init()

# Create Objects
screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION)
background = Background(screen, GROUND_X, GROUND_Y, SKY_X, SKY_Y)
player = Player(screen, ZERO, PLAYER_X, PLAYER_Y)

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

    # Print
    print(f'x: {player.rect_x}, y: {player.rect_y}')

    # Clock
    screen.clock.tick(screen.framerate)

# Exit
pygame.quit()
exit()
