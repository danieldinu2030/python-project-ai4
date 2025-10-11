import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, LOSS_SCREEN_DURATION, MAIN_MENU, screen, loss_sound, mixer
from character import player
from objects import obj_list
from worlds import world1
from buttons import Button

pygame.init()

#class Game():
#        def __init__(self):
#                self.setup()
#                self.running = True
#                self.gameover = False
#                self.run()

class Level():
        def __init__(self, bg_img, world):
                self.running = True
                # background
                bg_surf = pygame.image.load(bg_img)
                self.bg_surf = pygame.transform.scale(bg_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
                # world map
                self.world = world
                # timer start
                self.clock = pygame.time.Clock()

        # once there is a main menu
        #def go_to_main_menu(self):

        def update(self):
                screen.blit(self.bg_surf, (0, 0))
                self.world.draw()
                self.display_score()
                self.display_time()
                player.update()

                for obj in obj_list:
                        obj.obj_animation()

                if player.player_rect.y < SCREEN_HEIGHT:        
                        pygame.display.update()
                else:
                        self.display_fallen(pygame.time.get_ticks())
                        pygame.display.update()
                        mixer.music.unload() # stop background music
                        loss_sound.play()
                        pygame.time.delay(LOSS_SCREEN_DURATION)
                        self.running = False

        def display_score(self):
                score_font = pygame.font.Font('brackeys_platformer_assets/fonts/PixelOperator8-Bold.ttf', 25)
                score = player.coins_collected * 10
                score_surf = score_font.render(f'Score: {score}', True, (64, 64, 64))
                score_rect = score_surf.get_rect(center = (SCREEN_WIDTH - 150, 50))
                screen.blit(score_surf, score_rect)

        def display_time(self):
                time_font = pygame.font.Font('brackeys_platformer_assets/fonts/PixelOperator8-Bold.ttf', 25)
                time = pygame.time.get_ticks()
                time = (int)(time / 1000) # transform to seconds
                minutes = (int)(time / 60)
                seconds = (int)(time % 60)
        
                if seconds < 10:
                        time_surf = time_font.render(f'Time: 0{minutes}:0{seconds}', True, (64, 64, 64))
                elif seconds < 60:
                        time_surf = time_font.render(f'Time: 0{minutes}:{seconds}', True, (64, 64, 64))
                time_rect = time_surf.get_rect(center = (SCREEN_WIDTH - 150, 100))
                screen.blit(time_surf, time_rect)

        def display_fallen(self, time):
                pygame.time.delay(250) # avoid making the transition very sudden
                bg_surf = pygame.image.load('backgrounds/fallen_menu.jpg')
                bg_surf = pygame.transform.scale(bg_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
                screen.blit(bg_surf, (0, 0))

                fallen_font = pygame.font.Font('brackeys_platformer_assets/fonts/PixelOperator8-Bold.ttf', 45)
                score = player.coins_collected * 10
                time = (int)(time / 1000) # transform to seconds
                minutes = (int)(time / 60)
                seconds = (int)(time % 60)

                fallen_surf = fallen_font.render(f'You have fallen!', True, (64, 64, 64))
                fallen_rect = fallen_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60)) # determined by successive tries

                score_surf = fallen_font.render(f'Score: {score}', True, (64, 64, 64))
                score_rect = score_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

                if seconds < 10:
                        time_surf = fallen_font.render(f'Time: 0{minutes}:0{seconds}', True, (64, 64, 64))
                elif seconds < 60:
                        time_surf = fallen_font.render(f'Time: 0{minutes}:{seconds}', True, (64, 64, 64))
                time_rect = time_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60))

                #restart_button = Button(400, 400, "Try Again")
                #restart_button.get_img("button_images_01", 5, "png")

                screen.blit(fallen_surf, fallen_rect)
                screen.blit(score_surf, score_rect)
                screen.blit(time_surf, time_rect)



running = True

start_button = Button(400, 400, "Start") # test coordinates (will change for final main menu)
start_button.get_img("button_images_01", 5, "png")

level1 = Level('backgrounds/sky.jpg', world1)

while running:
        level1.clock.tick(FPS)

        # for clarity 
        # def draw_grid():
        #         for line in range(0, 73):
        #                 pygame.draw.line(screen, (0, 0, 0), (0, line * block_size), (screen_width, line * block_size))
        #                 pygame.draw.line(screen, (0, 0, 0), (line * block_size, 0), (line * block_size, screen_height))
        # Keep this commented unless you want to debug the screen layout
        #draw_grid()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        if MAIN_MENU == True:
                start_button.update()
                if start_button.was_pressed >= 1:
                        MAIN_MENU = False
                pygame.display.update()
        elif level1.running == True:
                level1.update()
        else:
                running = False

pygame.quit()
