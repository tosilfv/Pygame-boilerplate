"""
Main entry point for the Piccolo2 game.

This module initializes and runs the game loop and delegates game logic
to the Game class. The game continues running until the user closes the window.
"""

import pygame
from sys import exit
from control.game import game
running = True

# Game Loop
if __name__ == "__main__":
    while running:

        # Event Loop
        for event in pygame.event.get():
            # Stop Running
            if event.type == pygame.QUIT:
                running = False

        # Run
        game.run()

    # Quit and Exit
    pygame.quit()
    exit()
