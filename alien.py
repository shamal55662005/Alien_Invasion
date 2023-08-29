import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class that represnt a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its stating to position"""
        super(Alien, self). __init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Load the alien image and its react attribute.
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def biltme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)


