import pygame
import settings

class OverlayHandler(object):
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
		super(GlobalOverlayHandler, self).__init__(surface, theme)

	def draw_start(self):
		self.surface.fill(self.theme.color("overlay_start"))

		text1 = self.theme.font("large").render("Asteroid Game", True, self.theme.color("text_primary"))
		text2 = self.theme.font("medium").render("Press ENTER to start", True, self.theme.color("text_secondary"))
		text3 = self.theme.font("medium").render("Press Q to quit", True, self.theme.color("text_secondary"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 140))
		rect2 = text2.get_rect(center=(settings.WIDTH // 2, 250))
		rect3 = text3.get_rect(center=(settings.WIDTH // 2, 270))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.surface.blit(text3, rect3)
		self.on_state_change()

	def draw_pause_menu(self, game):
		self.surface.fill(self.theme.color("overlay_pause"))

		text1 = self.theme.font("large").render("GAME PAUSED", True, self.theme.color("text_primary"))
		text2 = self.theme.font("medium").render("%-15s%s" % ('Score:', str(game.score)), True, self.theme.color("text_secondary"))
		text3 = self.theme.font("medium").render("%-12s%s" % ('High Score:', str(game.high_score)), True, self.theme.color("text_secondary"))
		text4 = self.theme.font("medium").render("Press ESC to continue", True, self.theme.color("text_secondary"))
		text5 = self.theme.font("medium").render("Press Q to quit", True, self.theme.color("text_secondary"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 140))
		rect3 = text3.get_rect(center=(settings.WIDTH // 2, 205))
		rect2 = text2.get_rect(topleft=(rect3.x + 1, rect3.y - 20))
		rect4 = text4.get_rect(center=(settings.WIDTH // 2, 270))
		rect5= text5.get_rect(center=(settings.WIDTH // 2, 290))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.surface.blit(text3, rect3)
		self.surface.blit(text4, rect4)
		self.surface.blit(text5, rect5)
		self.on_state_change()

	def draw_game_over(self, game):
		self.surface.fill(self.theme.color("overlay_game_over"))
		text1 = self.theme.font("large").render("GAME OVER", True, self.theme.color("text_primary"))
		text2 = self.theme.font("medium").render("%-15s%s" % ('Score:', str(game.score)), True, self.theme.color("text_secondary"))
		text3 = self.theme.font("medium").render("%-12s%s" % ('High Score:', str(game.high_score)), True, self.theme.color("text_secondary"))
		text4 = self.theme.font("medium").render("Press ENTER to respawn", True, self.theme.color("text_secondary"))
		text5 = self.theme.font("medium").render("Press Q to quit", True, self.theme.color("text_secondary"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 140))
		rect3 = text3.get_rect(center=(settings.WIDTH // 2, 205))
		rect2 = text2.get_rect(topleft=(rect3.x + 1, rect3.y - 20))
		rect4 = text4.get_rect(center=(settings.WIDTH // 2, 270))
		rect5= text5.get_rect(center=(settings.WIDTH // 2, 290))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.surface.blit(text3, rect3)
		self.surface.blit(text4, rect4)
		self.surface.blit(text5, rect5)
		self.on_state_change()

class LocalOverlayHandler(OverlayHandler):
	def __init__(self, surface, theme):
		super(LocalOverlayHandler, self).__init__(surface, theme)

	def draw_info(self, game):
		self.surface.fill((0, 0, 0, 0))

		lives = game.lives
		high_score = game.high_score

		lives_len = self.theme.get_text_width("medium", str(lives))
		high_score_len = self.theme.get_text_width("medium", str(high_score))
		space_len = self.theme.get_text_width("medium", " ")

		high_score_text = "%-12s%s" % ('High Score:', str(high_score))
		high_score_text = high_score_text + " " * (lives_len // space_len) if high_score_len < lives_len else high_score_text

		text1 = self.theme.font("medium").render("%-15s%s" % ('Score:', str(game.score)), True, self.theme.color("text_secondary"))
		text2 = self.theme.font("medium").render(high_score_text, True, self.theme.color("text_secondary"))
		text3 = self.theme.font("medium").render("%-16s%s" % ('Lives:', str(lives)), True, self.theme.color("text_secondary"))

		rect2 = text2.get_rect()

		rect1 = text1.get_rect(topleft=(settings.WIDTH - rect2.width - 1, 5))
		rect3 = text3.get_rect(topleft=(settings.WIDTH - rect2.width - 2, 45))
		rect2 = text2.get_rect(topleft=(settings.WIDTH - rect2.width - 2, 25))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.surface.blit(text3, rect3)