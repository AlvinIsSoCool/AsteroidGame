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

	def update(self, dt, keys):
		self.old_rect.center = self.rect.center

        dx = dy = 0
		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			dx = 1
		elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
			dx = -1
		elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
			dy = 1
		elif keys[pygame.K_w] or keys[pygame.K_UP]:
			dy = -1

        if dx == 0 and dy == 0:
            return

        if dx != 0:
            self.rect.x += dx * self.speed * dt
        elif dy != 0:
            self.rect.y += dy * self.speed * dt

		self.rect.clamp_ip(pygame.Rect(0, 0, settings.WIDTH, settings.HEIGHT))

	def draw(self, surface, is_invincible=False, current_time=0):
		if self.theme:
			draw_color = self.theme.color("player")

		absolute_points = [(self.rect.x + x, self.rect.y + y) for (x, y) in self.triangle_points]
		if not is_invincible or (current_time // 200) % 2 == 0:
			pygame.draw.polygon(surface, draw_color, absolute_points)