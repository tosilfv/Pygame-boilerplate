"""Unit tests for Background class"""
import pytest
from unittest.mock import Mock, patch

class TestBackground:
    """Test Background class"""
    
    def test_background_initialization(self, mediator, mock_screen,
                                       mock_image_loader):
        """Test Background initialization"""
        from classes.background import Background
        
        background = Background(mediator, mock_screen)
        
        assert background.mediator == mediator
        assert background.screen == mock_screen
        assert background.current_background == "entrance"
        assert background.ground_surf is not None
        assert background.sky_surf is not None
    
    def test_background_switch_to_yard(self, mediator, mock_screen,
                                       mock_image_loader):
        """Test switching background to yard"""
        from classes.background import Background
        
        background = Background(mediator, mock_screen)
        assert background.current_background == "entrance"
        
        background.switch_to_yard()
        
        assert background.current_background == "yard"
        assert background.ground_surf == background.yard_ground_surf
        assert background.sky_surf == background.yard_sky_surf
    
    def test_background_switch_to_entrance(self, mediator, mock_screen,
                                           mock_image_loader):
        """Test switching background back to entrance"""
        from classes.background import Background
        
        background = Background(mediator, mock_screen)
        background.switch_to_yard()
        assert background.current_background == "yard"
        
        background.switch_to_entrance()
        
        assert background.current_background == "entrance"
        assert background.ground_surf == background.entrance_ground_surf
        assert background.sky_surf == background.entrance_sky_surf
    
    def test_background_switch_to_yard_no_change_if_already_yard(self,
                                    mediator, mock_screen, mock_image_loader):
        """Test that switch_to_yard doesn't change if already yard"""
        from classes.background import Background
        
        background = Background(mediator, mock_screen)
        background.switch_to_yard()
        yard_sky = background.sky_surf
        
        # Try to switch to yard again
        background.switch_to_yard()
        
        # Should still be yard with same surfaces
        assert background.current_background == "yard"
        assert background.sky_surf == yard_sky
    
    def test_background_switch_to_entrance_no_change_if_already_entrance(self,
                                    mediator, mock_screen, mock_image_loader):
        """Test that switch_to_entrance doesn't change if already entrance"""
        from classes.background import Background
        
        background = Background(mediator, mock_screen)
        entrance_sky = background.sky_surf
        
        # Try to switch to entrance again
        background.switch_to_entrance()
        
        # Should still be entrance with same surfaces
        assert background.current_background == "entrance"
        assert background.sky_surf == entrance_sky
    
    def test_background_draw(self, mediator, mock_screen, mock_image_loader):
        """Test background draw method"""
        from classes.background import Background
        
        background = Background(mediator, mock_screen)
        background.draw()
        
        # Verify blit was called twice (ground and sky)
        assert mock_screen.scr.blit.call_count == 2
    
    def test_background_notify(self, mediator, mock_screen, mock_image_loader):
        """Test background notification"""
        from classes.background import Background
        
        background = Background(mediator, mock_screen)
        
        # The notify method should call mediator.notify
        with patch.object(mediator, 'notify') as mock_notify:
            background.notify('Test message')
            mock_notify.assert_called_once_with('Test message')
