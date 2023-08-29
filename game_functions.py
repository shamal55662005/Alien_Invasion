import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):

     if event.key == pygame.K_RIGHT:
          ship.moving_right = True
     elif event.key == pygame.K_LEFT:
          ship.moving_left = True
     elif event.key == pygame.K_SPACE:
          fire_bullet(ai_settings, screen, ship, bullets)
          

def fire_bullet(ai_settings, screen, ship, bullets):
# Ceate a new bullet and add it to the bullets group.
     if len(bullets) < ai_settings.bullets_allowed:
          new_bullet = Bullet(ai_settings, screen, ship)
          bullets.add(new_bullet)
     


def check_keyup_events(event, ship):
     
    if event.key == pygame.K_RIGHT:
         ship.moving_right = False
    elif event.key == pygame.K_LEFT:
         ship.moving_left = False
    elif event.key == pygame.K_ESCAPE:
         sys.exit()



def check_events(ai_settings, screen, ship, bullets):
     """Respond to keypress and mouse events."""
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
             check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, ship)
       


def update_screen(ai_settings, screen, ship, alien, bullets):
        
        # Redraw the screen during each pass through loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # Redraw all bullets behind ships and aliens.
        for bullet in bullets:
             bullet.draw_bullet()
        ship.blitme()
        alien.draw(screen)
        

        # Make the most recently drawn screen visible
        pygame.display.flip()


def update_bullets(bullets):
     """Update position of bullets and get rid of ild bullets"""
     # Update bullet positions.
     bullets.update()

     #Get rid bullet that have disappeared
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
     print(len(bullets))


def create_fleet(ai_settings, screen, aliens):
     """Create a full fleet of aliens"""
     # Create an alien and find the number of aliens in a row
     # Spacing between each alien is equal to one alien width
     alien = Alien(ai_settings, screen)
     alien_width = alien.rect.width
     available_space_x = ai_settings.screen_wdith - 2 * alien_width
     number_aliens_x = int(available_space_x / (2 * alien_width))

     # Create the first row of aliens.
     for alien_number in range(number_aliens_x):
          # Create an alien and place it in the row
          alien = Alien(ai_settings, screen)
          alien.x = alien_width + 2 * alien_width * alien_number
          alien.rect.x = alien.x
          aliens.add(alien)