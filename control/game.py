"""
Main game controller and loop management.

This module contains the Game class which orchestrates the game loop,
coordinating drawing and updating of all game objects. It also creates
and initializes all game objects using the Mediator pattern.
"""

import pygame
from control.mediator import Mediator
from classes.screen import Screen
from classes.background import Background
from classes.player import Player

# Game
class Game:
    """
    Main game controller that manages the game loop.
    
    The Game class coordinates all game objects (screen, background, player)
    and runs the main game loop. It handles the drawing order, display updates,
    and object updates each frame. Uses the Mediator pattern for inter-object
    communication.
    
    Attributes:
        mediator: Mediator instance for inter-object communication.
        screen: Screen instance for display operations.
        background: Background instance for scene rendering.
        player: Player instance for character control.
    """

    def __init__(self, mediator, screen, background, player) -> None:
        self.mediator = mediator
        self.screen = screen
        self.background = background
        self.player = player
        self.notify('Game was created.')

    def run(self):
        """
        Execute one frame of the game loop.
        
        Performs the following operations in order:
        1. Draw background
        2. Draw player
        3. Update pygame display
        4. Update player state (input, physics, animation)
        5. Tick the game clock to maintain framerate
        
        Should be called continuously in the main game loop.
        """
        # Draw
        self.background.draw()
        self.player.draw()

        # Update
        pygame.display.update()
        self.player.update()

        # Clock
        self.screen.clock.tick(self.screen.framerate)

    def notify(self, message):
        """
        Send a notification message through the mediator.
        
        Args:
            message (str): Message to send to the mediator.
        """
        self.mediator.notify(message)


# Create Objects
mediator = Mediator()
screen = Screen(mediator)
background = Background(mediator, screen)
player = Player(mediator, screen, background)

# Create Game
game = Game(mediator, screen, background, player)
