import pygame
import sys
import random
import settings

from overlay import GlobalOverlayHandler
from player import Player
from enemy import Enemy
from enum import Enum, auto
from themes import THEMES

class GameState(Enum):
	START = auto(),
	PAUSED = auto(),
	PLAYING = auto(),
	GAME_OVER = auto()
	GAME_WIN = auto()

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
		pygame.display.set_caption("Test Game v1")

		self.fps = settings.FPS
		self.clock = pygame.time.Clock()
		self.running = True
		self.state = None
		self.theme = random.choice(THEMES)
		self.overlay_global = GlobalOverlayHandler(pygame.Surface((settings.WIDTH + 1, settings.HEIGHT + 1), pygame.SRCALPHA).convert_alpha(), self.theme)
		print(f"Theme: {self.theme.name}")

		self.set_state(GameState.START, True, True)

		self.frame_count = 0
		self.update_count = 0
		self.draw_count = 0
		self.event_count = 0

		self.all_sprites = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		self.player = Player(160, 400)
		self.all_sprites.add(self.player)
		self.score = 0
		self.lives = 3
		self.last_spawn = 0
		self.spawn_delay = 1000

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q: 
					if self.state != GameState.PLAYING: self.end_game()
				if event.key == pygame.K_RETURN:
					if self.state == GameState.START: self.set_state(GameState.PLAYING, True)
					elif self.state == GameState.GAME_OVER or self.state == GameState.GAME_WIN: self.restart_run()
				if event.key == pygame.K_ESCAPE:
					if self.state == GameState.PLAYING: self.set_state(GameState.PAUSED, True)
					elif self.state == GameState.PAUSED: self.set_state(GameState.PLAYING, True)

			if event.type == pygame.WINDOWFOCUSLOST:
				print("Window lost focus.")
				self.set_state(GameState.PAUSED)
				self.fps /= 4

			if event.type == pygame.WINDOWFOCUSGAINED:
				print("Window gained focus.")
				self.fps = settings.FPS

			if event.type == pygame.WINDOWMINIMIZED:
				print("Window minimized.")
				self.set_state(GameState.PAUSED)
				self.fps /= 4

			if event.type == pygame.WINDOWRESTORED:
				print("Window restored.")
				self.fps = settings.FPS

			self.event_count += 1
			#print(f"Event Count: {self.event_count}")'''

	def spawn_enemies(self):
		current_time = pygame.time.get_ticks()
		if current_time - self.last_spawn > self.spawn_delay:
			enemy = Enemy(random.randint(5, 315), -20)
			self.all_sprites.add(enemy)
			self.enemies.add(enemy)
			self.last_spawn = current_time

	def restart_run(self):
		self.all_sprites.empty()
		self.enemies.empty()

		self.score = 0
		self.lives = 3
		self.last_spawn = 0

		self.player = Player(400, 300)
		self.all_sprites.add(self.player)
		self.set_state(GameState.PLAYING, True, True)

	def update(self):
		if not self.running or self.state != GameState.PLAYING:
			return

		keys = pygame.key.get_pressed()

		for sprite in self.all_sprites:
			if hasattr(sprite, 'update'):
				if sprite == self.player:
					sprite.update(keys)
				else:
					sprite.update()

		self.spawn_enemies()
		if pygame.sprite.spritecollide(self.player, self.enemies, False):
			self.set_state(GameState.GAME_OVER, True, True)

		self.update_count += 1
		#print(f"Update Count: {self.update_count}")

	def draw(self):
		self.screen.fill(self.theme.color("background"))
		if self.state != GameState.START:
			for sprite in self.all_sprites:
				if hasattr(sprite, 'draw'):
					sprite.draw(self.screen)
				else:
					self.all_sprites.draw(self.screen)
		self.overlay_global.draw(self.screen)
		pygame.display.flip()
		self.draw_count += 1

	def set_state(self, state, force=False, refresh=False):
		if (state != self.state and isinstance(state, GameState)) and (force or not self.overlay_global.active) or refresh:
			self.state = state
			self.overlay_global.reset()
			print("State changed.")

			if self.state == GameState.START: self.overlay_global.draw_start()
			elif self.state == GameState.PAUSED: self.overlay_global.draw_pause_menu()
			elif self.state == GameState.GAME_OVER: self.overlay_global.draw_game_over()
			elif self.state == GameState.GAME_WIN: self.overlay_global.draw_game_won()

	def end_game(self):
		self.running = False

	def run(self):
		while self.running:
			self.handle_events()
			self.update()
			self.draw()
			self.clock.tick(self.fps)
			self.frame_count += 1

		pygame.quit()
		sys.exit()