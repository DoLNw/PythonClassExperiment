import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	pygame.init()
	alien_settings = Settings()
	screen = pygame.display.set_mode((alien_settings.screen_width, alien_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(alien_settings, screen)

	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(alien_settings, screen, ship)

run_game()