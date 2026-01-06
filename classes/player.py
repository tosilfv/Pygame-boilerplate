"""
Player character implementation for the Piccolo game.

This module handles all player-related functionality including movement,
jumping, gravity, animation, and sound effects. The player can move
horizontally, jump, and trigger background changes when reaching screen
edges.
"""

import pygame
import os
from utils.constants.constants import FIVE,\
    GRAVITY_MAX, GROUND_LEVEL,HUNDRED, PLAYER_X, PLAYER_Y, POINT_ONE,\
    PURPLE, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_LIMIT_L, SCREEN_LIMIT_R, TEN,\
    ZERO
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
        facing_left (bool): Whether player is facing left.
        moving_down (bool): Whether player is currently falling downward.
        moving_horizontally (bool): Whether player is currently moving left/right.
        moving_up (bool): Whether player is currently jumping upward.
        show_player (bool): Whether player image is shown.
        gravity (int): Current gravity value affecting vertical movement.
        player_x (int): Current X position of the player.
        player_y (int): Current Y position of the player.
        prev_player_x (int): Previous X position for edge detection.
        walk_index (float): Animation index for walking animation.
        selected_floor (int or None): Number of selected floor or None.
        show_elevator_prompt (bool): Timer for floor selection delay.
        elevator_floor_selection_time (bool): Whether elevator prompt is visible.
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
        self.screen = screen
        self.background = background
        self.facing_left = False
        self.moving_down = False
        self.moving_horizontally = False
        self.moving_up = False
        self.show_player = True
        self.gravity = ZERO
        self.player_x = PLAYER_X
        self.player_y = PLAYER_Y
        self.prev_player_x = PLAYER_X
        self.walk_index = ZERO
        
        # Elevator input state
        self.selected_floor = None
        self.show_elevator_prompt = False
        self.elevator_floor_selection_time = None
        
        # Font for elevator prompt
        font_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "media",
            "font",
            "Pixeltype.ttf")
        try:
            self.font = pygame.font.Font(font_path, 30)
        except:
            self.font = pygame.font.Font(None, 30)
        
        # Normal (right-facing) images
        self.jump_image_normal = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_jump_normal.png"))
        self.stand_image_normal = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_stand_normal.png"))
        walk_image_1_normal = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_walk1_normal.png"))
        walk_image_2_normal = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_walk2_normal.png"))
        self.walking_normal = [walk_image_1_normal, walk_image_2_normal]
        
        # Large (right-facing) images
        self.jump_image_large = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_jump_large.png"))
        self.stand_image_large = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_stand_large.png"))
        walk_image_1_large = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_walk1_large.png"))
        walk_image_2_large = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_walk2_large.png"))
        self.walking_large = [walk_image_1_large, walk_image_2_large]
        
        # Normal left-facing images
        self.jump_image_left_normal = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_jump_normal.png"))
        self.stand_image_left_normal = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_stand_normal.png"))
        walk_image_1_left_normal = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_walk1_normal.png"))
        walk_image_2_left_normal = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_walk2_normal.png"))
        self.walking_left_normal = \
                        [walk_image_1_left_normal, walk_image_2_left_normal]
        
        # Large left-facing images
        self.jump_image_left_large = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_jump_large.png"))
        self.stand_image_left_large = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_stand_large.png"))
        walk_image_1_left_large = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_walk1_large.png"))
        walk_image_2_left_large = helpers.load_image(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "graphics",
                "player",
                "piccolo_left_walk2_large.png"))
        self.walking_left_large = \
                        [walk_image_1_left_large, walk_image_2_left_large]
        
        # Set initial images (using normal by default)
        self.image = self.stand_image_normal

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
        self.hissi_sound = pygame.mixer.Sound(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "audio",
                "hissi.wav"))
        self.hissi_sound.set_volume(POINT_ONE)
        
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
        # Reset elevator prompt if no longer in any elevator_open background
        if (self.background and 
            not self.background.current_background.startswith("elevator_open")
            and self.show_elevator_prompt):
            self.show_elevator_prompt = False
            self.selected_floor = None
        
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
        
        # Check if player is at center and up arrow is pressed
        # Center is approximately SCREEN_WIDTH / 2 (400), with some tolerance
        center_tolerance = HUNDRED  # Allow player to be within 100px of center
        center_min = SCREEN_WIDTH // 2 - center_tolerance
        center_max = SCREEN_WIDTH // 2 + center_tolerance
        
        if (keys[pygame.K_UP] and 
            self.background and 
            self.background.current_background == "entrance" and
            center_min <= self.player_x <= center_max):
            self.background.switch_to_frontdesk()
            self.change_music("musa2.wav")
        
        # Check if player is at center and up arrow is pressed in elevator lobby
        if (keys[pygame.K_UP] and 
            self.background and 
            self.background.current_background == "elevator_lobby" and
            center_min <= self.player_x <= center_max):
            # Store the previous background state
            previous_background = self.background.current_background
            self.background.switch_to_elevator_open_lobby()
            # Play sound only if the switch actually happened (background changed)
            if previous_background == "elevator_lobby" and self.background.current_background == "elevator_open_lobby":
                self.play_sound(self.hissi_sound)
                self.show_elevator_prompt = True
                self.show_player = False
                self.selected_floor = None
        
        # Check if player is at center and up arrow is pressed on any elevator floor
        if (keys[pygame.K_UP] and 
            self.background and 
            self.background.current_background.startswith("elevator_floor") and
            center_min <= self.player_x <= center_max):
            # Extract floor number from background name (e.g., "elevator_floor3" -> 3)
            try:
                floor_num = int(self.background.current_background.replace("elevator_floor", ""))
                # Store the previous background state
                previous_background = self.background.current_background
                self.background.switch_to_elevator_open_floor(floor_num)
                # Play sound only if the switch actually happened (background changed)
                if previous_background == f"elevator_floor{floor_num}" and self.background.current_background == f"elevator_open_floor{floor_num}":
                    self.play_sound(self.hissi_sound)
                    self.show_elevator_prompt = True
                    self.selected_floor = None
            except ValueError:
                pass  # Invalid floor number format
        
        # Check if player is at center and down arrow is pressed
        if (keys[pygame.K_DOWN] and 
            self.background and 
            self.background.current_background == "frontdesk" and
            center_min <= self.player_x <= center_max):
            self.background.switch_to_entrance()
            self.change_music("musa1.wav")
        
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
                elif self.background.current_background == "frontdesk":
                    self.background.switch_to_elevator_lobby()
                    # Position player 10px from left edge after switching
                    self.player_x = TEN
                elif self.background.current_background == "elevator_lobby":
                    self.background.switch_to_frontdesk()
                    # Position player 10px from left edge after switching
                    self.player_x = TEN
                # Handle corridor transitions when on elevator floors
                elif self.background.current_background.startswith("elevator_floor"):
                    # Extract floor number from background name
                    try:
                        floor_num = int(self.background.current_background.replace("elevator_floor", ""))
                        next_corridor = self.background.get_next_corridor_right(floor_num, self.background.current_corridor)
                        if next_corridor is not None:
                            # Switch to next corridor
                            self.background.switch_to_corridor(floor_num, next_corridor)
                            self.player_x = TEN
                        else:
                            # Already at last corridor or no corridors available, stay at elevator
                            pass
                    except ValueError:
                        pass  # Invalid floor number format
                elif self.background.current_background.startswith("corridor"):
                    # Extract floor and corridor numbers from background name (e.g., "corridor1_floor3")
                    try:
                        parts = self.background.current_background.split("_")
                        corridor_num = int(parts[0].replace("corridor", ""))
                        floor_num = int(parts[1].replace("floor", ""))
                        next_corridor = self.background.get_next_corridor_right(floor_num, corridor_num)
                        if next_corridor is not None:
                            # Switch to next corridor
                            self.background.switch_to_corridor(floor_num, next_corridor)
                            self.player_x = TEN
                        else:
                            # At last corridor, go back to elevator
                            if floor_num in self.background.elevator_floor_ground_surfs:
                                self.background.switch_to_elevator_floor(floor_num)
                                self.player_x = TEN
                    except (ValueError, IndexError):
                        pass  # Invalid background name format
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
                elif self.background.current_background == "frontdesk":
                    self.background.switch_to_elevator_lobby()
                    # Position player 10px from right edge after switching
                    self.player_x = SCREEN_WIDTH - TEN
                elif self.background.current_background == "elevator_lobby":
                    self.background.switch_to_frontdesk()
                    # Position player 10px from right edge after switching
                    self.player_x = SCREEN_WIDTH - TEN
                # Handle corridor transitions when on elevator floors (moving left)
                elif self.background.current_background.startswith("elevator_floor"):
                    # Extract floor number from background name
                    try:
                        floor_num = int(self.background.current_background.replace("elevator_floor", ""))
                        next_corridor = self.background.get_next_corridor_left(floor_num, self.background.current_corridor)
                        if next_corridor is not None:
                            # Switch to previous corridor (last one when coming from elevator)
                            self.background.switch_to_corridor(floor_num, next_corridor)
                            self.player_x = SCREEN_WIDTH - TEN
                        else:
                            # Already at first corridor or no corridors available, stay at elevator
                            pass
                    except ValueError:
                        pass  # Invalid floor number format
                elif self.background.current_background.startswith("corridor"):
                    # Extract floor and corridor numbers from background name (e.g., "corridor1_floor3")
                    try:
                        parts = self.background.current_background.split("_")
                        corridor_num = int(parts[0].replace("corridor", ""))
                        floor_num = int(parts[1].replace("floor", ""))
                        next_corridor = self.background.get_next_corridor_left(floor_num, corridor_num)
                        if next_corridor is not None:
                            # Switch to previous corridor
                            self.background.switch_to_corridor(floor_num, next_corridor)
                            self.player_x = SCREEN_WIDTH - TEN
                        else:
                            # At first corridor, go back to elevator
                            if floor_num in self.background.elevator_floor_ground_surfs:
                                self.background.switch_to_elevator_floor(floor_num)
                                self.player_x = SCREEN_WIDTH - TEN
                    except (ValueError, IndexError):
                        pass  # Invalid background name format
        
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
            self.gravity += -FIVE
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
            self.gravity += FIVE
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
        
        # Draw elevator prompt if in any elevator_open background
        if (self.background and 
            self.background.current_background.startswith("elevator_open") and
            self.show_elevator_prompt):
            self._draw_elevator_prompt()

    def _get_image_set(self):
        """
        Get the appropriate image set (normal or large) based on current background.
        
        Returns:
            tuple: (jump_image, stand_image, walking, jump_image_left, 
                   stand_image_left, walking_left) for the current size.
        """
        # Use large images when background is "frontdesk", "elevator_lobby", "elevator_open_lobby",
        # any elevator floor background (elevator_floorX or elevator_open_floorX), or any corridor
        # normal otherwise
        if self.background:
            bg = self.background.current_background
            is_large_bg = (bg == "frontdesk" or 
                          bg == "elevator_lobby" or
                          bg == "elevator_open_lobby" or
                          bg.startswith("elevator_floor") or
                          bg.startswith("elevator_open_floor") or
                          bg.startswith("corridor"))
            if is_large_bg:
                return (self.jump_image_large, self.stand_image_large, 
                       self.walking_large, self.jump_image_left_large,
                       self.stand_image_left_large, self.walking_left_large)
        return (self.jump_image_normal, self.stand_image_normal,
               self.walking_normal, self.jump_image_left_normal,
               self.stand_image_left_normal, self.walking_left_normal)

    def animate(self):
        """
        Update player animation based on current state.
        
        Selects the appropriate animation frame based on:
        - Whether player is in the air (jump animation)
        - Whether player is moving horizontally (walking animation)
        - Whether player is standing still (stand animation)
        - Current facing direction (left or right)
        - Current background (normal or large images)
        
        Updates the self.image attribute with the correct surface.
        """
        # Get the appropriate image set based on background
        jump_img, stand_img, walking_imgs, jump_img_left, stand_img_left, walking_imgs_left = self._get_image_set()
        
        if self.rect.bottom < GROUND_LEVEL + FIVE:
            self.image = jump_img_left if self.facing_left else jump_img
        elif self.rect.bottom == GROUND_LEVEL + FIVE:
            if self.moving_horizontally:
                self.walk_index += POINT_ONE
                if self.walk_index >= len(walking_imgs):
                    self.walk_index = ZERO
                walking_images = walking_imgs_left if self.facing_left else walking_imgs
                self.image = walking_images[int(self.walk_index)]
            else:
                self.image = stand_img_left if self.facing_left else stand_img

    def play_sound(self, sound):
        """
        Play a sound effect.
        
        Args:
            sound: Pygame Sound object to play.
        """
        sound.play()

    def change_music(self, music_file):
        """
        Change the background music to a new file.
        
        Stops the current music and starts playing the new music file.
        
        Args:
            music_file (str): Name of the music file (e.g., "musa1.wav").
        """
        self.music.stop()
        self.music = pygame.mixer.Sound(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "media",
                "audio",
                music_file))
        self.music.set_volume(POINT_ONE)
        self.music.play(loops=-1)

    def update(self):
        """
        Update player state for the current frame.
        
        Processes input, applies gravity/physics, and updates animation.
        Should be called once per frame in the game loop.
        """
        self.player_input()
        self.apply_gravity()
        self.animate()
        
        # Check if it's time to switch to elevator floor background (after 1 second)
        if (self.elevator_floor_selection_time is not None and 
            self.selected_floor is not None and
            self.background and
            self.background.current_background.startswith("elevator_open")):
            current_time = pygame.time.get_ticks()
            # 1000 milliseconds = 1 second
            if current_time - self.elevator_floor_selection_time >= 1000:
                # Check if floor background exists before switching
                if (self.selected_floor in self.background.elevator_floor_ground_surfs and
                    self.selected_floor in self.background.elevator_floor_sky_surfs):
                    self.background.switch_to_elevator_floor(self.selected_floor)
                # Reset timer and selection state regardless of whether switch happened
                self.elevator_floor_selection_time = None
                self.show_elevator_prompt = False

    def handle_elevator_input(self, event):
        """
        Handle number key input for elevator floor selection.
        
        Args:
            event: Pygame KEYDOWN event.
        
        Returns:
            bool: True if input was handled, False otherwise.
        """
        if (not self.background or 
            not self.background.current_background.startswith("elevator_open") or
            not self.show_elevator_prompt):
            return False
        
        # Check if a number key (1-9) was pressed
        if event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_1 and event.key <= pygame.K_9:
                floor = event.key - pygame.K_0  # Convert key to number (1-9)
                
                # If input is 1 or 2, switch to elevator lobby
                if floor == 1 or floor == 2:
                    self.background.switch_to_elevator_lobby()
                    self.show_elevator_prompt = False
                    self.selected_floor = None
                    self.elevator_floor_selection_time = None
                    return True
                
                # For floors 3-9, select the floor
                self.selected_floor = floor
                # Start timer for 1 second delay before switching background
                self.elevator_floor_selection_time = pygame.time.get_ticks()
                self.notify(f'Elevator floor {floor} selected.')
                return True
        
        return False
    
    def _draw_elevator_prompt(self):
        """
        Draw the elevator floor selection prompt message.
        """
        # Main prompt text
        prompt_text = "Press a number (1-9) to select floor:"
        prompt_surface = self.font.render(prompt_text, True, (255, 255, 255))
        prompt_rect = prompt_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        
        # Draw semi-transparent background for better visibility
        bg_surface = pygame.Surface((prompt_rect.width + 20, prompt_rect.height + 20))
        bg_surface.set_alpha(200)
        bg_surface.fill((0, 0, 0))
        bg_rect = bg_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        self.screen.scr.blit(bg_surface, bg_rect)
        
        # Draw prompt text
        self.screen.scr.blit(prompt_surface, prompt_rect)
        
        # Draw selected floor if one is selected
        if self.selected_floor is not None:
            selected_text = f"Floor {self.selected_floor} selected!"
            selected_surface = self.font.render(selected_text, True, PURPLE)
            selected_rect = selected_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
            
            # Draw background for selected floor message
            selected_bg = pygame.Surface((selected_rect.width + 20, selected_rect.height + 20))
            selected_bg.set_alpha(200)
            selected_bg.fill((0, 0, 0))
            selected_bg_rect = selected_bg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
            self.screen.scr.blit(selected_bg, selected_bg_rect)
            
            self.screen.scr.blit(selected_surface, selected_rect)

    def notify(self, message):
        """
        Send a notification message through the mediator.
        
        Args:
            message (str): Message to send to the mediator.
        """
        self.mediator.notify(message)
