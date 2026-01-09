# Media Assets

This directory contains all media assets used in the Piccolo2 game.

**Naming Convention:**
- `*_normal.png` - Standard resolution images
- `*_large.png` - Higher resolution images (for indoor scenes)

## Usage

All images are loaded using the `helpers.load_image()` function from
`utils/helpers.py`, which handles error cases by providing placeholder
surfaces if files are missing.

## License

See the `LICENCE` file in this directory for licensing information.

## Directory Structure

### `graphics/`
Contains all visual assets organized by category:

#### `hotel/`
Background images for different hotel scenes:
- `entrance_normal.png` - Sky surface for entrance scene
- `outdoor_ground_normal.png` - Ground surface for outdoor scenes
