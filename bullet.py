import pygame
import random
import settings

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, theme, elapsed_ms=0):
		pygame.sprite.Sprite.__init__(self)

		self.theme = theme
		self.image = pygame.Surface((7, 7), pygame.SRCALPHA)
		self.image.fill((0, 0, 0, 0))
		self.color = (100, 255, 255)
		pygame.draw.rect(self.image, self.color, (0, 0, 7, 7))

		self.rect = self.image.get_rect(center=(x, y))
		minutes_played = elapsed_ms / 60000
		speed_multiplier = min(settings.BASE_SPEED + (minutes_played * settings.SPEED_MULTIPLIER_PROGRESS), settings.SPEED_MULTIPLIER_CAP)
		drift_multiplier = min(settings.BASE_DRIFT + (minutes_played * settings.DRIFT_MULTIPLIER_PROGRESS), settings.DRIFT_MULTIPLIER_CAP)
		self.speed = random.uniform(200.0, 300.0) * speed_multiplier
		self.drift = random.uniform(-3.0, 3.0) * drift_multiplier

	def update(self, dt):
		self.rect.x += self.drift * dt
		self.rect.y -= self.speed * dt

		if self.rect.bottom < 0:
			self.kill()

		self.rect.clamp_ip(pygame.Rect(0, -10, settings.WIDTH, settings.HEIGHT + 20))

	def draw(self, surface):
		if self.theme:
			color = self.theme.color("bullet")

		pygame.draw.rect(surface, color, self.rect)