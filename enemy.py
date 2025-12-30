import pygame
import random
import settings

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		is_big = random.random() < 0.25

		if is_big:
			size = 18
			self.color = (180, 100, 80)
			self.score = 200
			self.speed = random.uniform(1.0, 2.0)
		else:
			size = 12
			self.color = (220, 140, 100)
			self.score = 10
			self.speed = random.uniform(2.0, 3.0)

		self.image = pygame.Surface((size, size), pygame.SRCALPHA)
		self.image.fill((0, 0, 0, 0))

		self.rect = self.image.get_rect(center=(x, y))
		self.drift = random.uniform(-0.5, 0.5)

	def update(self):
		self.rect.x += self.drift
		self.rect.y += self.speed

		if self.rect.top > settings.HEIGHT:
			self.kill()