import pygame

class Ship():

	def __init__(self, ailen_settings, screen):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.ailen_settings = ailen_settings

		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center = float(self.rect.centerx)

		self.moving_right = False
		self.moving_left = False

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""根据移动标志调整飞船的位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ailen_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ailen_settings.ship_speed_factor
		
		self.rect.centerx = self.center


