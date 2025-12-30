import pygame
import random
import settings

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, theme):
		super().__init__()
		self.theme = theme
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

	def update_theme(self, theme):
		self.theme = theme

	def draw(self, surface):
		if self.theme:
			color = self.theme.color("bullet")
		else:
			color = (100, 255, 255)  # Fallback cyan
		
		pygame.draw.rect(surface, color, self.rect)