"""Unit tests for Game class"""
from unittest.mock import patch

class TestGame:
    """Test Game class"""

    def test_game_initialization(self):
        """Test Game initialization"""
        from classes.background import Background
        from control.game import Game
        from unittest.mock import Mock

        mock_screen = Mock()
        background = Background(mock_screen)
        game = Game(mock_screen, background)

        assert game.screen == mock_screen
        assert game.background == background

    def test_game_run(self, monkeypatch):
        """Test Game run method"""
        from classes.background import Background
        from control.game import Game
        from unittest.mock import Mock

        mock_screen = Mock()
        background = Background(mock_screen)
        game = Game(mock_screen, background)


        # Mock pygame.display.update
        mock_update = Mock()
        monkeypatch.setattr('pygame.display.update', mock_update)

        # Reset mocks
        mock_screen.screen.blit.reset_mock()
        mock_screen.clock.tick.reset_mock()

        # Call run
        game.run()

        # Verify draw methods were called
        assert mock_screen.screen.blit.called  # Background draw

        # Verify update was called
        assert mock_update.called

    def test_game_run_calls_background_draw(self, monkeypatch):
        """Test that game.run calls background.draw"""
        from classes.background import Background
        from control.game import Game
        from unittest.mock import Mock

        mock_screen = Mock()
        background = Background(mock_screen)
        game = Game(mock_screen, background)

        # Mock pygame.display.update
        mock_update = Mock()
        monkeypatch.setattr('pygame.display.update', mock_update)

        # Mock background.draw to track calls
        with patch.object(background, 'draw') as mock_draw:
            game.run()
            mock_draw.assert_called_once()
