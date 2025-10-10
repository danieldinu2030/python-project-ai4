import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, LOSS_SCREEN_DURATION, MAIN_MENU, screen, loss_sound, mixer
from character import player
from objects import obj_list
from worlds import world1 # this will become deprecated once we add more worlds
from buttons import Button

pygame.init()
clock = pygame.time.Clock()
run = True

# background
sky_surf = pygame.image.load('backgrounds/sky.jpg')
sky_surf = pygame.transform.scale(sky_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))

def display_score():
        score_font = pygame.font.Font('brackeys_platformer_assets/fonts/PixelOperator8-Bold.ttf', 25)
        score = player.coins_collected * 10
        score_surf = score_font.render(f'Score: {score}', True, (64, 64, 64))
        score_rect = score_surf.get_rect(center = (SCREEN_WIDTH - 150, 50))
        screen.blit(score_surf, score_rect)

def display_fallen():
        fallen_font = pygame.font.Font('brackeys_platformer_assets/fonts/PixelOperator8-Bold.ttf', 45)
        score = player.coins_collected * 10
        fallen_surf = fallen_font.render(f'You have lost!', True, (64, 64, 64))
        fallen_rect = fallen_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60)) # determined by successive tries
        score_surf = fallen_font.render(f'Score: {score}', True, (64, 64, 64))
        score_rect = score_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(fallen_surf, fallen_rect)
        screen.blit(score_surf, score_rect)

start_button = Button(400, 400, "Start") # test coordinates (will change for final main menu)

start_button.get_img("button_images_01", 5, "png")

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

        if MAIN_MENU == True:
                start_button.update()
                if start_button.was_pressed >= 1:
                        MAIN_MENU = False
                pygame.display.update()
        else:
                world1.draw()
                display_score()
                player.update()

                for obj in obj_list:
                        obj.obj_animation()

                if player.player_rect.y < SCREEN_HEIGHT:        
                        pygame.display.update()
                else:
                        display_fallen()
                        pygame.display.update()
                        mixer.music.unload()

                        loss_sound.play()
                        pygame.time.delay(LOSS_SCREEN_DURATION)
                        
                        run = False
                        pygame.quit()

pygame.quit()
