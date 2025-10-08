import pygame
from settings import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, screen
from character import Player
from worlds import world1 # this will become deprecated once we add more worlds

pygame.init()
clock = pygame.time.Clock()
run = True

# background
sky_surf = pygame.image.load('backgrounds/sky.jpg')
sky_surf = pygame.transform.scale(sky_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(4 * BLOCK_SIZE, SCREEN_HEIGHT - 7 * BLOCK_SIZE)
# getting running images
player.get_img(player.img, 32, 32, (0, 0, 0), 3, 8, player.running_img_list)
# getting rolling images
player.get_img(player.img, 32, 32, (0, 0, 0), 6, 8, player.rolling_img_list)
# getting idle images
player.get_img(player.img, 32, 32, (0, 0, 0), 1, 4, player.idle_image_list)



while run:
        clock.tick(FPS)

        screen.blit(sky_surf, (0, 0))

        # for clarity 
        # def draw_grid():
        #         for line in range(0, 73):
        #                 pygame.draw.line(screen, (0, 0, 0), (0, line * block_size), (screen_width, line * block_size))
        #                 pygame.draw.line(screen, (0, 0, 0), (line * block_size, 0), (line * block_size, screen_height))
        # Keep this commented unless you want to debug the screen layout
        #draw_grid()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        world1.draw()

        player.update()

        pygame.display.update()

pygame.quit()
