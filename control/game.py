"""
Main game controller and loop management.
"""

import pygame
from classes.background import Background
from classes.screen import Screen

# Game
class Game:
    """
    Main game controller that manages the game loop.

    Attributes:
        screen: Screen instance for display operations.
        background: Background instance for scene rendering.
    """
    def __init__(self, screen, background) -> None:
        self.screen = screen
        self.background = background

    def run(self) -> None:
        """
        Executes one frame of the game loop.

        Performs the following operations in order:
        1. Draw background
        2. Update pygame display
        3. Tick the game clock to maintain framerate

        Should be called continuously in the main.py Game Loop.
        """

        # Draw
        self.background.draw()

        # Update
        pygame.display.update()

        # Clock
        self.screen.clock.tick(self.screen.framerate)

# Create Objects
_screen = Screen()
_background = Background(_screen)

# Create Game
game = Game(_screen, _background)
