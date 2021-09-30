import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and create a screen object
    pygame.init() # Initialize background settings that Pygame needs to work properly.
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # set create a display window(screen or surface) (1200(w) x 800(h) pixels)
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Set the background color.
    #bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        

run_game()