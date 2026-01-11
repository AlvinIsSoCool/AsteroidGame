import pygame
import random
import settings

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, theme, elapsed_ms=0):
		pygame.sprite.Sprite.__init__(self)

		self.theme = theme
		self.is_big = random.random() < 0.25
		minutes_played = elapsed_ms / 60000
		speed_multiplier = min(settings.BASE_SPEED + (minutes_played * settings.SPEED_MULTIPLIER_PROGRESS), settings.SPEED_MULTIPLIER_CAP)
		drift_multiplier = min(settings.BASE_DRIFT + (minutes_played * settings.DRIFT_MULTIPLIER_PROGRESS), settings.DRIFT_MULTIPLIER_CAP)

		if self.is_big:
			self.size = 18
			self.color = (180, 100, 80)
			self.score = 20
			self.speed = random.uniform(45.0, 80.0) * speed_multiplier
		else:
			self.size = 14
			self.color = (220, 140, 100)
			self.score = 10
			self.speed = random.uniform(100.0, 200.0) * speed_multiplier

		self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
		self.image.fill((0, 0, 0, 0))

		self.rect = self.image.get_rect(center=(x, y))
		self.drift = random.uniform(-10.0, 10.0) * drift_multiplier if self.is_big else random.uniform(-20.0, 20.0) * drift_multiplier

	def update(self, dt):
		self.rect.x += self.drift * dt
		self.rect.y += self.speed * dt

		if self.rect.top > settings.HEIGHT:
			self.kill()

		self.rect.clamp_ip(pygame.Rect(0, -20, settings.WIDTH, settings.HEIGHT + 40))

	def draw(self, surface):
		if self.theme:
			if self.is_big:
				color = self.theme.color("asteroid_big")
			else:
				color = self.theme.color("asteroid_small")

		center_x, center_y = self.rect.center
		radius = self.size // 2
		pygame.draw.circle(surface, color, (center_x, center_y), radius)