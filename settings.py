import pygame

class Settings:
	def __init__(self):

		self.screen_width = 1080
		self.screen_height = 608
		self.title = "Mario Bros"
		self.background = pygame.image.load("img/bg44.JPG")

		self.mario_image = pygame.image.load("img/marioooo.PNG")

		self.platform_image = pygame.image.load('img/groundddd.JPG')