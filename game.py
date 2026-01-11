import pygame
import sys
import random
import settings
import math

from overlay import GlobalOverlayHandler, LocalOverlayHandler
from player import Player
from enemy import Enemy
from bullet import Bullet
from themes import THEMES, DARK_THEME, LIGHT_THEME

class GameState:
	START = 1,
	PAUSED = 2,
	PLAYING = 3,
	GAME_OVER = 4

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
		pygame.display.set_caption("Asteroid Game v1.1.1")

		self.fps = settings.FPS
		self.clock = pygame.time.Clock()
		self.running = True
		self.state = None
		self.theme = random.choice(THEMES)
		self.overlay_global = GlobalOverlayHandler(pygame.Surface((settings.WIDTH, settings.HEIGHT), pygame.SRCALPHA), self.theme)
		self.overlay_local = LocalOverlayHandler(pygame.Surface((settings.WIDTH, settings.HEIGHT), pygame.SRCALPHA), self.theme)

		self.set_state(GameState.START, True, True)

		self.frame_count = 0
		self.update_count = 0
		self.draw_count = 0
		self.event_count = 0

		self.day_duration = settings.DAY_DURATION
		self.day_length = self.day_duration * self.fps
		self.is_day = True if self.theme.name == LIGHT_THEME.name else False
		self.cycle_time = 0 if self.is_day else self.day_length // 2

		self.all_sprites = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.player = Player(160, 400, self.theme)
		self.all_sprites.add(self.player)

		self.game_start_time = pygame.time.get_ticks()
		self.score_changed = True
		self.score = 0
		self.high_score = 0
		self.lives = min(100, settings.LIVES)
		self.enemy_last_spawn = self.game_start_time
		self.bullet_last_spawn = self.game_start_time
		self.last_hit = self.game_start_time
		self.invincible_duration = 1000
		self.bullet_spawn_delay = 250
		self.enemy_spawn_delay = settings.ENEMY_SPAWN_DELAY

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			active = self.is_window_active(event)
			if active is not None:
				if active:
					self.fps = settings.FPS
				else:
					self.fps = 15
					self.set_state(GameState.PAUSED)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					if self.state != GameState.PLAYING:
						self.end_game()
				if event.key == pygame.K_RETURN:
					if self.state == GameState.START:
						self.set_state(GameState.PLAYING, True)
					elif self.state == GameState.GAME_OVER:
						self.restart_run()
				if event.key == pygame.K_ESCAPE:
					if self.state == GameState.PLAYING:
						self.set_state(GameState.PAUSED, True)
					elif self.state == GameState.PAUSED:
						self.set_state(GameState.PLAYING, True)
				if event.key == pygame.K_SPACE:
					if self.state == GameState.PLAYING:
						self.shoot_bullet()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.state == GameState.PLAYING:
					self.shoot_bullet()

			self.event_count += 1

	def is_window_active(self, event):
		if hasattr(pygame, 'WINDOWFOCUSLOST'):
			if event.type in (pygame.WINDOWFOCUSGAINED, pygame.WINDOWRESTORED):
				return True
			elif event.type in (pygame.WINDOWFOCUSLOST, pygame.WINDOWMINIMIZED):
				return False
		elif event.type == pygame.ACTIVEEVENT:
			if event.state == 1:
				if event.gain == 1 and self.state != GameState.PLAYING:
					return True # Mouse entry.
				elif event.gain == 0 and self.state != GameState.PLAYING:
					return False # Mouse exit.
			elif event.state == 2 and event.gain == 0:
				return False # Focus loss.
		elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN) and self.state != GameState.PLAYING:
			return True # Key/Mouse click. (when paused; checks focus received)
		elif event.type == pygame.VIDEOEXPOSE:
			return True # Window Repaint.
		else:
			return None

	def spawn_enemies(self):
		current_time = pygame.time.get_ticks()
		elapsed_ms = current_time - self.game_start_time
		minutes_played = elapsed_ms / 60000

		if (current_time - self.enemy_last_spawn) > self.enemy_spawn_delay:
			speed_multiplier = min(settings.BASE_SPEED + (minutes_played * (settings.SPEED_MULTIPLIER_PROGRESS / 4)), 1.25)
			self.enemy_spawn_delay = max(200, self.enemy_spawn_delay / speed_multiplier)
			enemy = Enemy(random.randint(5, 315), -15, self.theme, elapsed_ms)
			self.all_sprites.add(enemy)
			self.enemies.add(enemy)
			self.enemy_last_spawn = current_time

	def shoot_bullet(self):
		current_time = pygame.time.get_ticks()
		if (current_time - self.bullet_last_spawn) > self.bullet_spawn_delay:
			tip_x = self.player.rect.centerx
			tip_y = self.player.rect.top + 1
			elapsed_ms = current_time - self.game_start_time

			bullet = Bullet(tip_x, tip_y, self.theme, elapsed_ms)
			self.all_sprites.add(bullet)
			self.bullets.add(bullet)
			self.bullet_last_spawn = current_time

	def restart_run(self):
		self.all_sprites.empty()
		self.enemies.empty()
		self.bullets.empty()

		self.game_start_time = pygame.time.get_ticks()
		self.score = 0
		self.lives = settings.LIVES
		self.enemy_last_spawn = self.game_start_time
		self.bullet_last_spawn = self.game_start_time
		self.last_hit = self.game_start_time
		self.score_changed = True
		self.lives_changed = True

		self.player = Player(160, 400, self.theme)
		self.all_sprites.add(self.player)
		self.set_state(GameState.PLAYING, True, True)

	def change_score(self, score):
		self.score += score
		if self.score > self.high_score:
			self.high_score = self.score
		self.score_changed = True

	def update(self, dt):
		if not self.running or self.state != GameState.PLAYING:
			return
		keys = pygame.key.get_pressed()

		for sprite in self.all_sprites:
			if hasattr(sprite, 'update'):
				if sprite == self.player:
					sprite.update(dt, keys)
				else:
					sprite.update(dt)

		self.spawn_enemies()

		hits = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
		for bullet, hit_enemies in hits.items():
			for enemy in hit_enemies:
				if self.lives != -1:
					self.change_score(enemy.score)

		current_time = pygame.time.get_ticks()
		if (current_time - self.last_hit) > self.invincible_duration:
			hits = pygame.sprite.spritecollide(self.player, self.enemies, False)
			if hits:
				if self.lives != -1:
					self.lives -= 1
					if self.lives <= 0:
						self.set_state(GameState.GAME_OVER, True)

				self.last_hit = current_time
				self.lives_changed = True

		old_day_state = self.is_day
		self.cycle_time = (self.cycle_time + 1) % self.day_length
		self.is_day = self.cycle_time < (self.day_length // 2)

		if old_day_state != self.is_day:
			self.theme = LIGHT_THEME if self.is_day else DARK_THEME
			self.overlay_global.on_theme_change(self.theme)

		self.update_count += 1

	def draw(self):
		self.screen.fill(self.theme.color("background"))

		if self.state != GameState.START:
			current_time = pygame.time.get_ticks()

			for sprite in self.all_sprites:
				if hasattr(sprite, 'draw'):
					if sprite == self.player:
						is_invincible = (current_time - self.last_hit) < self.invincible_duration
						sprite.draw(self.screen, is_invincible, current_time)
					else:
						sprite.draw(self.screen)
				else:
					self.all_sprites.draw(self.screen)

		if self.state == GameState.PLAYING:
			if self.score_changed or self.lives_changed:
				self.overlay_local.draw_info(self)
				self.score_changed = False
				self.lives_changed = False
			self.overlay_local.draw(self.screen)

		self.overlay_global.draw(self.screen)
		pygame.display.flip()
		self.draw_count += 1

	def set_state(self, state, force=False, refresh=False):
		if state != self.state and (force or not self.overlay_global.active) or refresh:
			self.state = state
			self.overlay_global.reset()

			if self.state == GameState.START: self.overlay_global.draw_start()
			elif self.state == GameState.PAUSED: self.overlay_global.draw_pause_menu(self)
			elif self.state == GameState.GAME_OVER: self.overlay_global.draw_game_over(self)

	def end_game(self):
		self.running = False

	def run(self):
		while self.running:
			dt = min(1.0 / 10.0, self.clock.tick(self.fps) / 1000.0)
			self.handle_events()
			self.update(dt)
			self.draw()

			self.frame_count += 1

		pygame.quit()
		sys.exit()