import pygame
import random
import settings

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()

		self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
		self.image.fill((0, 0, 0, 0))
		self.color = (0, 255, 0)
		pygame.draw.circle(self.image, self.color, (5, 5), 4)

		self.rect = self.image.get_rect(center=(x, y))
		self.speed = random.uniform(1.0, 3.0)

	def update(self):
		self.rect.y += self.speed

		if self.rect.top > settings.HEIGHT:
			self.kill()