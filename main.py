"""
Main entry point for the Piccolo game.

This module initializes and runs the game loop, handling pygame events
and delegating game logic to the Game class. The game continues running
until the user closes the window.
"""

import pygame
from sys import exit
from control.game import game

# Variables
running = True

# Game Loop
if __name__ == "__main__":
    while running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

        # Run
        game.run()

    # Exit
    pygame.quit()
    exit()
