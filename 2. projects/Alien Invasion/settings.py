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

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3 # pixels
        self.bullet_height = 5 #pixels
        self.bullet_color = 60, 60, 60 # dark gray bullets
        self.bullets_allowed = 5 # the number of bullets at a time