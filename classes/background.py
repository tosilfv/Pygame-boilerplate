import os
from utils.constants.constants import GROUND_X, GROUND_Y, SKY_X, SKY_Y
from utils.helpers import helpers

# Background
class Background():

    def __init__(self, mediator, screen):
        self.mediator = mediator
        self.screen = screen
        self.ground_x = GROUND_X
        self.ground_y = GROUND_Y
        self.sky_x = SKY_X
        self.sky_y = SKY_Y
        self.notify('Background was created.')

        self.ground_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "entrance_ground_normal.png"))
        self.sky_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel_entrance_normal.png"))

    def draw(self):
        self.screen.scr.blit(self.ground_surf, (self.ground_x, self.ground_y))
        self.screen.scr.blit(self.sky_surf, (self.sky_x, self.sky_y))

    def notify(self, message):
        self.mediator.notify(message)
