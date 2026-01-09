"""
Helper functions for game utilities.
"""

import pygame
from utils.constants import (DEFAULT_COLOR, DEFAULT_SIZE)

# Load Image
def load_image(path, default_color=DEFAULT_COLOR, default_size=DEFAULT_SIZE) -> pygame.Surface:
    """
    Loads an image file with error handling and placeholder fallback.
    
    Args:
        path (str): File path to the image file.
        default_color (tuple): RGB color tuple for placeholder.
        default_size (tuple): Width and height for placeholder surface.
    
    Returns:
        pygame.Surface: Loaded image surface or placeholder surface if loading fails.
    """
    try:
        image = pygame.image.load(path).convert_alpha()
        return image
    except pygame.error as e:
        print(f"Error: {e}.")
    except FileNotFoundError:
        print(f"File not found in '{path}'.")

    placeholder = pygame.Surface(default_size)
    placeholder.fill(default_color)

    return placeholder
