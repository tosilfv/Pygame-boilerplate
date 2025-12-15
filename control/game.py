import pygame
from control.mediator import Mediator
from classes.screen import Screen
from classes.background import Background
from classes.player import Player

# Game
class Game:

    def __init__(self, mediator, screen, background, player) -> None:
        self.mediator = mediator
        self.screen = screen
        self.background = background
        self.player = player
        self.notify('Game was created.')

    def run(self):
        # Draw
        self.background.draw()
        self.player.draw()

        # Update
        pygame.display.update()
        self.player.update()

        # Clock
        game.screen.clock.tick(game.screen.framerate)

    def notify(self, message):
        self.mediator.notify(message)


# Create Objects
mediator = Mediator()
screen = Screen(mediator)
background = Background(mediator, screen)
player = Player(mediator, screen)

# Create Game
game = Game(mediator, screen, background, player)
