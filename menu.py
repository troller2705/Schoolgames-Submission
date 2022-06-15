import pygame

class Menu:
    def __init__(self, game):
        self.game = game
        self.x, self.y = self.game.display.get_size()
        self.mid_w, self.mid_h = self.x / 2, self.y / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

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
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

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
            self.draw_cursor()
            self.game.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            pygame.mixer.Sound.play(self.game.click)
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + -70, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + -70, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.exitx + -40, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            pygame.mixer.Sound.play(self.game.click)
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + -40, self.exity)
                self.state = 'Exit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + -70, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsx + -70, self.creditsy)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                import chess
                self.run_display = False
                chess.Chess()
                pygame.quit()
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Exit':
                pygame.quit()

            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 200
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 225
        self.cursor_rect.midtop = (self.volx + -60, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text('Volume', 20, self.volx, self.voly)
            self.game.draw_text('Controls', 20, self.controlsx, self.controlsy)
            self.draw_cross()
            self.draw_cursor()
            self.game.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            pygame.mixer.Sound.play(self.game.click)
            if self.state == 'Volume':
                self.cursor_rect.midtop = (self.controlsx + -80, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.volx + -60, self.voly)
                self.state = 'Volume'
        elif self.game.UP_KEY:
            pygame.mixer.Sound.play(self.game.click)
            if self.state == 'Volume':
                self.cursor_rect.midtop = (self.controlsx + -80, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.volx + -60, self.voly)
                self.state = 'Volume'

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        if self.game.START_KEY:
            if self.state == 'Volume':
                self.game.curr_menu = self.game.volume_menu
            elif self.state == 'Controls':
                self.game.curr_menu = self.game.controls_menu

            self.run_display = False


class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Music Mute'
        self.volx, self.voly = self.mid_w, self.mid_h + 225
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 250
        self.cursor_rect.midtop = (self.volx + -85, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Volume', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text(f'Music:{self.game.mute1}', 20, self.volx, self.voly)
            self.game.draw_text(f'Sound:{self.game.mute2}', 20, self.controlsx, self.controlsy)
            self.draw_cross()
            self.draw_cursor()
            self.game.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            pygame.mixer.Sound.play(self.game.click)
            if self.state == 'Music Mute':
                self.cursor_rect.midtop = (self.controlsx + -90, self.controlsy)
                self.state = 'Sound Mute'
            elif self.state == 'Sound Mute':
                self.cursor_rect.midtop = (self.volx + -90, self.voly)
                self.state = 'Music Mute'
        elif self.game.UP_KEY:
            pygame.mixer.Sound.play(self.game.click)
            if self.state == 'Music Mute':
                self.cursor_rect.midtop = (self.controlsx + -90, self.controlsy)
                self.state = 'Sound Mute'
            elif self.state == 'Sound Mute':
                self.cursor_rect.midtop = (self.volx + -90, self.voly)
                self.state = 'Music Mute'

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False
        if self.game.START_KEY:
            if self.state == 'Music Mute' and self.game.mute1 == 'Off':
                pygame.mixer.music.unpause()
                self.game.mute1 = 'On'
            elif self.state == 'Music Mute' and self.game.mute1 == 'On':
                pygame.mixer.music.pause()
                self.game.mute1 = 'Off'
            elif self.state == 'Sound Mute' and self.game.mute2 == 'Off':
                self.game.mute2 = 'On'
            elif self.state == 'Sound Mute' and self.game.mute2 == 'On':
                self.game.mute2 = 'Off'


class ControlsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.volx, self.voly = self.mid_w, self.mid_h + 200
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 225
        self.videox, self.videoy = self.mid_w, self.mid_h + 250

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Controls', 30, self.mid_w, self.mid_h - 200)
            self.game.draw_text('Arrow Keys', 20, self.volx, self.voly)
            self.game.draw_text('Enter', 20, self.controlsx, self.controlsy)
            self.game.draw_text('Backspace', 20, self.videox, self.videoy)
            self.draw_cross()
            self.game.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.options
            self.run_display = False


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
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
