"""
Background for the game.
"""

import os
from utils.constants import (GRAPHICS_PATH, GROUND_X, GROUND_Y, SKY_X, SKY_Y)
from utils.helpers import load_image

# Background
class Background:
    """
    Game backgrounds.

    Attributes:
        screen: Screen instance for drawing operations.
        entrance_ground_surf: Ground surface for entrance scene.
        entrance_sky_surf: Sky surface for entrance scene.
    """
    def __init__(self, screen) -> None:
        self.screen = screen

        # Initial background (entrance)
        self.entrance_ground_surf = load_image(
            os.path.join(GRAPHICS_PATH,
                "hotel",
                "outdoor_ground_normal.png"))
        self.entrance_sky_surf = load_image(
            os.path.join(GRAPHICS_PATH,
                "hotel",
                "entrance_normal.png"))

        # Set initial surfaces
        self.ground_surf = self.entrance_ground_surf
        self.sky_surf = self.entrance_sky_surf

    def draw(self) -> None:
        """
        Draw the background ground and sky sufraces to the screen.
        """
        self.screen.screen.blit(self.ground_surf, (GROUND_X, GROUND_Y))
        self.screen.screen.blit(self.sky_surf, (SKY_X, SKY_Y))
