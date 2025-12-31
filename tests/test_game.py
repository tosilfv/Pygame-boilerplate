"""Unit tests for Game class"""
import pytest
from unittest.mock import Mock, patch

class TestGame:
    """Test Game class"""
    
    def test_game_initialization(self, mediator, mock_screen, mock_image_loader):
        """Test Game initialization"""
        from classes.background import Background
        from classes.player import Player
        from control.game import Game
        from unittest.mock import Mock
        
        background = Background(mediator, mock_screen)
        player = Player(mediator, mock_screen, background)
        
        game = Game(mediator, mock_screen, background, player)
        
        assert game.mediator == mediator
        assert game.screen == mock_screen
        assert game.background == background
        assert game.player == player
    
    def test_game_run(self, mediator, mock_screen, mock_image_loader, mock_sound, monkeypatch):
        """Test Game run method"""
        from classes.background import Background
        from classes.player import Player
        from control.game import Game
        
        background = Background(mediator, mock_screen)
        player = Player(mediator, mock_screen, background)
        game = Game(mediator, mock_screen, background, player)
        
        # Mock pygame.display.update
        mock_update = Mock()
        monkeypatch.setattr('pygame.display.update', mock_update)
        
        # Reset mocks
        mock_screen.scr.blit.reset_mock()
        mock_screen.clock.tick.reset_mock()
        
        game.run()
        
        # Verify draw methods were called
        assert mock_screen.scr.blit.called  # Background and player draw
        
        # Verify update was called
        assert mock_update.called
        
        # Verify clock tick was called
        mock_screen.clock.tick.assert_called_once_with(60)
    
    def test_game_notify(self, mediator, mock_screen, mock_image_loader):
        """Test Game notify method"""
        from classes.background import Background
        from classes.player import Player
        from control.game import Game
        
        background = Background(mediator, mock_screen)
        player = Player(mediator, mock_screen, background)
        game = Game(mediator, mock_screen, background, player)
        
        with patch.object(mediator, 'notify') as mock_notify:
            game.notify('Test message')
            mock_notify.assert_called_once_with('Test message')
    
    def test_game_run_calls_player_update(self, mediator, mock_screen, mock_image_loader, mock_sound, monkeypatch):
        """Test that game.run calls player.update"""
        from classes.background import Background
        from classes.player import Player
        from control.game import Game
        
        background = Background(mediator, mock_screen)
        player = Player(mediator, mock_screen, background)
        game = Game(mediator, mock_screen, background, player)
        
        # Mock pygame.display.update
        monkeypatch.setattr('pygame.display.update', Mock())
        
        # Mock player.update to track calls
        with patch.object(player, 'update') as mock_update:
            game.run()
            mock_update.assert_called_once()
    
    def test_game_run_calls_background_draw(self, mediator, mock_screen, mock_image_loader, mock_sound, monkeypatch):
        """Test that game.run calls background.draw"""
        from classes.background import Background
        from classes.player import Player
        from control.game import Game
        
        background = Background(mediator, mock_screen)
        player = Player(mediator, mock_screen, background)
        game = Game(mediator, mock_screen, background, player)
        
        # Mock pygame.display.update
        monkeypatch.setattr('pygame.display.update', Mock())
        
        # Mock background.draw to track calls
        with patch.object(background, 'draw') as mock_draw:
            game.run()
            mock_draw.assert_called_once()
    
    def test_game_run_calls_player_draw(self, mediator, mock_screen, mock_image_loader, mock_sound, monkeypatch):
        """Test that game.run calls player.draw"""
        from classes.background import Background
        from classes.player import Player
        from control.game import Game
        
        background = Background(mediator, mock_screen)
        player = Player(mediator, mock_screen, background)
        game = Game(mediator, mock_screen, background, player)
        
        # Mock pygame.display.update
        monkeypatch.setattr('pygame.display.update', Mock())
        
        # Mock player.draw to track calls
        with patch.object(player, 'draw') as mock_draw:
            game.run()
            mock_draw.assert_called_once()
