"""Unit tests for utils module"""
import pygame

class TestConstants:
    """Test constants values"""

    def test_numeric_constants(self):
        """Test numeric constants"""
        from utils.constants import (ZERO)
        assert ZERO == 0

    def test_background_constants(self):
        """Test background constants"""
        import os
        from utils.constants import (GRAPHICS_PATH, GROUND_X, GROUND_Y, SKY_X,
                                     SKY_Y)
        assert GRAPHICS_PATH == os.path.join(
                    os.path.dirname(
                        os.path.dirname(
                            __file__)),
                                "media",
                                    "graphics")
        assert GROUND_X == 0
        assert GROUND_Y == 320
        assert SKY_X == 0
        assert SKY_Y == -120

    def test_default_constants(self):
        """Test default constants"""
        from utils.constants import (DEFAULT_COLOR, DEFAULT_SIZE)
        assert DEFAULT_COLOR == (0, 255, 0)
        assert DEFAULT_SIZE == (100, 100)

    def test_display_constants(self):
        """Test display constants"""
        from utils.constants import (CAPTION, DISPLAY_SIZE, FRAMERATE)
        assert CAPTION == "Piccolo2"
        assert DISPLAY_SIZE == (800, 400)
        assert FRAMERATE == 60

class TestHelpers:
    """Test helper functions"""
    def test_load_image_successful(self, tmp_path):
        """Test loading a valid image"""
        from utils.helpers import load_image

        # Create a temporary image file
        test_image = pygame.Surface((50, 50))
        test_image.fill((0, 0, 255))
        image_path = tmp_path / "test_img.png"
        pygame.image.save(test_image, str(image_path))

        # Load the image
        loaded = load_image(str(image_path))
        assert isinstance(loaded, pygame.Surface)
        assert loaded.get_size() == (50, 50)

    def test_load_image_not_found(self):
        """Test load_image when file doesn't exist"""
        from utils.helpers import load_image

        # Try to load a non-existent file
        res = load_image("non_existent_file.png")

        # Should return a placeholder surface
        assert isinstance(res, pygame.Surface)
        assert res.get_size() == (100, 100)  # Default size

    def test_load_image_pygame_error(self, monkeypatch):
        """Test load_image when pygame raises an error"""
        from utils.helpers import load_image

        # Mock pygame.image.load to raise an error
        def mock_load(path):
            raise pygame.error("Test error.")

        monkeypatch.setattr(pygame.image, "load", mock_load)

        # Should return a placeholder surface
        res = load_image("test.png")
        assert isinstance(res, pygame.Surface)
        assert res.get_size() == (100, 100)
