import pygame

class Menu:
    def __init__(self, game):
        self.game = game
        self.x, self.y = self.game.display.get_size()
        self.mid_w, self.mid_h = self.x / 2, self.y / 2
        self.run_display = True
        self.offset = -100

    def draw_cross(self):
        for y_offset in range(0, 100, 10):
            pygame.draw.line(self.game.display, self.game.RED,
                             [0, 0 + y_offset], [self.x, self.y + y_offset], 2)
            pygame.draw.line(self.game.display, self.game.RED,
                             [0, self.y + y_offset], [self.x, 0 + y_offset], 2)
        # pygame.draw.polygon(self.game.display, self.game.RED,
        #   [[self.mid_w, self.mid_h], [340, 345], [400, 390], [460, 345]], 0)


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.startx, self.starty = self.mid_w, self.mid_h + 200
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 225
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 250
        self.exitx, self.exity = self.mid_w, self.mid_h + 275
        self.prect = pygame.Rect(self.startx - 25, self.starty - 5, 100, 10)
        self.orect = pygame.Rect(self.optionsx - 25, self.optionsy - 5, 100, 10)
        self.crect = pygame.Rect(self.creditsx - 25, self.creditsy - 5, 100, 10)
        self.erect = pygame.Rect(self.exitx - 25, self.exity - 5, 100, 10)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            # double quotes for use of apostrophe
            self.game.draw_text("Troller's Paradise", 30, self.mid_w, self.mid_h - 250)
            self.game.draw_text('Start Game', 20, self.startx, self.starty)
            self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
            self.game.draw_text('Exit', 20, self.exitx, self.exity)
            self.draw_cross()
            self.game.blit_screen()

    def check_input(self):
        self.pos = pygame.mouse.get_pos()
        if self.game.click:
            if self.prect.collidepoint(self.pos):
                import chess
                self.run_display = False
                chess.Chess()
            elif self.orect.collidepoint(self.pos):
                self.game.curr_menu = self.game.options
            elif self.crect.collidepoint(self.pos):
                self.game.curr_menu = self.game.credits
            elif self.erect.collidepoint(self.pos):
                pygame.quit()

            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 200
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 225
        self.backx, self.backy = self.mid_w, self.mid_h + 250
        self.vrect = pygame.Rect(self.volx - 25, self.voly - 5, 100, 10)
        self.crect = pygame.Rect(self.controlsx - 25, self.controlsy - 5, 100, 10)
        self.brect = pygame.Rect(self.backx - 25, self.backy - 5, 100, 10)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text('Volume', 20, self.volx, self.voly)
            self.game.draw_text('Controls', 20, self.controlsx, self.controlsy)
            self.game.draw_text('Back', 20, self.backx, self.backy)
            self.draw_cross()
            self.game.blit_screen()

    def check_input(self):
        self.pos = pygame.mouse.get_pos()
        if self.game.click:
            if self.vrect.collidepoint(self.pos):
                self.game.curr_menu = self.game.volume_menu
            elif self.crect.collidepoint(self.pos):
                self.game.curr_menu = self.game.controls_menu
            elif self.brect.collidepoint(self.pos):
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.run_display = False


class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.volx, self.voly = self.mid_w, self.mid_h + 225
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 250
        self.backx, self.backy = self.mid_w, self.mid_h + 275
        self.mrect = pygame.Rect(self.volx - 25, self.voly - 5, 100, 10)
        self.srect = pygame.Rect(self.controlsx - 25, self.controlsy - 5, 100, 10)
        self.brect = pygame.Rect(self.backx - 25, self.backy - 5, 100, 10)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Volume', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text(f'Music:{self.game.mute1}', 20, self.volx, self.voly)
            self.game.draw_text(f'Sound:{self.game.mute2}', 20, self.controlsx, self.controlsy)
            self.game.draw_text('Back', 20, self.backx, self.backy)
            self.draw_cross()
            self.game.blit_screen()

    def check_input(self):
        self.pos = pygame.mouse.get_pos()
        if self.game.click:
            if self.mrect.collidepoint(self.pos) and self.game.mute1 == 'Off':
                pygame.mixer.music.unpause()
                self.game.mute1 = 'On'
            elif self.mrect.collidepoint(self.pos) and self.game.mute1 == 'On':
                pygame.mixer.music.pause()
                self.game.mute1 = 'Off'
            elif self.srect.collidepoint(self.pos) and self.game.mute2 == 'Off':
                self.game.mute2 = 'On'
            elif self.srect.collidepoint(self.pos) and self.game.mute2 == 'On':
                self.game.mute2 = 'Off'
            elif self.brect.collidepoint(self.pos):
                self.game.curr_menu = self.game.options
                self.run_display = False


class ControlsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.volx, self.voly = self.mid_w, self.mid_h + 200

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Controls', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text('Mouse', 20, self.volx, self.voly)
            self.draw_cross()
            self.game.blit_screen()

    def check_input(self):
        if self.game.click:
            self.game.curr_menu = self.game.options
            self.run_display = False


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.click:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 40, self.mid_w, self.mid_h - 200)
            self.game.draw_text('Made by Deathboard Productions', 25, self.mid_w, self.mid_h - 100)
            self.game.draw_text('Lead Developer, Graphics Designer, Sound Engineer:', 15, self.mid_w, self.mid_h + 25)
            self.game.draw_text('Troller AKA Cole', 25, self.mid_w, self.mid_h + 50)

            self.game.blit_screen()

pygame.display.quit()
pygame.quit()
