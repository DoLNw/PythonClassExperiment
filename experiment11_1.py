import sys
import pygame

import settings

def run_game():
	pygame.init()

	ailen_settings = Settings()

	screen = pygame.display.set_mode((ailen_settings.screen_width, ailen_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(ailen_settings.bg_color)
		pygame.display.flip()

run_game()