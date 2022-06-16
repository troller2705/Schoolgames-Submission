import pygame
from peices import *
from ratings import Ratings
import time


class UserInterface:
    def __init__(self, surface, Board):
        self.font_name = 'UI/8-Bit.ttf'
        self.click = pygame.mixer.Sound('Music&Sounds/Sounds/Bomb_Drop.wav')
        self.surface = surface
        self.inPlay = True
        self.squareSize = 75
        self.peices = 64

        self.textSize = 20

        if pygame.display.get_desktop_sizes()[0][0] >= 1900:
            self.squareSize = 135
            self.textSize = 35
        elif pygame.display.get_desktop_sizes()[0][0] >= 1600:
            self.squareSize = 115
            self.textSize = 30
        elif pygame.display.get_desktop_sizes()[0][0] >= 1300:
            self.squareSize = 95
            self.textSize = 25
        elif pygame.display.get_desktop_sizes()[0][0] >= 1000:
            self.squareSize = 85
            self.textSize = 20
        elif pygame.display.get_desktop_sizes()[0][0] >= 800:
            self.squareSize = 55
            self.textSize = 15

        self.DISPLAY_W = self.squareSize * 8
        self.DISPLAY_H = pygame.display.get_desktop_sizes()[0][1]

        self.forfeit_rect = pygame.Rect(self.DISPLAY_W + 150, self.DISPLAY_H / 2 + 160 - self.textSize, 250, 100)

        self.mouseInitialX = 0
        self.mouseInitialY = 0

        self.mouseFinalX = 0
        self.mouseFinalY = 0

        self.chessboard = Board
        self.playerMove = ""
        self.computerMove = ""
        self.playerColor = ""
        self.computerColor = ""
        self.status = ""
        self.turn = ""

    def drawComponent(self):

        for i in range(0, self.peices, 2):
            pygame.draw.rect(self.surface, (120, 60, 30),
                             [(i % 8 + (i // 8) % 2) * self.squareSize, (i // 8) * self.squareSize, self.squareSize,
                              self.squareSize])
            pygame.draw.rect(self.surface, (245, 245, 220),
                             [((i + 1) % 8 - ((i + 1) // 8) % 2) * self.squareSize, ((i + 1) // 8) * self.squareSize,
                              self.squareSize, self.squareSize])

        for index in range(self.peices):
            currentPosition = self.chessboard.boardArray[index // 8][index % 8]

            if currentPosition == "P":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_pl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_pd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "p":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_pd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_pl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "K":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_nl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_nd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "k":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_nd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_nl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "B":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_bl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_bd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "b":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_bd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_bl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "R":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_rl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_rd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "r":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_rd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_rl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "Q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_ql.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_qd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_qd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_ql.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))


            elif currentPosition == "A":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_kl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_kd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))

            elif currentPosition == "a":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_kd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_kl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))

        pygame.display.update()

    def eventHandler(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.inPlay = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(self.click)
                if self.forfeit_rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    self.inPlay = False
                    break

                if pygame.mouse.get_pos()[0] < 8 * self.squareSize and pygame.mouse.get_pos()[1] < 8 * self.squareSize:
                    self.mouseInitialX = pygame.mouse.get_pos()[0]
                    self.mouseInitialY = pygame.mouse.get_pos()[1]

            if event.type == pygame.MOUSEBUTTONUP:

                if pygame.mouse.get_pos()[0] < 8 * self.squareSize and pygame.mouse.get_pos()[1] < 8 * self.squareSize:
                    self.mouseFinalX = pygame.mouse.get_pos()[0]
                    self.mouseFinalY = pygame.mouse.get_pos()[1]
                    self.computeMove()

    def computeMove(self):

        rowInitial = self.mouseInitialY // self.squareSize
        columnInitial = self.mouseInitialX // self.squareSize
        rowFinal = self.mouseFinalY // self.squareSize
        columnFinal = self.mouseFinalX // self.squareSize

        if rowFinal == 0 and rowInitial == 1 and self.chessboard.boardArray[rowInitial][columnInitial] == "P":

            promotionPeice = self.promote_piece()

            self.playerMove += str(columnInitial) + str(columnFinal) + str(
                self.chessboard.boardArray[rowFinal][columnFinal]) + promotionPeice + "P"


        elif rowFinal == 7 and (columnInitial == 0 or columnInitial == 7) and self.chessboard.boardArray[rowInitial][
            columnInitial] == "R" and self.chessboard.boardArray[rowFinal][columnFinal] == "A":

            if columnInitial == 0:
                self.playerMove += str(columnInitial) + str(columnFinal - 1) + str(columnFinal) + "R" + "C"
            elif columnInitial == 7:
                self.playerMove += str(columnInitial) + str(columnFinal + 1) + str(columnFinal) + "R" + "C"

        else:
            self.playerMove += str(rowInitial) + str(columnInitial) + str(rowFinal) + str(columnFinal) + str(
                self.chessboard.boardArray[rowFinal][(columnFinal)])

        if self.playerMove in self.chessboard.generateMoveList():
            self.chessboard.computeMove(self.playerMove)
            self.drawComponent()
            if self.chessboard.kingissafe() is not False:
                self.status = ""
                self.draw_status()
            self.computerMoves()
        self.playerMove = ""
        self.computerMove = ""

    def computerMoves(self):
        if self.computerColor == "W":
            self.turn = "White's Turn"
            self.draw_turn()
        else:
            self.turn = "Black's Turn"
            self.draw_turn()

        self.chessboard.changePerspective()
        self.computerMove = self.chessboard.alphaBeta(self.chessboard.MAXDEPTH, float("inf"), -float("inf"), "", 0)

        if self.computerMove is None:
            self.status = "CHECKMATE!"
            self.draw_status()
            time.sleep(15)
            self.inPlay = False

        else:
            self.chessboard.computeMove(self.computerMove)

        self.chessboard.changePerspective()
        self.drawComponent()

        if len(self.chessboard.generateMoveList()) == 0:
            if self.chessboard.kingissafe() is False:
                self.status = "CHECKMATE!"
                self.draw_status()
                time.sleep(15)
                self.inPlay = False

            else:
                self.status = "STALEMATE!"
                self.draw_status()
                time.sleep(15)
                self.inPlay = False

        if self.chessboard.kingissafe() is False:
            self.status = "Check!"
            self.draw_status()

        if self.playerColor == "W":
            self.turn = "White's Turn"
            self.draw_turn()
        else:
            self.turn = "Black's Turn"
            self.draw_turn()

    def playGame(self):
        self.surface.fill((0, 0, 0))

        while (self.playerColor != "W" and self.playerColor != "B"):
            self.colorSelect()

        self.surface.fill((0, 0, 0))

        self.drawComponent()

        if self.playerColor == "W":
            self.computerColor = "B"
        else:
            self.computerColor = "W"

        if self.playerColor == "W":
            self.turn = "White's Turn"

        else:

            self.turn = "White's Turn"
            self.computerMoves()
            self.turn = "Black's Turn"

        while self.inPlay:
            self.eventHandler()
            self.draw_turn()
            self.draw_forfeit()

    def colorSelect(self):
        bx, by = self.DISPLAY_W / 3, self.DISPLAY_H / 2
        wx, wy = self.DISPLAY_W / 3, self.DISPLAY_H / 2
        b = pygame.draw.rect(self.surface, (255, 255, 255), [bx - 50, by - 50, 100, 100])
        bn_o = pygame.image.load("Assets/Chess_tile_nd.png")
        bn = pygame.transform.scale(bn_o, (75, 75))

        w = pygame.draw.rect(self.surface, (255, 255, 255), [bx + wx - 50, wy - 50, 100, 100])
        wn_o = pygame.image.load("Assets/Chess_tile_nl.png")
        wn = pygame.transform.scale(wn_o, (75, 75))

        self.surface.blit(self.surface, (0, 0))
        self.surface.blit(wn, (bx + wx - 40, wy - 40))
        self.surface.blit(bn, (bx - 40, by - 40))
        pygame.display.update()

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if w.collidepoint(pos):
                    self.playerColor = "W"
                    self.computerColor = "B"
                elif b.collidepoint(pos):
                    self.playerColor = "B"
                    self.computerColor = "W"

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.surface.blit(text_surface, text_rect)

    def promote_piece(self):
        self.draw_text("Promote your pawn", self.textSize, self.DISPLAY_W + 170, 18)
        q = pygame.image.load("Assets/Chess_tile_ql.png")
        r = pygame.image.load("Assets/Chess_tile_rl.png")
        b = pygame.image.load("Assets/Chess_tile_bl.png")
        n = pygame.image.load("Assets/Chess_tile_nl.png")
        q = pygame.transform.scale(q, (75, 75))
        r = pygame.transform.scale(r, (75, 75))
        b = pygame.transform.scale(b, (75, 75))
        n = pygame.transform.scale(n, (75, 75))

        self.surface.blit(q, (self.DISPLAY_W + 9, 34))
        self.surface.blit(r, (self.DISPLAY_W + 84, 34))
        self.surface.blit(b, (self.DISPLAY_W + 159, 34))
        self.surface.blit(n, (self.DISPLAY_W + 234, 34))
        pygame.display.update()

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if q.get_rect().collidepoint(pos):
                    return "Q"
                elif r.get_rect().collidepoint(pos):
                    return "R"
                elif b.get_rect().collidepoint(pos):
                    return "B"
                elif n.get_rect().collidepoint(pos):
                    return "K"

    def draw_turn(self):
        pygame.draw.rect(self.surface, (0, 0, 0), [self.DISPLAY_W + 25, self.DISPLAY_H / 2 - 25, 600, 50])
        self.draw_text(self.turn, self.textSize, self.DISPLAY_W + 270, self.DISPLAY_H / 2)
        pygame.display.update()

    def draw_status(self):
        pygame.draw.rect(self.surface, (0, 0, 0), [self.DISPLAY_W + 25, self.DISPLAY_H / 2 + 60, 600, 75])
        self.draw_text(self.status, self.textSize, self.DISPLAY_W + 270, self.DISPLAY_H / 2 + 80)
        pygame.display.update()

    def draw_forfeit(self):
        self.draw_text("Forfeit", self.textSize, self.DISPLAY_W + 270, self.DISPLAY_H / 2 + 160)
        pygame.display.update()
