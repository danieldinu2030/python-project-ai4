# Everything about the objects (an object is anything that can be "collected")

import pygame
from settings import screen

class Object():
    def __init__(self, path_to_sheet, x, y): # x, y -> placement
        self.object_sheet = pygame.image.load(path_to_sheet)
        self.object_img_list = []
        self.object_shown = True
        self.object_img_index = 0
        self.obj_width = 16
        self.obj_height = 16
        self.obj_rect = pygame.rect.Rect(x, y, self.obj_width, self.obj_height)
        
    def get_obj_img(self, width, height, color, row_number, number_of_images, list_of_images):
        for i in range(0, number_of_images):
            obj_img = pygame.surface.Surface((width, height)).convert_alpha()
            obj_img.blit(self.object_sheet, (0, 0), (i * width, (row_number - 1) * height, (i + 1) * width, row_number * height))
            obj_img.set_colorkey(color)
            obj_rect = obj_img.get_rect()
            obj_mask = pygame.mask.from_surface(obj_img)
            obj = (obj_img, obj_rect, obj_mask)
            list_of_images.append(obj)
        
    def obj_animation(self): 
        if self.object_shown == True:
            self.object_img_index += 0.1 
            if self.object_img_index >= len(self.object_img_list):
                self.object_img_index = 0
            obj_surface = self.object_img_list[int(self.object_img_index)][0]
            screen.blit(obj_surface, self.obj_rect)
        

# objects

obj_list = []

coin = Object('brackeys_platformer_assets/sprites/coin.png', 700, 750) # test coordinates 
coin.get_obj_img(16, 16, (0, 0, 0), 1, 12, coin.object_img_list)

obj_list.append(coin)