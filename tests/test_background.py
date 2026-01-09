"""Unit tests for Background class"""
from unittest.mock import Mock

class TestBackground:
    """Test Background class"""

    def test_background_initialization(self):
        """Test Background initialization"""
        from classes.background import Background

        mock_screen = Mock()
        background = Background(mock_screen)

        assert background.screen == mock_screen
        assert background.ground_surf is not None
        assert background.sky_surf is not None
    
    def test_background_draw(self):
        """Test background draw method"""
        from classes.background import Background

        mock_screen = Mock()
        background = Background(mock_screen)
        background.draw()

        # Verify blit was called twice (once for groud and sky)
        assert mock_screen.screen.blit.call_count == 2
