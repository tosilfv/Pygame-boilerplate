"""
Game constants and configuration values.
"""

import os

# Numeric
ZERO = 0

# Background
GRAPHICS_PATH = os.path.join(
                    os.path.dirname(
                        os.path.dirname(
                            __file__)),
                                "media",
                                    "graphics")
GROUND_X = ZERO
GROUND_Y = 320
SKY_X = ZERO
SKY_Y = -120

# Default
DEFAULT_COLOR = (0, 255, 0)  # Green
DEFAULT_SIZE = (100, 100)

# Display
CAPTION = "Piccolo2"
DISPLAY_SIZE = (800, 400)
FRAMERATE = 60
