class Settings:
    """A class to store all the settings for Alien Invasion"""
    def __init__(self):
        """Intializing the game settings."""

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bgcolor = (230, 230, 230)

        #Alien settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 5

        #ship settings
        self.ship_speed = 4.0
        self.ship_limit = 3