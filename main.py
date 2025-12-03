import pygame
import os
from sys import exit

# Constants
FPS = 60
GROUND_X = 0
GROUND_Y = 300
PLAYER_X = 100
PLAYER_Y = 300
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SKY_X = 0
SKY_Y = 0

# Variables
running = True

# Load Images
def load_image(path, default_color=(255, 0, 0), default_size=(100, 100)):
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
        self.framerate = FPS  # 1/[s]
        pygame.display.set_caption(caption)

# Background
class Background():

    def __init__(self, screen, ground_x, ground_y, sky_x, sky_y):
        self.screen = screen
        self.ground_x = ground_x
        self.ground_y = ground_y
        self.sky_x = sky_x
        self.sky_y = sky_y

        try:
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
        except FileNotFoundError:
            print("Background files not found")

    def draw(self):
        self.screen.scr.blit(self.ground_surf, (self.ground_x, self.ground_y))
        self.screen.scr.blit(self.sky_surf, (self.sky_x, self.sky_y))

# Player
class Player():

    def __init__(self, screen, player_x, player_y):
        self.screen = screen

        try:
            self.player_surf = load_image(
                os.path.join(
                    os.path.dirname(__file__),
                    "graphics",
                    "player",
                    "player_stand.png"))
            self.player_rect = self.player_surf.get_rect(
                midbottom = (player_x, player_y))
        except FileNotFoundError:
            print("Player file not found")

    def draw(self):
        self.screen.scr.blit(self.player_surf, self.player_rect)

# Initialize Pygame
pygame.init()

# Create Objects
screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, "todo")
background = Background(screen, GROUND_X, GROUND_Y, SKY_X, SKY_Y)
player = Player(screen, PLAYER_X, PLAYER_Y)

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

    # Clock
    screen.clock.tick(screen.framerate)

# Exit
pygame.quit()
exit()
