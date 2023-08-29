import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Intilize the ship and set its stating position"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Load the ship image and get its react.
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each ship at bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the ship's center value, not the rect

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ships_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ships_speed
        
        # Update rect object from self.center.
        self.rect.centerx = self.center



    def blitme(self):
        """Draw the shit at its location"""
        self.screen.blit(self.image,self.rect)
