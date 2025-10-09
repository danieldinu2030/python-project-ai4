# General usage parameters and game settings

BLOCK_SIZE = 16 # px
SCREEN_WIDTH = 1152 # 16px * 72 blocks
SCREEN_HEIGHT = 864 # 16px * 54 blocks
DEATH_SCREEN_DURATION = 5000 # miliseconds
FPS = 60
RUNNING_IMAGE_INCREMENT = 0.1
ROLLING_IMAGE_INCREMENT = 0.15 # faster rolling animation
IDLE_IMAGE_INCREMENT = 0.1
OBJECT_IMAGE_INCREMENT = 0.1

from pygame import display
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
