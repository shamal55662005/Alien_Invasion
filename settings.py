class Settings():
    """A class to store all the settings for alien invasion"""

    def __init__(self):
        """instilize the game settings """
        #Screen settings
        self.screen_wdith = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # Ship settings
        self.ships_speed = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60 
        self.bullets_allowed = 10000
