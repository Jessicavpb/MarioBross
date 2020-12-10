import pygame


class Mario:

	def __init__(self, Arena_Game):
		self.screen = Arena_Game.screen
		self.screen_rect = Arena_Game.screen.get_rect()

		self.game_settings = Arena_Game.game_settings
		self.image = self.game_settings.mario_image
		self.image_rect = self.image.get_rect()

		self.image_rect.midleft = self.screen_rect.midleft
		self.image_rect.x += 20
		self.image_rect.y += 218

	def show_mario(self):
		self.screen.blit(self.image, self.image_rect)