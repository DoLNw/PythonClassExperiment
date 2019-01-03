import pygame
import sys

while True:
	pygame.init()
	screen = pygame.display.set_mode((100, 100))
	pygame.display.flip()
	print("1")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()