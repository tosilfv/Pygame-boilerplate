"""
Game constants and configuration values.

This module contains all game-wide constants including screen dimensions,
player settings, physics values, and positioning constants. Centralizing
these values makes the game easier to configure and maintain.
"""

# Movement Constants (defined first as they're used by other constants)
FIVE = 5
POINT_ONE = 0.1
TEN = 10
ZERO = 0

# Screen Configuration
CAPTION = "Piccolo"
FPS = 60  # Frames per second
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800

# Physics Constants
GRAVITY_MAX = -150
GROUND_LEVEL = 320

# Positioning Constants
GROUND_X = 0
GROUND_Y = GROUND_LEVEL
SKY_X = 0
SKY_Y = -120

# Player Configuration
PLAYER_X = 100
PLAYER_Y = GROUND_LEVEL + FIVE

# Screen Boundaries
SCREEN_LIMIT_L = 35
SCREEN_LIMIT_R = 40
