"""Unit tests for Player class"""
import pytest
from unittest.mock import Mock, patch, MagicMock
import pygame
from utils.constants.constants import SCREEN_WIDTH, SCREEN_LIMIT_R, SCREEN_LIMIT_L, TEN, GROUND_LEVEL, FIVE

class TestPlayer:
    """Test Player class"""
    
    def test_player_initialization(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test Player initialization"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        
        assert player.mediator == mediator
        assert player.screen == mock_screen
        assert player.moving_horizontally == False
        assert player.moving_up == False
        assert player.moving_down == False
        assert player.gravity == 0
        assert player.facing_left == False
        assert player.player_x == 100  # PLAYER_X
        assert player.image is not None
    
    def test_player_rect_properties(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player rect properties"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        
        # Test rect_x property
        assert isinstance(player.rect_x, (int, float))
        
        # Test rect_y property and setter
        original_y = player.rect_y
        player.rect_y = 200
        assert player.rect_y == 200
        assert player.rect.y == 200
    
    def test_player_move_left(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player movement to the left"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        initial_x = player.player_x
        
        # Mock pygame.key.get_pressed to return LEFT key pressed
        with patch('pygame.key.get_pressed', return_value={pygame.K_LEFT: True, pygame.K_RIGHT: False, pygame.K_SPACE: False}):
            player.player_input()
        
        assert player.player_x < initial_x
        assert player.moving_horizontally == True
        assert player.facing_left == True
    
    def test_player_move_right(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player movement to the right"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        initial_x = player.player_x
        
        # Mock pygame.key.get_pressed to return RIGHT key pressed
        with patch('pygame.key.get_pressed', return_value={pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False}):
            player.player_input()
        
        assert player.player_x > initial_x
        assert player.moving_horizontally == True
        assert player.facing_left == False
    
    def test_player_jump(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player jump"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        player.rect.bottom = GROUND_LEVEL + FIVE  # On ground
        
        # Mock pygame.key.get_pressed to return SPACE key pressed
        with patch('pygame.key.get_pressed', return_value={pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: True}):
            player.player_input()
        
        assert player.moving_up == True
        mock_sound.play.assert_called()
    
    def test_player_apply_gravity_jump(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test gravity application during jump"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        player.moving_up = True
        player.gravity = 0
        initial_bottom = player.rect.bottom
        
        player.apply_gravity()
        
        # Gravity should be negative (moving up)
        assert player.gravity < 0
        # Rect should move up
        assert player.rect.bottom < initial_bottom
    
    def test_player_apply_gravity_fall(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test gravity application during fall"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        player.moving_down = True
        player.gravity = -100  # Already at max
        player.rect.bottom = 200  # Above ground
        
        player.apply_gravity()
        
        # Gravity should increase (moving down)
        assert player.gravity > -100
    
    def test_player_apply_gravity_ground(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test gravity reset when player reaches ground"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        player.moving_down = True
        player.gravity = 50
        player.rect.bottom = GROUND_LEVEL + FIVE
        
        player.apply_gravity()
        
        # Should reset gravity and stop moving down
        assert player.gravity == 0
        assert player.moving_down == False
        assert player.rect.bottom == GROUND_LEVEL + FIVE
    
    def test_player_animate_jump(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player animation during jump"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        player.rect.bottom = GROUND_LEVEL - 10  # In air
        player.facing_left = False
        
        player.animate()
        
        # Should show jump image
        assert player.image == player.jump_image
    
    def test_player_animate_walk(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player animation during walk"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        player.rect.bottom = GROUND_LEVEL + FIVE  # On ground
        player.moving_horizontally = True
        player.walk_index = 0
        
        player.animate()
        
        # Should show walking animation
        assert player.image in player.walking
    
    def test_player_animate_stand(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player animation when standing"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        player.rect.bottom = GROUND_LEVEL + FIVE  # On ground
        player.moving_horizontally = False
        
        player.animate()
        
        # Should show stand image
        assert player.image == player.stand_image
    
    def test_player_draw(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player draw method"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        player.draw()
        
        # Verify blit was called
        mock_screen.scr.blit.assert_called_once()
    
    def test_player_update(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player update method"""
        from classes.player import Player
        
        player = Player(mediator, mock_screen)
        
        with (patch.object(player, 'player_input') as mock_input,
             patch.object(player, 'apply_gravity') as mock_gravity,
             patch.object(player, 'animate') as mock_animate):
            player.update()
            
            mock_input.assert_called_once()
            mock_gravity.assert_called_once()
            mock_animate.assert_called_once()
    
    def test_player_edge_detection_right(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player edge detection on right side"""
        from classes.background import Background
        from classes.player import Player
        
        background = Background(mediator, mock_screen)
        player = Player(mediator, mock_screen, background)
        player.player_x = SCREEN_WIDTH - SCREEN_LIMIT_R + 1
        player.prev_player_x = SCREEN_WIDTH - SCREEN_LIMIT_R
        
        # Mock keys to move right
        with patch('pygame.key.get_pressed', return_value={pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False}):
            player.player_input()
        
        # Should be clamped to limit
        assert player.player_x <= SCREEN_WIDTH - SCREEN_LIMIT_R
    
    def test_player_edge_detection_left(self, mediator, mock_screen, mock_image_loader, mock_sound):
        """Test player edge detection on left side"""
        from classes.background import Background
        from classes.player import Player
        
        background = Background(mediator, mock_screen)
        player = Player(mediator, mock_screen, background)
        player.player_x = SCREEN_LIMIT_L - 1
        player.prev_player_x = SCREEN_LIMIT_L
        
        # Mock keys to move left
        with patch('pygame.key.get_pressed', return_value={pygame.K_LEFT: True, pygame.K_RIGHT: False, pygame.K_SPACE: False}):
            player.player_input()
        
        # Should be clamped to limit
        assert player.player_x >= SCREEN_LIMIT_L
