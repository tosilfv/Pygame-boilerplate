"""
Helper functions for game utilities.

This module provides utility functions used throughout the game, such as
image loading with error handling and placeholder generation.
"""

import pygame
from utils.constants.constants import ZERO

# Load Image
def load_image(path, default_color=(ZERO, 255, ZERO), default_size=(100, 100)):
    """
    Load an image file with error handling and placeholder fallback.
    
    Attempts to load an image file using pygame. If loading fails due to
    a pygame error or file not found, creates and returns a colored
    placeholder surface instead. This ensures the game continues running
    even if some assets are missing.
    
    Args:
        path (str): File path to the image file.
        default_color (tuple): RGB color tuple for placeholder (default:
        green).
        default_size (tuple): Width and height for placeholder surface.
    
    Returns:
        pygame.Surface: Loaded image surface or placeholder surface if loading
        fails.
    """
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
