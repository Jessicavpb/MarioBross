import pygame

class Platform:

	def __init__(self, Arena_Game):
		self.screen = Arena_Game.screen
		self.screen_rect = Arena_Game.screen.get_rect()

		self.game_settings = Arena_Game.game_settings
		self.image = self.game_settings.platform_image
		self.image_rect = self.image.get_rect()

		self.image_rect.midbottom = self.screen_rect.midbottom

	def show_platform(self):
		self.screen.blit(self.image, self.image_rect)