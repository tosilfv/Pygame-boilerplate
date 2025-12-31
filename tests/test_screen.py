"""Unit tests for Screen class"""
import pytest
from unittest.mock import Mock, patch

class TestScreen:
    """Test Screen class"""
    
    def test_screen_initialization(self, mediator, monkeypatch):
        """Test Screen initialization"""
        from classes.screen import Screen
        
        # Mock pygame display functions
        mock_display = Mock()
        mock_clock = Mock()
        mock_clock.tick = Mock()
        
        monkeypatch.setattr('pygame.display.set_mode', lambda size: mock_display)
        monkeypatch.setattr('pygame.display.set_caption', Mock())
        monkeypatch.setattr('pygame.time.Clock', lambda: mock_clock)
        
        screen = Screen(mediator)
        
        assert screen.mediator == mediator
        assert screen.scr == mock_display
        assert screen.clock == mock_clock
        assert screen.framerate == 60
    
    def test_screen_set_caption(self, mediator, monkeypatch):
        """Test that screen sets caption correctly"""
        from classes.screen import Screen
        from utils.constants.constants import CAPTION
        
        set_caption_called = []
        
        def mock_set_caption(caption):
            set_caption_called.append(caption)
        
        monkeypatch.setattr('pygame.display.set_mode', lambda size: Mock())
        monkeypatch.setattr('pygame.display.set_caption', mock_set_caption)
        monkeypatch.setattr('pygame.time.Clock', lambda: Mock())
        
        Screen(mediator)
        
        assert CAPTION in set_caption_called
    
    def test_screen_notify(self, mediator, monkeypatch):
        """Test screen notification"""
        from classes.screen import Screen
        
        monkeypatch.setattr('pygame.display.set_mode', lambda size: Mock())
        monkeypatch.setattr('pygame.display.set_caption', Mock())
        monkeypatch.setattr('pygame.time.Clock', lambda: Mock())
        
        screen = Screen(mediator)
        
        with patch.object(mediator, 'notify') as mock_notify:
            screen.notify('Test message')
            mock_notify.assert_called_once_with('Test message')
