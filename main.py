import pygame
import os
from sys import exit
from utils.constants import CAPTION, FIVE, FPS, GRAVITY_MAX, GROUND_LEVEL,\
    GROUND_X, GROUND_Y, PLAYER_X, PLAYER_Y, POINT_ONE, SCREEN_HEIGHT,\
    SCREEN_WIDTH, SCREEN_LIMIT_L, SCREEN_LIMIT_R, SKY_X, SKY_Y, TEN, ZERO

# Variables
running = True

# Initialize Pygame
pygame.init()

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

    def __init__(self):
        self.scr = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.framerate = FPS
        pygame.display.set_caption(CAPTION)

# Background
class Background():

    def __init__(self, screen):
        self.screen = screen
        self.ground_x = GROUND_X
        self.ground_y = GROUND_Y
        self.sky_x = SKY_X
        self.sky_y = SKY_Y

        self.ground_surf = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "media",
                "graphics",
                "entrance_ground_normal.png"))
        self.sky_surf = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "media",
                "graphics",
                "hotel_entrance_normal.png"))

    def draw(self):
        self.screen.scr.blit(self.ground_surf, (self.ground_x, self.ground_y))
        self.screen.scr.blit(self.sky_surf, (self.sky_x, self.sky_y))

# Player
class Player():

    def __init__(self, screen):
        self.moving_horizontally = False
        self.moving_up = False
        self.moving_down = False
        self.screen = screen
        self.gravity = ZERO
        self.player_x = PLAYER_X
        self.player_y = PLAYER_Y
        self.walk_index = ZERO
        self.jump_image = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "media",
                "graphics",
                "player",
                "piccolo_jump_normal.png"))
        self.stand_image = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "media",
                "graphics",
                "player",
                "piccolo_stand_normal.png"))
        walk_image_1 = load_image(
            os.path.join(
                os.path.dirname(__file__),
                "media",
                "graphics",
                "player",
                "piccolo_walk1_normal.png"))
        walk_image_2 = load_image(
            os.path.join(
                os.path.dirname(__file__),
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
                os.path.dirname(__file__),
                "media",
                "audio",
                "musa1.wav"))
        self.music.set_volume(POINT_ONE)
        self.music.play(loops=-1)
        self.jump_sound = pygame.mixer.Sound(
            os.path.join(
                os.path.dirname(__file__),
                "media",
                "audio",
                "hyppy.mp3"))
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
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_LEVEL + FIVE:
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
        if self.moving_down and self.rect.bottom >= GROUND_LEVEL + FIVE:
            print('4')
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

# Game
class Game:

    def __init__(self, screen, background, player) -> None:
        self.screen = screen
        self.background = background
        self.player = player

    def run(self):
        # Draw
        self.background.draw()
        self.player.draw()

        # Update
        pygame.display.update()
        self.player.update()

        # Clock
        game.screen.clock.tick(game.screen.framerate)

        # Print
        print(f'x: {game.player.rect_x}, y: {game.player.rect_y}')


# Create Objects and Game
screen = Screen()
background = Background(screen)
player = Player(screen)
game = Game(screen, background, player)

# Game Loop
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    # Run
    game.run()

# Exit
pygame.quit()
exit()
