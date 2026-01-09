"""Unit tests for Screen class"""
from unittest.mock import Mock

class TestScreen:
    """Test Screen class"""

    def test_screen_initialization(self, monkeypatch):
        """Test Screen initialization"""
        from classes.screen import Screen
        from utils.constants import (FRAMERATE)

        # Mock pygame display functions
        mock_display = Mock()
        mock_clock = Mock()
        mock_clock.tick = Mock()

        monkeypatch.setattr('pygame.display.set_mode', lambda size: mock_display)
        monkeypatch.setattr('pygame.display.set_caption', Mock())
        monkeypatch.setattr('pygame.time.Clock', lambda: mock_clock)

        screen = Screen()

        assert screen.screen == mock_display
        assert screen.clock == mock_clock
        assert screen.framerate == FRAMERATE

    def test_screen_set_caption(self, monkeypatch):
        """Test that screen sets caption correctly"""
        from classes.screen import Screen
        from utils.constants import (CAPTION)

        set_caption_called = []

        def mock_set_caption(caption):
            set_caption_called.append(caption)

        monkeypatch.setattr('pygame.display.set_mode', lambda size: Mock())
        monkeypatch.setattr('pygame.display.set_caption', mock_set_caption)
        monkeypatch.setattr('pygame.time.Clock', lambda: Mock())

        Screen()

        assert CAPTION in set_caption_called
        