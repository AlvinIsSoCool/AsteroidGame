import pygame
import random
import settings

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, theme, elapsed_ms=0):
		super().__init__()
		self.theme = theme
		self.image = pygame.Surface((7, 7), pygame.SRCALPHA)
		self.image.fill((0, 0, 0, 0))
		self.color = (100, 255, 255)
		pygame.draw.rect(self.image, self.color, (0, 0, 7, 7))

		self.rect = self.image.get_rect(center=(x, y))
		minutes_played = elapsed_ms / 60000
		speed_multiplier = min(settings.BASE_SPEED + (minutes_played * settings.SPEED_MULTIPLIER_PROGRESS), settings.SPEED_MULTIPLIER_CAP)
		drift_multiplier = min(settings.BASE_DRIFT + (minutes_played * settings.DRIFT_MULTIPLIER_PROGRESS), settings.DRIFT_MULTIPLIER_CAP)
		print(f"Bullet Speed Multiplier: {speed_multiplier}")
		print(f"Bullet Drift Multiplier: {drift_multiplier}")
		self.speed = random.uniform(-2.5, -5.0) * speed_multiplier
		self.drift = random.uniform(-0.25, 0.25) * drift_multiplier

	def update(self):
		self.rect.y += self.speed
		if self.rect.bottom < 0:
			self.kill()

	def draw(self, surface):
		if self.theme:
			color = self.theme.color("bullet")

		pygame.draw.rect(surface, color, self.rect)