"""Unit tests for utils module"""
import pytest
import pygame
from unittest.mock import Mock, patch

class TestConstants:
    """Test constants values"""
    
    def test_screen_dimensions(self):
        """Test screen width and height constants"""
        from utils.constants.constants import SCREEN_WIDTH, SCREEN_HEIGHT
        assert SCREEN_WIDTH == 800
        assert SCREEN_HEIGHT == 400
    
    def test_gravity_constants(self):
        """Test gravity-related constants"""
        from utils.constants.constants import GRAVITY_MAX, GROUND_LEVEL
        assert GRAVITY_MAX == -150
        assert GROUND_LEVEL == 320
    
    def test_player_constants(self):
        """Test player-related constants"""
        from utils.constants.constants import PLAYER_X, PLAYER_Y, FIVE
        assert PLAYER_X == 100
        assert PLAYER_Y == 325  # GROUND_LEVEL + FIVE
        assert FIVE == 5
    
    def test_screen_limits(self):
        """Test screen limit constants"""
        from utils.constants.constants import SCREEN_LIMIT_L, SCREEN_LIMIT_R
        assert SCREEN_LIMIT_L == 35
        assert SCREEN_LIMIT_R == 40
    
    def test_numeric_constants(self):
        """Test numeric constants"""
        from utils.constants.constants import ZERO, TEN, POINT_ONE
        assert ZERO == 0
        assert TEN == 10
        assert POINT_ONE == 0.1

class TestHelpers:
    """Test helper functions"""
    
    def test_load_image_success(self, tmp_path):
        """Test loading a valid image"""
        from utils.helpers.helpers import load_image
        
        # Create a temporary image file
        test_image = pygame.Surface((50, 50))
        test_image.fill((255, 0, 0))
        image_path = tmp_path / "test_image.png"
        pygame.image.save(test_image, str(image_path))
        
        # Load the image
        loaded = load_image(str(image_path))
        assert isinstance(loaded, pygame.Surface)
        assert loaded.get_size() == (50, 50)
    
    def test_load_image_file_not_found(self):
        """Test load_image when file doesn't exist"""
        from utils.helpers.helpers import load_image
        
        # Try to load non-existent file
        result = load_image("nonexistent_file.png")
        
        # Should return a placeholder surface
        assert isinstance(result, pygame.Surface)
        assert result.get_size() == (100, 100)  # default_size
    
    def test_load_image_pygame_error(self, monkeypatch):
        """Test load_image when pygame raises an error"""
        from utils.helpers.helpers import load_image
        
        # Mock pygame.image.load to raise an error
        def mock_load(path):
            raise pygame.error("Test error")
        
        monkeypatch.setattr(pygame.image, "load", mock_load)
        
        # Should return a placeholder surface
        result = load_image("test.png")
        assert isinstance(result, pygame.Surface)
        assert result.get_size() == (100, 100)
