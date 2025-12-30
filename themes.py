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
		"text_primary": (220, 220, 220),
		"text_secondary": (160, 160, 160),
		"overlay_start": (0, 0, 0, 120),
		"overlay_pause": (20, 30, 40, 150),
		"overlay_game_over": (90, 0, 0, 170),
		"overlay_game_win": (0, 60, 30, 140)
	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)

LIGHT_THEME = Theme(
	name = "light",
	colors = {
		"text_primary": (30, 30, 30),
		"text_secondary": (80, 80, 80),
		"overlay_start": (255, 255, 255, 160),
		"overlay_pause": (210, 210, 210, 150),
		"overlay_game_over": (160, 40, 40, 160),
		"overlay_game_win": (100, 200, 140, 140)
	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)

THEMES = [DARK_THEME, LIGHT_THEME]