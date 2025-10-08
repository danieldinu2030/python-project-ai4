# Everything about the character (player)

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, screen
from worlds import world1

class Player():
        def __init__(self, x, y):
                self.player_gravity = -15
                self.player_width = 48
                self.player_height = 48
                self.img_index = 0
                self.img_list = []
                self.img = pygame.image.load('brackeys_platformer_assets/sprites/knight.png').convert_alpha()
                self.player_rect = pygame.rect.Rect(x, y, self.player_width, self.player_height)
                self.can_jump = True
                
        def get_img(self, sheet, width, height, color):
                
                for i in range(0, 8):
                        img = pygame.surface.Surface((width, height)).convert_alpha()
                        img.blit(sheet, (0, 0), (width * i, 2 * height, width * (i + 1), 3 * height))
                        img = pygame.transform.scale(img, (self.player_width, self.player_height))
                        img.set_colorkey(color)
                        player_mask = pygame.mask.from_surface(img) # mask for better collision
                        img_rect = img.get_rect()
                        image = (img, img_rect, player_mask)
                        self.img_list.append(image)
        
        def update(self):
                # movement
                dx = 0
                dy = self.player_gravity

                self.player_gravity += 1

                if self.player_gravity >= 10:
                        self.player_gravity = 10

                keys = pygame.key.get_pressed()

                if keys[pygame.K_RIGHT] == True:
                        self.img_index += 0.1
                        dx += 5
                if keys[pygame.K_LEFT] == True:
                        self.img_index += 0.1
                        dx -= 5
                if keys[pygame.K_SPACE] == True:
                        if self.can_jump == True:
                                self.player_gravity = -15
                                dy = self.player_gravity
                                self.can_jump = False # prevent button mashing and multi jumps                        

                if int(self.img_index) >= len(self.img_list):
                        self.img_index = 0

                img_mask = self.img_list[int(self.img_index)][2] # the mask of the player

                # collision

                for block in world1.block_list:
                        block_rect = block[1] # the rect of the block
                        block_mask = block[2] # the mask of the block
                        # going horizontally
                        if img_mask.overlap(block_mask, (block_rect.x - (self.player_rect.x + dx), block_rect.y - self.player_rect.y)):
                                dx = 0
                        
                        # going vertically
                        if img_mask.overlap(block_mask, (block_rect.x - self.player_rect.x, block_rect.y - (self.player_rect.y + dy))):
                                if self.player_gravity > 0: # landing on the ground
                                        dy = 0
                                        self.player_gravity = 0
                                        self.can_jump = True # jumping should be allowed whilst on the ground
                                elif self.player_gravity < 0: # hitting the ceiling
                                        dy = 0
                                        self.player_gravity = 0
                                        
                self.player_rect.y += dy 
                self.player_rect.x += dx
                
                img_frame = self.img_list[int(self.img_index)][0] # the surface                
                
                # Keep this commented unless you want to debug the player's hitbox range
                #pygame.draw.rect(screen, (255, 255, 255), self.player_rect, 3) # for clarity
                
                screen.blit(img_frame, self.player_rect)
