class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5 # pixels
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3 # pixels
        self.bullet_height = 5 #pixels
        self.bullet_color = 60, 60, 60 # dark gray bullets
        self.bullets_allowed = 5 # the number of bullets at a time

        # Alien seetings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5 # how quickly the fleet drops down the screen each time
        self.fleet_direction = 1 # fleet_direction of 1 represents right; -1 represents left.