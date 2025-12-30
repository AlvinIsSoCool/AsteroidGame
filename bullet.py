import pygame
import random
import settings

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()

		self.image = pygame.Surface((5, 5), pygame.SRCALPHA)
		self.image.fill((0, 0, 0, 0))
		self.color = (100, 255, 255)
		pygame.draw.rect(self.image, self.color, (0, 0, 5, 5))

		self.rect = self.image.get_rect(center=(x, y))
		self.speed = -8
		self.growing = True

	def update(self):
		self.rect.y += self.speed
		if self.rect.bottom < 0:
			self.kill()