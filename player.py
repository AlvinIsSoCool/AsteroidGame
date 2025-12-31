import pygame
import settings

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, theme):
		super().__init__()

		self.image = pygame.Surface((14, 14), pygame.SRCALPHA)
		self.image.fill((0, 0, 0, 0))

		self.rect = self.image.get_rect(center=(x, y))
		self.old_rect = self.rect.copy()
		self.theme = theme
		self.speed = 5
		self.triangle_points = [
			(7, 2), # Top point.
			(3, 12), # Bottom-left point.
			(11, 12) #Bottom-right point.
		]

	def update(self, keys):
		self.old_rect.center = self.rect.center

		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
		elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
			self.rect.x -= self.speed
		elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
			self.rect.y += self.speed
		elif keys[pygame.K_w] or keys[pygame.K_UP]:
			self.rect.y -= self.speed

		self.rect.clamp_ip(pygame.Rect(0, 0, settings.WIDTH, settings.HEIGHT))

	def draw(self, surface, is_invincible=False, current_time=0):
		if self.theme:
			draw_color = self.theme.color("player")

		absolute_points = [(self.rect.x + x, self.rect.y + y) for (x, y) in self.triangle_points]
		if not is_invincible or (current_time // 200) % 2 == 0:
			pygame.draw.polygon(surface, draw_color, absolute_points)