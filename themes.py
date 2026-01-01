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
			try:
				font = pygame.font.Font(path, size)
			except:
				font = pygame.font.Font(None, size)
			font.set_bold(bold)
			font.set_italic(italic)
			self._fonts[key] = font
		return self._fonts[key]

	def get_text_size(self, key, text):
		return self.font(key).size(text)

	def get_text_width(self, key, text):
		len = self.get_text_size(key, text)[0]
		print(f"Length: {len}")
		return len

	def get_text_height(self, key, text):
		return self.get_text_size(key, text)[1]

DARK_THEME = Theme(
	name = "dark",
	colors = {
		"background": (10, 10, 10),
		"player": (0, 150, 255),
		"bullet": (31, 81, 255),
		"asteroid_big": (110, 38, 14),
		"asteroid_small": (165, 42, 42),
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
		"background": (255, 250, 250),
		"player": (0, 0, 139),
		"bullet": (63, 0, 255),
		"asteroid_big": (123, 63, 0),
		"asteroid_small": (160, 40, 40),
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