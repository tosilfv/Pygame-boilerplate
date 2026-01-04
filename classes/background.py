"""
Background management for the game.

This module handles loading and switching between different background
scenes (entrance and yard). It manages both ground and sky surfaces
and provides methods to switch between backgrounds when the player
reaches screen edges.
"""

import os
from utils.constants.constants import GROUND_X, GROUND_Y, SKY_X, SKY_Y
from utils.helpers import helpers

# Background
class Background():
    """
    Manages game backgrounds and scene transitions.
    
    The Background class loads and stores different background images
    (entrance and yard scenes) and handles switching between them when
    triggered by player movement. It uses the Mediator pattern to notify
    other game objects of background changes.
    
    Attributes:
        mediator: Mediator instance for inter-object communication.
        screen: Screen instance for drawing operations.
        ground_x (int): X coordinate for ground surface.
        ground_y (int): Y coordinate for ground surface.
        sky_x (int): X coordinate for sky surface.
        sky_y (int): Y coordinate for sky surface.
        mediator.current_bg (str): Current background scene name.
        entrance_ground_surf: Surface for entrance ground.
        entrance_sky_surf: Surface for entrance sky.
        yard_ground_surf: Surface for yard ground.
        yard_sky_surf: Surface for yard sky.
        ground_surf: Currently active ground surface.
        sky_surf: Currently active sky surface.
    """

    def __init__(self, mediator, screen):
        self.mediator = mediator
        self.screen = screen
        self.ground_x = GROUND_X
        self.ground_y = GROUND_Y
        self.sky_x = SKY_X
        self.sky_y = SKY_Y
        self.mediator.current_bg = "entrance"  # Track current background
        self.notify('Background was created.')

        # Initial background (entrance)
        self.entrance_ground_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "entrance_ground_normal.png"))
        self.entrance_sky_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "hotel_entrance_normal.png"))
        
        # Yard background
        self.yard_ground_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "entrance_ground_normal.png"))
        self.yard_sky_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "yard_normal.png"))
        
        # Frontdesk background
        self.frontdesk_ground_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "indoors_ground_large.png"))
        self.frontdesk_sky_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "frontdesk_large.png"))
        
        # Elevator lobby background
        self.elevator_lobby_ground_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "indoors_ground_large.png"))
        self.elevator_lobby_sky_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "elevator_lobby_large.png"))
        
        # Elevator open lobby background
        self.elevator_open_lobby_ground_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "indoors_ground_large.png"))
        self.elevator_open_lobby_sky_surf = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                "elevator_open_lobby_large.png"))
        
        # Elevator floor backgrounds (1-9)
        self.elevator_floor_ground_surfs = {}
        self.elevator_floor_sky_surfs = {}
        for floor_num in range(1, 10):
            floor_image_name = f"elevator_floor{floor_num}_large.png"
            floor_image_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                floor_image_name)
            # Only load if file exists (floors 1-2 may not exist)
            if os.path.exists(floor_image_path):
                self.elevator_floor_ground_surfs[floor_num] = \
                    helpers.load_image(
                    os.path.join(
                        os.path.dirname(os.path.dirname(__file__)),
                        "media",
                        "graphics",
                        "hotel",
                        "indoors_ground_large.png"))
                self.elevator_floor_sky_surfs[floor_num] = \
                    helpers.load_image(floor_image_path)
        
        # Elevator open floor backgrounds (1-9)
        self.elevator_open_floor_ground_surfs = {}
        self.elevator_open_floor_sky_surfs = {}
        for floor_num in range(1, 10):
            floor_open_image_name = f"elevator_open_floor{floor_num}_large.png"
            floor_open_image_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "hotel",
                floor_open_image_name)
            # Only load if file exists (floors 1-2 may not exist)
            if os.path.exists(floor_open_image_path):
                self.elevator_open_floor_ground_surfs[floor_num] = \
                    helpers.load_image(
                    os.path.join(
                        os.path.dirname(os.path.dirname(__file__)),
                        "media",
                        "graphics",
                        "hotel",
                        "indoors_ground_large.png"))
                self.elevator_open_floor_sky_surfs[floor_num] = \
                    helpers.load_image(floor_open_image_path)
        
        # Corridor backgrounds for floors 3-9 (corridors 1, 2, 3, 4)
        self.corridor_ground_surfs = {}  # {(floor_num, corridor_num): surface}
        self.corridor_sky_surfs = {}     # {(floor_num, corridor_num): surface}
        corridor_numbers = [1, 2, 3, 4]  # Corridors that exist
        for floor_num in range(3, 10):
            for corridor_num in corridor_numbers:
                if corridor_num == 2:
                    corridor_image_name = "corridor2_large.png"
                else:
                    corridor_image_name = \
                    f"rooms_floor{floor_num}_corridor{corridor_num}_large.png"
                corridor_image_path = os.path.join(
                    os.path.dirname(os.path.dirname(__file__)),
                    "media",
                    "graphics",
                    "hotel",
                    corridor_image_name)
                # Only load if file exists
                if os.path.exists(corridor_image_path):
                    self.corridor_ground_surfs[(floor_num, corridor_num)] = \
                        helpers.load_image(
                        os.path.join(
                            os.path.dirname(os.path.dirname(__file__)),
                            "media",
                            "graphics",
                            "hotel",
                            "indoors_ground_large.png"))
                    self.corridor_sky_surfs[(floor_num, corridor_num)] = \
                        helpers.load_image(corridor_image_path)
        
        # Track current floor and corridor for navigation
        self.current_floor = None  # Current floor number (3-9)
        self.current_corridor = None  # Current corridor number (1, 2, 3, 4, or None for elevator)
        
        # Set initial surfaces
        self.ground_surf = self.entrance_ground_surf
        self.sky_surf = self.entrance_sky_surf

    def switch_to_yard(self):
        """
        Switch the background to the yard scene.
        
        Changes the current background from entrance to yard if currently
        at entrance. Updates ground and sky surfaces accordingly and notifies
        the mediator of the change.
        """
        if self.mediator.current_bg == "entrance":
            self.mediator.current_bg = "yard"
            self.ground_surf = self.yard_ground_surf
            self.sky_surf = self.yard_sky_surf
            self.notify(f'Background switched to {self.mediator.current_bg}.')

    def switch_to_entrance(self):
        """
        Switch the background back to the entrance scene.
        
        Changes the current background from yard or frontdesk to entrance if
        currently at yard or frontdesk. Updates ground and sky surfaces
        accordingly and notifies the mediator of the change.
        """
        if self.mediator.current_bg == "yard" or \
                self.mediator.current_bg == "frontdesk":
            self.mediator.current_bg = "entrance"
            self.ground_surf = self.entrance_ground_surf
            self.sky_surf = self.entrance_sky_surf
            self.notify(f'Background switched to {self.mediator.current_bg}.')

    def switch_to_frontdesk(self):
        """
        Switch the background to the frontdesk scene.
        
        Changes the current background from entrance or elevator_lobby to
        frontdesk if currently at entrance or elevator_lobby. Updates ground
        and sky surfaces accordingly and notifies the mediator of the change.
        """
        if self.mediator.current_bg == "entrance" or \
                self.mediator.current_bg == "elevator_lobby":
            self.mediator.current_bg = "frontdesk"
            self.ground_surf = self.frontdesk_ground_surf
            self.sky_surf = self.frontdesk_sky_surf
            self.notify(f'Background switched to {self.mediator.current_bg}.')

    def switch_to_elevator_lobby(self):
        """
        Switch the background to the elevator lobby scene.
        
        Changes the current background from frontdesk or any elevator_open
        background to elevator lobby if currently at frontdesk or any
        elevator_open background. Updates ground and sky surfaces accordingly
        and notifies the mediator of the change.
        """
        is_elevator_open = (self.mediator.current_bg == "elevator_open_lobby" or
                    self.mediator.current_bg.startswith("elevator_open_floor"))
        
        if self.mediator.current_bg == "frontdesk" or is_elevator_open:
            self.mediator.current_bg = "elevator_lobby"
            self.ground_surf = self.elevator_lobby_ground_surf
            self.sky_surf = self.elevator_lobby_sky_surf
            self.notify(f'Background switched to {self.mediator.current_bg}.')

    def switch_to_elevator_open_lobby(self):
        """
        Switch the background to the elevator open lobby scene.
        
        Changes the current background from elevator_lobby to
        elevator_open_lobby if currently at elevator_lobby. Updates ground and
        sky surfaces accordingly and notifies the mediator of the change.
        """
        if self.mediator.current_bg == "elevator_lobby":
            self.mediator.current_bg = "elevator_open_lobby"
            self.ground_surf = self.elevator_open_lobby_ground_surf
            self.sky_surf = self.elevator_open_lobby_sky_surf
            self.notify(f'Background switched to {self.mediator.current_bg}.')

    def switch_to_elevator_floor(self, floor_num):
        """
        Switch the background to the specified elevator floor scene.
        
        Changes the current background from any elevator_open background or
        corridor to elevator_floor{floor_num} if the floor background exists.
        Updates ground and sky surfaces accordingly and notifies the mediator
        of the change.
        
        Args:
            floor_num (int): Floor number (1-9).
        """
        # Check if current background is any elevator_open background or a corridor on the same floor
        is_elevator_open = (self.mediator.current_bg == "elevator_open_lobby" or
                    self.mediator.current_bg.startswith("elevator_open_floor"))
        is_corridor_on_same_floor = \
                        (self.mediator.current_bg.startswith("corridor") and
                            self.current_floor == floor_num)
        
        if ((is_elevator_open or is_corridor_on_same_floor) and 
            floor_num in self.elevator_floor_ground_surfs and 
            floor_num in self.elevator_floor_sky_surfs):
            self.mediator.current_bg = f"elevator_floor{floor_num}"
            self.ground_surf = self.elevator_floor_ground_surfs[floor_num]
            self.sky_surf = self.elevator_floor_sky_surfs[floor_num]
            self.current_floor = floor_num
            self.current_corridor = None  # At elevator, not in corridor
            self.notify(f'Background switched to {self.mediator.current_bg}.')
    
    def switch_to_elevator_open_floor(self, floor_num):
        """
        Switch the background to the specified elevator open floor scene.
        
        Changes the current background from elevator_floor{floor_num} to
        elevator_open_floor{floor_num} if currently at that floor and the open
        floor background exists. Updates ground and sky surfaces accordingly
        and notifies the mediator of the change.
        
        Args:
            floor_num (int): Floor number (1-9).
        """
        if (self.mediator.current_bg == f"elevator_floor{floor_num}" and 
            floor_num in self.elevator_open_floor_ground_surfs and 
            floor_num in self.elevator_open_floor_sky_surfs):
            self.mediator.current_bg = f"elevator_open_floor{floor_num}"
            self.ground_surf = self.elevator_open_floor_ground_surfs[floor_num]
            self.sky_surf = self.elevator_open_floor_sky_surfs[floor_num]
            self.current_floor = floor_num
            self.current_corridor = None  # At elevator, not in corridor
            self.notify(f'Background switched to {self.mediator.current_bg}.')
    
    def switch_to_corridor(self, floor_num, corridor_num):
        """
        Switch the background to the specified corridor scene.
        
        Changes the current background to corridor{corridor_num} on
        floor{floor_num} if the corridor background exists. Updates ground and
        sky surfaces accordingly and notifies the mediator of the change.
        
        Args:
            floor_num (int): Floor number (3-9).
            corridor_num (int): Corridor number (1, 3, or 4).
        """
        if (floor_num, corridor_num) in self.corridor_ground_surfs and \
           (floor_num, corridor_num) in self.corridor_sky_surfs:
            self.mediator.current_bg = \
                f"corridor{corridor_num}_floor{floor_num}"
            self.ground_surf = \
                self.corridor_ground_surfs[(floor_num, corridor_num)]
            self.sky_surf = self.corridor_sky_surfs[(floor_num, corridor_num)]
            self.current_floor = floor_num
            self.current_corridor = corridor_num
            self.notify(f'Background switched to {self.mediator.current_bg}.')
    
    def get_available_corridors(self, floor_num):
        """
        Get list of available corridor numbers for a given floor.
        
        Args:
            floor_num (int): Floor number (3-9).
        
        Returns:
            list: Sorted list of available corridor numbers for the floor.
        """
        available = []
        for corridor_num in [1, 2, 3, 4]:  # Check all possible corridors
            if (floor_num, corridor_num) in self.corridor_ground_surfs:
                available.append(corridor_num)
        return sorted(available)
    
    def get_next_corridor_right(self, floor_num, current_corridor):
        """
        Get the next corridor number when moving right.
        
        Args:
            floor_num (int): Floor number (3-9).
            current_corridor (int or None): Current corridor number, or None if at elevator.
        
        Returns:
            int or None: Next corridor number, or None if should go back to elevator.
        """
        available = self.get_available_corridors(floor_num)
        if not available:
            return None
        
        if current_corridor is None:
            # At elevator, go to first corridor
            return available[0]
        
        # Find current corridor index
        try:
            current_index = available.index(current_corridor)
            if current_index < len(available) - 1:
                # Move to next corridor
                return available[current_index + 1]
            else:
                # At last corridor, go back to elevator
                return None
        except ValueError:
            # Current corridor not in available list, go to first
            return available[0]
    
    def get_next_corridor_left(self, floor_num, current_corridor):
        """
        Get the next corridor number when moving left.
        
        Args:
            floor_num (int): Floor number (3-9).
            current_corridor (int or None): Current corridor number, or None if at elevator.
        
        Returns:
            int or None: Next corridor number, or None if should go back to elevator.
        """
        available = self.get_available_corridors(floor_num)
        if not available:
            return None
        
        if current_corridor is None:
            # At elevator, go to last corridor
            return available[-1]
        
        # Find current corridor index
        try:
            current_index = available.index(current_corridor)
            if current_index > 0:
                # Move to previous corridor
                return available[current_index - 1]
            else:
                # At first corridor, go back to elevator
                return None
        except ValueError:
            # Current corridor not in available list, go to last
            return available[-1]

    def draw(self):
        """
        Draw the background surfaces to the screen.
        
        Blits both the ground and sky surfaces at their configured positions.
        Should be called every frame before drawing other game objects.
        """
        self.screen.scr.blit(self.ground_surf, (self.ground_x, self.ground_y))
        self.screen.scr.blit(self.sky_surf, (self.sky_x, self.sky_y))

    def change_background(self, background):
        """
        Change background throught the mediator.
        
        Args:
            background (str): Background to send to the mediator.
        """
        self.mediator.current_bg(background)

    def notify(self, message):
        """
        Send a notification message through the mediator.
        
        Args:
            message (str): Message to send to the mediator.
        """
        self.mediator.notify(message)
