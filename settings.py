# General usage parameters and game settings

BLOCK_SIZE = 16 # px
SCREEN_WIDTH = 1152 # 16px * 72 blocks
SCREEN_HEIGHT = 864 # 16px * 54 blocks
FPS = 60

from pygame import display
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
