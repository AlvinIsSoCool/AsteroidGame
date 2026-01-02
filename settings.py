WIDTH = 320
HEIGHT = 480
FPS = 30

""" Number of seconds the whole day lasts for. (Default: 300 seconds or 5 minutes).
	Day/Night switching happens at half of this time (Default: 150 seconds or 2.5 minutes).
"""
DAY_DURATION = 300

""" Difficulty Options. Change the following values carefully.

	- LIVES: Number of lives the player gets before the game ends. (Default: 3 lives)
	- ENEMY_SPAWN_DELAY: The time that it takes for enemies to spawn. (Default: 1000ms or 1 second)
	- BASE_SPEED: The base speed that the elements will take. (Default: 1.0 or 100% speed)
	- SPEED_MULTIPLIER_PROGRESS: The percentage per minute the speed multiplies by. (Default: 0.1 or 10% per minute)
	- SPEED_MULTIPLIER_CAP: Caps speed multiplication to the defined value. Keeps difficulty sustainable. (Default: 4.0 or 400% speed)
	- BASE_DRIFT: The base drift that the elements will take. (Default: 1.0 or 100% drift)
	- DRIFT_MULTIPLIER_PROGRESS: The percentage per minute the drift multiplies by. (Default: 0.01 or 1% per minute)
	- DRIFT_MULTIPLIER_CAP: Caps drift multiplication to the defined value. Keeps difficulty sustainable. (Default: 2.0 or 200% drift)

	NOTE: Number of lives can be as high as needed. By default, it caps at 100 lives.
		  In the situation, where infinite lives are needed, the LIVES value can be set to -1.
		  This will prevent natural death. If you have to quit the game, press Q from the game menu.
		  Beware: setting LIVES to -1 will prevent score incrementing. Use only for testing purposes!
		  Drift Multiplication is subtle but makes asteroids and bullets move in the x axis randomly and sometimes wildly, if the values are
		  tweaked.
		  Speed Multiplication is more noticable, and makes everything move faster, sometimes wildly, if the values are tweaked.
		  Difficulty can scale a lot, if these values are changed at random. Speed multiplication also affects enemy spawn delay.
		  Player speed is not affected by these settings. They are internal values that are not configurable.
		  Changing FPS from the default of 30FPS to 60FPS will drastically increase difficulty, because the speed of everything
		  is dependent on FPS. Tweak every setting to your liking, if the FPS is changed.
"""
LIVES=3
ENEMY_SPAWN_DELAY=1000
BASE_SPEED=1.0
SPEED_MULTIPLIER_PROGRESS=0.1
SPEED_MULTIPLIER_CAP=4.0
BASE_DRIFT=1.0
DRIFT_MULTIPLIER_PROGRESS=0.01
DRIFT_MULTIPLIER_CAP=2.0