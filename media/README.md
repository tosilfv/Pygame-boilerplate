# Media Assets

This directory contains all media assets used in the Piccolo game.

## Directory Structure

### `audio/`
Contains sound effects and background music:
- `hyppy.mp3` - Jump sound effect
- `musa1.wav` - Background music

### `font/`
Contains font files:
- `Pixeltype.ttf` - Pixel-style font used in the game

### `graphics/`
Contains all visual assets organized by category:

#### `hotel/`
Background images for different hotel scenes:
- `entrance_ground_normal.png` - Ground surface for entrance scene
- `hotel_entrance_normal.png` - Sky/background for entrance scene
- `yard_normal.png` - Sky/background for yard scene
- `corridor1_normal.png`, `corridor1_large.png` - Corridor scene variants
- `corridor2_large.png` - Corridor scene variant 2
- `corridor3_normal.png`, `corridor3_large.png` - Corridor scene variant 3
- `elevator1_normal.png`, `elevator1_large.png` - Elevator scene
- `frontdesk_normal.png`, `frontdesk_large.png` - Front desk scene
- `yard_large.png`, `yard1_normal.png`, `yard1_large.png` - Yard scene variants

**Naming Convention:**
- `*_normal.png` - Standard resolution images
- `*_large.png` - Higher resolution images (for future use)

#### `items/`
Game item sprites:
- `bag1_normal.png`, `bag1_large.png` - Bag item (right-facing)
- `bag1_left_normal.png`, `bag1_left_large.png` - Bag item (left-facing)
- `bill1_normal.png`, `bill1_large.png` - Bill item
- `coin1_normal.png`, `coin1_large.png` - Coin item

#### `player/`
Player character sprites for different states and directions:
- `piccolo_stand_normal.png`, `piccolo_stand_large.png` - Standing
(right-facing)
- `piccolo_left_stand_normal.png`, `piccolo_left_stand_large.png` - Standing
(left-facing)
- `piccolo_walk1_normal.png`, `piccolo_walk1_large.png` - Walking frame 1
(right-facing)
- `piccolo_walk2_normal.png`, `piccolo_walk2_large.png` - Walking frame 2
(right-facing)
- `piccolo_left_walk1_normal.png`, `piccolo_left_walk1_large.png` - Walking
frame 1 (left-facing)
- `piccolo_left_walk2_normal.png`, `piccolo_left_walk2_large.png` - Walking
frame 2 (left-facing)
- `piccolo_jump_normal.png`, `piccolo_jump_large.png` - Jumping (right-facing)
- `piccolo_left_jump_normal.png`, `piccolo_left_jump_large.png` - Jumping
(left-facing)
- `piccolo_fell_normal.png`, `piccolo_fell_large.png` - Falling (right-facing)
- `piccolo_left_fell_normal.png`, `piccolo_left_fell_large.png` - Falling
(left-facing)
- `piccolo_trolley1_normal.png`, `piccolo_trolley1_large.png` - Trolley
frame 1 (right-facing)
- `piccolo_trolley2_normal.png`, `piccolo_trolley2_large.png` - Trolley
frame 2 (right-facing)
- `piccolo_left_trolley1_normal.png`, `piccolo_left_trolley1_large.png`
- Trolley frame 1 (left-facing)
- `piccolo_left_trolley2_normal.png`, `piccolo_left_trolley2_large.png`
- Trolley frame 2 (left-facing)

## Usage

All images are loaded using the `helpers.load_image()` function from
`utils/helpers/helpers.py`, which handles error cases by providing placeholder
surfaces if files are missing.

## License

See the `LICENCE` file in this directory for licensing information.
