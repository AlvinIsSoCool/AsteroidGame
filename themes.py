import pygame

__all__ = ["Theme", "THEMES", "DARK_THEME", "LIGHT_THEME"]

class Theme:
	def __init__(self, *, name, colors, fonts):
		self.name = name
		self.colors = colors
		self.font_defs = fonts
		self._fonts = {}

	def color(self, key):
		return self.colors[key]

	def font(self, key):
		if key not in self._fonts:
			path, size, bold, italic = self.font_defs[key]
			font = pygame.font.Font(path, size)
			font.set_bold(bold)
			font.set_italic(italic)
			self._fonts[key] = font
		return self._fonts[key]

DARK_THEME = Theme(
	name = "dark",
	colors = {
		"background": (20, 20, 40),
		"player": (100, 200, 255),
		"bullet": (100, 255, 255),
		"asteroid_big": (180, 100, 80),
		"asteroid_small": (220, 140, 100),
		"text_primary": (220, 220, 220),
		"text_secondary": (160, 160, 160),
		"overlay_start": (0, 0, 0, 120),
		"overlay_pause": (20, 30, 40, 150),
		"overlay_game_over": (90, 0, 0, 170),
		"overlay_game_win": (0, 60, 30, 140)
	},
	fonts = {
		"large": (None, 50, False, False),
		"medium": (None, 25, False, False),
		"small": (None, 15, False, False)
	}
)

LIGHT_THEME = Theme(
	name = "light",
	colors = {
		"background": (180, 210, 240),
		"player": (80, 160, 220),
		"bullet": (0, 0, 255),
		"asteroid_big": (200, 130, 100),
		"asteroid_small": (240, 160, 120),
		"text_primary": (30, 30, 30),
		"text_secondary": (80, 80, 80),
		"overlay_start": (255, 255, 255, 160),
		"overlay_pause": (210, 210, 210, 150),
		"overlay_game_over": (160, 40, 40, 160),
		"overlay_game_win": (100, 200, 140, 140)
	},
	fonts = {
		"large": (None, 50, False, False),
		"medium": (None, 25, False, False),
		"small": (None, 15, False, False)
	}
)

THEMES = [DARK_THEME, LIGHT_THEME]