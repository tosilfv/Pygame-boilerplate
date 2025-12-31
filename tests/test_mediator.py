"""Unit tests for Mediator class"""
import pytest
from unittest.mock import patch

class TestMediator:
    """Test Mediator class"""
    
    def test_mediator_initialization(self, capsys):
        """Test Mediator initialization"""
        from control.mediator import Mediator
        
        mediator = Mediator()
        
        assert mediator.message == "Mediator was created."
        # Check that message was printed
        captured = capsys.readouterr()
        assert "Mediator was created." in captured.out
    
    def test_mediator_notify(self, capsys):
        """Test Mediator notify method"""
        from control.mediator import Mediator
        
        mediator = Mediator()
        mediator.notify("Test notification")
        
        assert mediator.message == "Test notification"
        # Check that message was printed
        captured = capsys.readouterr()
        assert "Test notification" in captured.out
    
    def test_mediator_multiple_notifications(self, capsys):
        """Test multiple notifications"""
        from control.mediator import Mediator
        
        mediator = Mediator()
        mediator.notify("First message")
        mediator.notify("Second message")
        mediator.notify("Third message")
        
        assert mediator.message == "Third message"
        # Check that all messages were printed
        captured = capsys.readouterr()
        assert "First message" in captured.out
        assert "Second message" in captured.out
        assert "Third message" in captured.out
    
    def test_mediator_print_message(self, capsys):
        """Test print_message method"""
        from control.mediator import Mediator
        
        mediator = Mediator()
        mediator.message = "Custom message"
        mediator.print_message()
        
        captured = capsys.readouterr()
        assert "Custom message" in captured.out
