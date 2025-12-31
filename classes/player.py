"""
Player character implementation for the Piccolo game.

This module handles all player-related functionality including movement,
jumping, gravity, animation, and sound effects. The player can move
horizontally, jump, and trigger background changes when reaching screen
edges.
"""

import pygame
import os
from utils.constants.constants import FIVE, GRAVITY_MAX, GROUND_LEVEL,\
    PLAYER_X, PLAYER_Y, POINT_ONE, SCREEN_WIDTH, SCREEN_LIMIT_L,\
    SCREEN_LIMIT_R, TEN, ZERO
from utils.helpers import helpers

# Initialize Pygame
pygame.init()

# Player
class Player():
    """
    Represents the player character (Piccolo) in the game.
    
    The Player class handles all player interactions including keyboard
    input, movement, jumping with gravity physics, animation states,
    and sound effects. It communicates with the Background class to
    trigger scene transitions when reaching screen edges.
    
    Attributes:
        mediator: Mediator instance for inter-object communication.
        screen: Screen instance for drawing operations.
        background: Background instance for scene transition triggers.
        moving_horizontally (bool): Whether player is currently moving left/right.
        moving_up (bool): Whether player is currently jumping upward.
        moving_down (bool): Whether player is currently falling downward.
        gravity (int): Current gravity value affecting vertical movement.
        player_x (int): Current X position of the player.
        player_y (int): Current Y position of the player.
        walk_index (float): Animation index for walking animation.
        facing_left (bool): Whether player is facing left.
        prev_player_x (int): Previous X position for edge detection.
        jump_image: Surface for jump animation (right-facing).
        stand_image: Surface for standing animation (right-facing).
        walking: List of surfaces for walking animation (right-facing).
        jump_image_left: Surface for jump animation (left-facing).
        stand_image_left: Surface for standing animation (left-facing).
        walking_left: List of surfaces for walking animation (left-facing).
        image: Currently active image surface.
        rect: Pygame Rect object for collision detection and positioning.
        music: Background music sound object.
        jump_sound: Jump sound effect object.
    """

    def __init__(self, mediator, screen, background=None):
        self.mediator = mediator
        self.moving_horizontally = False
        self.moving_up = False
        self.moving_down = False
        self.screen = screen
        self.background = background
        self.gravity = ZERO
        self.player_x = PLAYER_X
        self.player_y = PLAYER_Y
        self.walk_index = ZERO
        self.facing_left = False  # Track direction
        self.prev_player_x = PLAYER_X  # Track previous position for edge detection
        
        # Normal (right-facing) images
        self.jump_image = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_jump_normal.png"))
        self.stand_image = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_stand_normal.png"))
        walk_image_1 = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_walk1_normal.png"))
        walk_image_2 = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_walk2_normal.png"))
        self.walking = [walk_image_1, walk_image_2]
        
        # Left-facing images
        self.jump_image_left = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_jump_normal.png"))
        self.stand_image_left = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_stand_normal.png"))
        walk_image_1_left = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_walk1_normal.png"))
        walk_image_2_left = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_walk2_normal.png"))
        self.walking_left = [walk_image_1_left, walk_image_2_left]
        self.image = self.stand_image

        # Place rectangle from midbottom
        self.rect = self.image.get_rect(
                    midbottom = (self.player_x, self.player_y))

        # Music and sounds
        self.music = pygame.mixer.Sound(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "audio",
                "musa1.wav"))
        self.music.set_volume(POINT_ONE)
        self.music.play(loops=-1)
        self.jump_sound = pygame.mixer.Sound(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "audio",
                "hyppy.mp3"))
        self.jump_sound.set_volume(POINT_ONE)
        self.notify('Player was created.')

    @property
    def rect_x(self):
        """
        Get the X coordinate of the player's rectangle.
        
        Returns:
            int: X coordinate of the player's rect.
        """
        return self.rect.x

    @property
    def rect_y(self):
        """
        Get the Y coordinate of the player's rectangle.
        
        Returns:
            int: Y coordinate of the player's rect.
        """
        return self.rect.y

    @rect_y.setter
    def rect_y(self, val):
        """
        Set the Y coordinate of the player's rectangle.
        
        Args:
            val (int): New Y coordinate value.
        """
        self.rect.y = val

    def player_input(self):
        """
        Handle player keyboard input and movement.
        
        Processes arrow key input for horizontal movement and spacebar
        for jumping. Handles screen edge detection and triggers background
        switching when the player reaches screen boundaries. Updates player
        position and facing direction based on input.
        """
        keys = pygame.key.get_pressed()

        # Move
        if keys[pygame.K_LEFT]:
            self.player_x += -FIVE
            self.moving_horizontally = True
            self.facing_left = True
        elif keys[pygame.K_RIGHT]:
            self.player_x += FIVE
            self.moving_horizontally = True
            self.facing_left = False
        else:
            self.moving_horizontally = False
        
        # Check if player reached right edge (crossed threshold)
        if self.player_x > SCREEN_WIDTH - SCREEN_LIMIT_R:
            self.player_x = SCREEN_WIDTH - SCREEN_LIMIT_R
            # Switch background when reaching right edge (only if just crossed
            # threshold)
            if self.background and self.prev_player_x <= SCREEN_WIDTH\
                                                            - SCREEN_LIMIT_R:
                if self.background.current_background == "entrance":
                    self.background.switch_to_yard()
                    # Position player 10px from left edge after switching
                    self.player_x = TEN
                elif self.background.current_background == "yard":
                    self.background.switch_to_entrance()
                    # Position player 10px from left edge after switching
                    self.player_x = TEN
        # Check if player reached left edge (crossed threshold)
        elif self.player_x < SCREEN_LIMIT_L:
            self.player_x = SCREEN_LIMIT_L
            # Switch background when reaching left edge (only if just crossed
            # threshold)
            if self.background and self.prev_player_x >= SCREEN_LIMIT_L:
                if self.background.current_background == "entrance":
                    self.background.switch_to_yard()
                    # Position player 10px from right edge after switching
                    self.player_x = SCREEN_WIDTH - TEN
                elif self.background.current_background == "yard":
                    self.background.switch_to_entrance()
                    # Position player 10px from right edge after switching
                    self.player_x = SCREEN_WIDTH - TEN
        
        # Update previous position for next frame
        self.prev_player_x = self.player_x

        # Jump
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_LEVEL + FIVE:
            self.moving_up = True
            self.play_sound(self.jump_sound)
            self.notify('Player jumped.')

        self.rect = self.image.get_rect(
                    midbottom = (self.player_x, self.player_y))

    def apply_gravity(self):
        """
        Apply gravity physics to the player's vertical movement.
        
        Manages the complete jump cycle:
        - When jumping up: applies negative gravity (upward force)
        - When reaching max height: switches to descending
        - When descending: applies positive gravity (downward force)
        - When reaching ground: resets gravity to zero
        
        Updates the player's rect.bottom position based on gravity
        calculations.
        """
        # BEGINNING:
            # Gravity = 0
        if self.moving_up:
            # JUMP:
                # Gravity Cumulative -10
                # Fly Until At Vertical Top Max
            self.gravity += -TEN
            self.rect.bottom += self.gravity
        if self.gravity <= GRAVITY_MAX:
            # At Vertical Top Max
                # Gravity <= -100
                # Start Descending
            self.rect.bottom += -self.gravity
            self.moving_up = False
            self.moving_down = True
        if self.moving_down:
            # Descending:
                # Gravity Cumulative +10
                # Fly Until At Ground Level
            self.gravity += TEN
            self.rect.bottom += self.gravity
        if self.moving_down and self.rect.bottom >= GROUND_LEVEL + FIVE:
            # At Ground Level:
                # Gravity = 0
            self.rect.bottom = GROUND_LEVEL + FIVE
            self.moving_down = False
            self.gravity = ZERO

    def draw(self):
        """
        Draw the player to the screen.
        
        Blits the current player image surface at the player's rect position.
        Should be called every frame after drawing the background.
        """
        self.screen.scr.blit(self.image, self.rect)

    def animate(self):
        """
        Update player animation based on current state.
        
        Selects the appropriate animation frame based on:
        - Whether player is in the air (jump animation)
        - Whether player is moving horizontally (walking animation)
        - Whether player is standing still (stand animation)
        - Current facing direction (left or right)
        
        Updates the self.image attribute with the correct surface.
        """
        if self.rect.bottom < GROUND_LEVEL + FIVE:
            self.image = self.jump_image_left if self.facing_left\
                else self.jump_image
        elif self.rect.bottom == GROUND_LEVEL + FIVE:
            if self.moving_horizontally:
                self.walk_index += POINT_ONE
                if self.walk_index >= len(self.walking):
                    self.walk_index = ZERO
                walking_images = self.walking_left if self.facing_left\
                    else self.walking
                self.image = walking_images[int(self.walk_index)]
            else:
                self.image = self.stand_image_left if self.facing_left\
                    else self.stand_image

    def play_sound(self, sound):
        """
        Play a sound effect.
        
        Args:
            sound: Pygame Sound object to play.
        """
        sound.play()

    def update(self):
        """
        Update player state for the current frame.
        
        Processes input, applies gravity/physics, and updates animation.
        Should be called once per frame in the game loop.
        """
        self.player_input()
        self.apply_gravity()
        self.animate()

    def notify(self, message):
        """
        Send a notification message through the mediator.
        
        Args:
            message (str): Message to send to the mediator.
        """
        self.mediator.notify(message)
