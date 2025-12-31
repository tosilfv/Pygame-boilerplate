"""
Background management for the game.

This module handles loading and switching between different background
scenes (entrance and yard). It manages both ground and sky surfaces
and provides methods to switch between backgrounds when the player
reaches screen edges.
"""

import os
from utils.constants.constants import GROUND_X, GROUND_Y, SKY_X, SKY_Y
from utils.helpers import helpers

# Background
class Background():
    """
    Manages game backgrounds and scene transitions.
    
    The Background class loads and stores different background images
    (entrance and yard scenes) and handles switching between them when
    triggered by player movement. It uses the Mediator pattern to notify
    other game objects of background changes.
    
    Attributes:
        mediator: Mediator instance for inter-object communication.
        screen: Screen instance for drawing operations.
        ground_x (int): X coordinate for ground surface.
        ground_y (int): Y coordinate for ground surface.
        sky_x (int): X coordinate for sky surface.
        sky_y (int): Y coordinate for sky surface.
        current_background (str): Current background scene name ("entrance" or
        "yard").
        entrance_ground_surf: Surface for entrance ground.
        entrance_sky_surf: Surface for entrance sky.
        yard_ground_surf: Surface for yard ground.
        yard_sky_surf: Surface for yard sky.
        ground_surf: Currently active ground surface.
        sky_surf: Currently active sky surface.
    """

    def __init__(self, mediator, screen):
        self.mediator = mediator
        self.screen = screen
        self.ground_x = GROUND_X
        self.ground_y = GROUND_Y
        self.sky_x = SKY_X
        self.sky_y = SKY_Y
        self.current_background = "entrance"  # Track current background
        self.notify('Background was created.')

        # Initial background (entrance)
        self.entrance_ground_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "entrance_ground_normal.png"))
        self.entrance_sky_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "hotel_entrance_normal.png"))
        
        # Yard background
        self.yard_ground_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "entrance_ground_normal.png"))
        self.yard_sky_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "yard_normal.png"))
        
        # Set initial surfaces
        self.ground_surf = self.entrance_ground_surf
        self.sky_surf = self.entrance_sky_surf

    def switch_to_yard(self):
        """
        Switch the background to the yard scene.
        
        Changes the current background from entrance to yard if currently
        at entrance. Updates ground and sky surfaces accordingly and notifies
        the mediator of the change.
        """
        if self.current_background == "entrance":
            self.current_background = "yard"
            self.ground_surf = self.yard_ground_surf
            self.sky_surf = self.yard_sky_surf
            self.notify('Background switched to yard.')

    def switch_to_entrance(self):
        """
        Switch the background back to the entrance scene.
        
        Changes the current background from yard to entrance if currently
        at yard. Updates ground and sky surfaces accordingly and notifies
        the mediator of the change.
        """
        if self.current_background == "yard":
            self.current_background = "entrance"
            self.ground_surf = self.entrance_ground_surf
            self.sky_surf = self.entrance_sky_surf
            self.notify('Background switched to entrance.')

    def draw(self):
        """
        Draw the background surfaces to the screen.
        
        Blits both the ground and sky surfaces at their configured
        positions. Should be called every frame before drawing other
        game objects.
        """
        self.screen.scr.blit(self.ground_surf, (self.ground_x, self.ground_y))
        self.screen.scr.blit(self.sky_surf, (self.sky_x, self.sky_y))

    def notify(self, message):
        """
        Send a notification message through the mediator.
        
        Args:
            message (str): Message to send to the mediator.
        """
        self.mediator.notify(message)
