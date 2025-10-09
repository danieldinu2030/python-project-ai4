import pygame
from settings import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, screen
from character import player
from objects import obj_list
from worlds import world1 # this will become deprecated once we add more worlds

pygame.init()
clock = pygame.time.Clock()
run = True

# background
sky_surf = pygame.image.load('backgrounds/sky.jpg')
sky_surf = pygame.transform.scale(sky_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))


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

        for obj in obj_list:
                obj.obj_animation()

        pygame.display.update()

pygame.quit()
