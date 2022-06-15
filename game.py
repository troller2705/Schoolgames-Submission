import pygame

from menu import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.running = True
        self.click = False
        self.DISPLAY_W = pygame.display.get_desktop_sizes()[0][0]
        self.DISPLAY_H = pygame.display.get_desktop_sizes()[0][1]
        self.display = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H), pygame.FULLSCREEN)
        Menu_icon = pygame.image.load('UI/icon.png')
        pygame.display.set_icon(Menu_icon)
        pygame.display.set_caption("Troller's Paradise")
        self.clock = pygame.time.Clock()
        self.font_name = 'UI/8-Bit.ttf'
        self.BLACK, self.WHITE, self.GREEN, self.RED, self.BLUE = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 100, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.volume_menu = VolumeMenu(self)
        self.controls_menu = ControlsMenu(self)
        self.curr_menu = self.main_menu
        self.mute1 = 'On'
        self.mute2 = 'On'
        pygame.mixer.music.load('Music&Sounds/Menu/8_Bit_Menu.mp3')
        pygame.mixer.music.play(-1)

        self.click = pygame.mixer.Sound('Music&Sounds/Menu/Cursor.wav')
        self.clock.tick(60)

    def blit_screen(self):
        self.display.blit(self.display, (0, 0))
        pygame.display.update()
        self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.curr_menu.run_display = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click = True

    def reset_keys(self):
        self.click = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
