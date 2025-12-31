"""
Screen management for the game.

This module handles the creation and configuration of the pygame display
window, including screen dimensions, framerate, and window caption.
"""

import pygame
from utils.constants.constants import CAPTION, FPS, SCREEN_HEIGHT, SCREEN_WIDTH

# Screen
class Screen():
    """
    Manages the game window and display settings.
    
    The Screen class initializes the pygame display surface, sets up
    the game clock for framerate control, and configures the window
    caption. It provides access to the display surface and clock
    for other game objects.
    
    Attributes:
        mediator: Mediator instance for inter-object communication.
        scr: Pygame display surface (the game window).
        clock: Pygame Clock object for framerate control.
        framerate (int): Target frames per second.
    """

    def __init__(self, mediator):
        self.mediator = mediator
        self.scr = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.framerate = FPS
        pygame.display.set_caption(CAPTION)
        self.notify('Screen was created.')

    def notify(self, message):
        """
        Send a notification message through the mediator.
        
        Args:
            message (str): Message to send to the mediator.
        """
        self.mediator.notify(message)
