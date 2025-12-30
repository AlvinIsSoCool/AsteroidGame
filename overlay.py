import pygame
import settings

class OverlayHandler:
	def __init__(self, surface, theme):
		self.surface = surface
		self.theme = theme
		self.active = False

	def reset(self):
		self.surface.fill((0, 0, 0, 0))
		self.active = False

	def on_state_change(self):
		self.active = True

	def on_theme_change(self, theme):
		self.theme = theme

	def draw(self, screen):
		screen.blit(self.surface, (0, 0))

class GlobalOverlayHandler(OverlayHandler):
	def __init__(self, surface, theme):
		super().__init__(surface, theme)

	def draw_start(self):
		self.surface.fill(self.theme.color("overlay_start"))

		text1 = self.theme.font("large").render("Maze N' Chase", True, self.theme.color("text_primary"))
		text2 = self.theme.font("medium").render("Press ENTER to start", True, self.theme.color("text_secondary"))
		text3 = self.theme.font("medium").render("Press Q to quit", True, self.theme.color("text_secondary"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 120))
		rect2 = text2.get_rect(center=(settings.WIDTH // 2, 250))
		rect3 = text3.get_rect(center=(settings.WIDTH // 2, 278))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.surface.blit(text3, rect3)
		self.on_state_change()

	def draw_pause_menu(self):
		self.surface.fill(self.theme.color("overlay_pause"))

		text1 = self.theme.font("large").render("GAME PAUSED", True, self.theme.color("text_primary"))
		text2 = self.theme.font("medium").render("Press ESC to continue", True, self.theme.color("text_secondary"))
		text3 = self.theme.font("medium").render("Press Q to quit", True, self.theme.color("text_secondary"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 120))
		rect2 = text2.get_rect(center=(settings.WIDTH // 2, 250))
		rect3 = text3.get_rect(center=(settings.WIDTH // 2, 278))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.surface.blit(text3, rect3)
		self.on_state_change()

	def draw_game_over(self):
		self.surface.fill(self.theme.color("overlay_game_over"))
		text1 = self.theme.font("large").render("GAME OVER!", True, self.theme.color("text_primary"))
		text2 = self.theme.font("medium").render("Press ENTER to respawn", True, self.theme.color("text_secondary"))
		text3 = self.theme.font("medium").render("Press Q to quit", True, self.theme.color("text_secondary"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 120))
		rect2 = text2.get_rect(center=(settings.WIDTH // 2, 250))
		rect3 = text3.get_rect(center=(settings.WIDTH // 2, 278))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.surface.blit(text3, rect3)
		self.on_state_change()

	def draw_game_won(self):
		self.surface.fill(self.theme.color("overlay_game_win"))
		text1 = self.theme.font("large").render("GAME WON!", True, self.theme.color("text_primary"))
		text2 = self.theme.font("medium").render("Press ENTER to respawn", True, self.theme.color("text_secondary"))
		text3 = self.theme.font("medium").render("Press Q to quit", True, self.theme.color("text_secondary"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 120))
		rect2 = text2.get_rect(center=(settings.WIDTH // 2, 250))
		rect3 = text3.get_rect(center=(settings.WIDTH // 2, 278))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.surface.blit(text3, rect3)
		self.on_state_change()

class LocalOverlayHandler(OverlayHandler):
	def __init__(self, surface, theme):
		super().__init__(surface, theme)

	def draw_coordinates(self, em):
		self.surface.fill((0, 0, 0, 0))

		p, x = em.get_player(), em.get_enemy()
		px, py = p.rect.topleft
		xx, xy = x.rect.topleft
		text1 = self.theme.font("small").render(f"Player1 -> X: {px}, Y: {py}", True, self.theme.color("text_secondary"))
		text2 = self.theme.font("small").render(f"Enemy1 -> X: {xx}, Y: {xy}", True, self.theme.color("text_secondary"))
		rect1 = text1.get_rect(topleft=(5, 5))
		rect2 = text2.get_rect(topleft=(5, 25))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.dirty = True