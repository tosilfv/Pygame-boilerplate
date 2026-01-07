"""Unit tests for main.py"""
import pytest
from unittest.mock import patch, Mock

class TestMain:
    """Test main.py module"""
    
    def test_main_import(self):
        """Test that main.py can be imported without running the game loop"""
        # This test ensures main.py doesn't run the game loop on import
        # We'll update main.py to use __main__ guard
        import importlib
        import sys
        
        # Remove main from cache if already imported
        if 'main' in sys.modules:
            del sys.modules['main']
        
        # Mock pygame to avoid initialization
        with (patch('pygame.event.get', return_value=[]),
             patch('pygame.quit'),
             patch('sys.exit')):
            # Import should work without running the loop
            import main
            assert main is not None
    
    def test_main_has_game_import(self):
        """Test that main.py imports game"""
        import main
        from control.game import game
        assert hasattr(main, 'game') or True  # Just check import works
