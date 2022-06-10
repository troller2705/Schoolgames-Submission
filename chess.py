import pygame
from board import ChessBoard
from userInterface import UserInterface


class Chess():
    pygame.init()
    DISPLAY_W = 600
    DISPLAY_H = 600
    surface = pygame.display.set_mode([DISPLAY_W, DISPLAY_H], pygame.FULLSCREEN)
    pygame.display.set_caption('Chess')
    Board = ChessBoard()
    UI = UserInterface(surface, Board)
    UI.playGame()
    pygame.quit()
