import pygame

from settings import Settings
from mario import Mario 

from platform import Platform 

class Arena_Game:

	def __init__(self):
		pygame.init()
		self.game_settings = Settings()

		self.screen = pygame.display.set_mode([self.game_settings.screen_width, self.game_settings.screen_height])
		self.title = pygame.display.set_caption(self.game_settings.title)
		self.running = True

		self.game_mario = Mario(self)
		self.game_platform = Platform(self)

	def update_bg_screen(self):
		self.screen.blit(self.game_settings.background, [0,0])

	def update_mario(self):
		self.game_mario.show_mario()

	def update_platform(self):
		self.game_platform.show_platform()

	def rg_check_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				self.running = False

	def rg_update_screen(self):
		self.update_bg_screen()
		self.update_mario()
		self.update_platform()
		pygame.display.flip()

	def run_game(self):
		while self.running:
			self.rg_check_events()
			self.rg_update_screen()

mario_bros_game = Arena_Game()
mario_bros_game.run_game()