"""Unit tests for main.py"""
from unittest.mock import patch

class TestMain:
    """Test main.py module"""

    def test_main_import(self):
        """Test that main.py can be imported without running the game loop"""
        import sys

        # Remove main from cache if it is already imported
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
        assert hasattr(main, 'game')
        
    def test_main_has_running_import(self):
        """Test that main.py imports running variable"""
        import main
        from utils.variables import (running)
        assert hasattr(main, 'running')
