# Everything about the worlds in the game

import pygame
from settings import BLOCK_SIZE, screen
import objects

class World():
        def __init__(self, grid):
                self.block_list = []
                self.coin_list = []

                grass_img = pygame.image.load('ClassicPlatformerAssets/GrassBlockBuildable/grassblocksetBuildable1.png')
                dirt_img = pygame.image.load('ClassicPlatformerAssets/GrassBlockBuildable/grassblocksetBuildable4.png')
                water_img = pygame.image.load('ClassicPlatformerAssets/Water/water.png')

                row_count = 0
                for row in grid:
                        col_count = 0
                        for block in row:
                                if block == 1:
                                        # dirt block
                                        image = pygame.transform.scale(dirt_img, (BLOCK_SIZE, BLOCK_SIZE))
                                        dirt_rect = image.get_rect()
                                        dirt_rect.x = BLOCK_SIZE * col_count
                                        dirt_rect.y = BLOCK_SIZE * row_count
                                        block_mask = pygame.mask.from_surface(image)
                                        block_var = (image, dirt_rect, block_mask)
                                        self.block_list.append(block_var)
                                if block == 2:
                                        # grass block
                                        image = pygame.transform.scale(grass_img, (BLOCK_SIZE, BLOCK_SIZE))
                                        grass_rect = image.get_rect()
                                        grass_rect.x = BLOCK_SIZE * col_count
                                        grass_rect.y = BLOCK_SIZE * row_count
                                        block_mask = pygame.mask.from_surface(image)
                                        block_var = (image, grass_rect, block_mask)
                                        self.block_list.append(block_var)
                                if block == 3:
                                        # water block
                                        image = pygame.transform.scale(water_img, (BLOCK_SIZE, BLOCK_SIZE))
                                        water_rect = image.get_rect()
                                        water_rect.x = BLOCK_SIZE * col_count
                                        water_rect.y = BLOCK_SIZE * row_count
                                        block_mask = pygame.mask.from_surface(image)
                                        block_var = (image, water_rect, block_mask)
                                        self.block_list.append(block_var)
                                if block == 4:
                                        # coin block
                                        coin_x = BLOCK_SIZE * col_count
                                        coin_y = BLOCK_SIZE * row_count
                                        coin = objects.Object('brackeys_platformer_assets/sprites/coin.png', coin_x, coin_y)
                                        coin.get_obj_img(16, 16, (0, 0, 0), 1, 12, coin.object_img_list)
                                        objects.obj_list.append(coin)
                                col_count += 1
                        row_count += 1

        def draw(self):
                for block in self.block_list:
                        screen.blit(block[0], block[1])
                        pygame.draw.rect(screen, (255, 255, 255), block[1], 1) # for clarity

# we must also modularise this part once we add more worlds
world1_data = []

with open("worlds/world1.txt") as file:
        for line in file:
                world1_data.append([int(c) for c in line.strip()])

world1 = World(world1_data)