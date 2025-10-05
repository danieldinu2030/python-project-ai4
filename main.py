import pygame

pygame.init()



run = True
# block -> 16px
block_size = 16
screen_width = 1152 # 16px * 72
screen_height = 864 # 16px * 54
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60


class World():
        def __init__(self, grid):
                self.block_list = []

                grass_img = pygame.image.load('ClassicPlatformerAssets/GrassBlockBuildable/grassblocksetBuildable1.png')
                dirt_img = pygame.image.load('ClassicPlatformerAssets/GrassBlockBuildable/grassblocksetBuildable4.png')

                row_count = 0
                for row in grid:
                        col_count = 0
                        for block in row:
                                if block == 1:
                                        # dirt block
                                        image = pygame.transform.scale(dirt_img, (block_size, block_size))
                                        dirt_rect = image.get_rect()
                                        dirt_rect.x = block_size * col_count
                                        dirt_rect.y = block_size * row_count
                                        block_var = (image, dirt_rect)
                                        self.block_list.append(block_var)
                                if block == 2:
                                        # grass block
                                        image = pygame.transform.scale(grass_img, (block_size, block_size))
                                        grass_rect = image.get_rect()
                                        grass_rect.x = block_size * col_count
                                        grass_rect.y = block_size * row_count
                                        block_var = (image, grass_rect)
                                        self.block_list.append(block_var)
                                col_count += 1
                        row_count += 1
        def draw(self):
                for block in self.block_list:
                        screen.blit(block[0], block[1])
                        pygame.draw.rect(screen, (255, 255, 255), block[1], 1) # for clarity
                        


class Player():
        def __init__(self, x, y):
                self.player_gravity = 10
                self.player_width = 48
                self.player_height = 48
                self.img_index = 0
                self.img_list = []
                self.img = pygame.image.load('brackeys_platformer_assets/sprites/knight.png').convert_alpha()
                self.player_rect = pygame.rect.Rect(x, y, self.player_width, self.player_height)
                

        def get_img(self, sheet, width, height, color):
                
                for i in range(0, 8):
                        img = pygame.surface.Surface((width, height)).convert_alpha()
                        img.blit(sheet, (0, 0), (width * i, 2 * height, width * (i + 1), 3 * height))
                        img = pygame.transform.scale(img, (self.player_width, self.player_height))
                        img.set_colorkey(color)
                        self.player_mask = pygame.mask.from_surface(img) # mask for better collision
                        img_rect = img.get_rect()
                        image = (img, img_rect, self.player_mask)
                        self.img_list.append(image)

         
                
        
        def update(self):


                # GAVITY AND COLLISION NOT FINISHED YET
                dx = 0
                dy = 0

                keys = pygame.key.get_pressed()

                if keys[pygame.K_DOWN] == True:
                        dy += 5

                if keys[pygame.K_RIGHT] == True:
                        self.img_index += 0.1
                        dx += 5
                if keys[pygame.K_LEFT] == True:
                        self.img_index += 0.1
                        dx -= 5
                if keys[pygame.K_SPACE] == True:
                        dy -= 5
                
                self.player_rect.x += dx
                self.player_rect.y += dy

                if int(self.img_index) >= len(self.img_list):
                        self.img_index = 0
                
                img_frame = self.img_list[int(self.img_index)][0] # the surface

                pygame.draw.rect(screen, (255, 255, 255), self.player_rect, 3) # for clarity
                screen.blit(img_frame, self.player_rect)



                




# for clarity 
# def draw_grid():
#         for line in range(0, 73):
#                 pygame.draw.line(screen, (0, 0, 0), (0, line * block_size), (screen_width, line * block_size))
#                 pygame.draw.line(screen, (0, 0, 0), (line * block_size, 0), (line * block_size, screen_height))


world1_data = []

with open("worlds/world1.txt") as file:
        for line in file:
                world1_data.append([int(c) for c in line.strip()])



world1 = World(world1_data)

# background
sky_surf = pygame.image.load('backgrounds/sky.jpg')
sky_surf = pygame.transform.scale(sky_surf, (screen_width, screen_height))

player = Player(3 * block_size, screen_height - 6 * block_size)

player.get_img(player.img, 32, 32, (0, 0, 0))

while run:
        clock.tick(FPS)

        screen.blit(sky_surf, (0, 0))

        # Keep this commented unless you want to debug the screen layout
        #draw_grid()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        world1.draw()




        player.update()

        pygame.display.update()

pygame.quit()
        
