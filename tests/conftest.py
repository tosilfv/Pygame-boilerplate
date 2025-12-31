import os
import pytest
import pygame

# Set dummy drivers for headless pygame testing
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

@pytest.fixture(autouse=True, scope="session")
def init_pygame():
    """Initialize pygame once for all tests"""
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def mock_screen():
    """Create a mock screen object"""
    from unittest.mock import Mock
    screen = Mock()
    screen.scr = Mock()
    screen.scr.blit = Mock()
    screen.clock = Mock()
    screen.clock.tick = Mock()
    screen.framerate = 60
    return screen

@pytest.fixture
def mediator():
    """Create a Mediator instance"""
    from control.mediator import Mediator
    return Mediator()

@pytest.fixture
def mock_image_loader(monkeypatch):
    """Mock image loader to return a simple surface"""
    def load_image_mock(path, default_color=(0, 255, 0),
                        default_size=(100, 100)):
        return pygame.Surface((100, 100))
    
    # Patch the load_image function in helpers.helpers module
    monkeypatch.setattr('utils.helpers.helpers.load_image', load_image_mock)
    return load_image_mock

@pytest.fixture
def mock_sound(monkeypatch):
    """Mock pygame mixer Sound"""
    from unittest.mock import Mock
    sound_mock = Mock()
    sound_mock.set_volume = Mock()
    sound_mock.play = Mock()
    
    def sound_init(path):
        return sound_mock
    
    monkeypatch.setattr(pygame.mixer, "Sound", sound_init)
    return sound_mock
