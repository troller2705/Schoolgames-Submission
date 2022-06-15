import pygame
from peices import *
from ratings import Ratings
import time

class UserInterface:
    def __init__(self, surface, Board):
        self.font_name = 'UI/8-Bit.ttf'
        self.click = pygame.mixer.Sound('Music&Sounds/Sounds/Bomb_Drop.wav')
        self.surface = surface  # Holds the surface variable defined for pygame
        self.inPlay = True  # Inplay variable to check if we are still playing the game
        self.squareSize = 75 # Size of square; used as a scale for peices and board squares (Re adjust this variable if you want to change size of game)
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


        # mouseInitial Stores the inital X and y coordinates user makes when clicking mouse on board
        self.mouseInitialX = 0
        self.mouseInitialY = 0

        # mouseFinal Stores the finale X and y coordinates user makes when releasing mouse on board
        self.mouseFinalX = 0
        self.mouseFinalY = 0

        self.chessboard = Board  # Initialize given board onto interface
        self.playerMove = ""  # stores players move they make
        self.computerMove = "" # Stores computers move they make
        self.playerColor = "" # Color of player
        self.computerColor = "" # Color of computer
        self.status = "" # Status of game
        self.turn = "" # Current turn




    def drawComponent(self):
        # Creates visual representation of board by Making Checkered square pattern
        for i in range(0, self.peices, 2):
            pygame.draw.rect(self.surface, (120, 60, 30), [(i % 8+(i//8) % 2)*self.squareSize, (i//8)*self.squareSize, self.squareSize, self.squareSize])  # Draws brown squares
            pygame.draw.rect(self.surface, (245, 245, 220), [((i+1) % 8-((i+1)//8) % 2)*self.squareSize, ((i+1)//8)*self.squareSize, self.squareSize, self.squareSize])  # Draws beige squares
        #  Loop through every peice
        for index in range(self.peices):
            currentPosition = self.chessboard.boardArray[index//8][index % 8]  # looking at current peice in board
            # If we are looking at a white pawn
            if currentPosition == "P":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_pl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_pd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black pawn
            elif currentPosition == "p":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_pd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_pl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white knight
            elif currentPosition == "K":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_nl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_nd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black knight
            elif currentPosition == "k":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_nd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_nl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white bishop
            elif currentPosition == "B":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_bl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_bd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black bishop
            elif currentPosition == "b":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_bd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_bl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white rook
            elif currentPosition == "R":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_rl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_rd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black rook
            elif currentPosition == "r":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_rd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_rl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white queen
            elif currentPosition == "Q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_ql.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_qd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black queen
            elif currentPosition == "q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_qd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_ql.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white king
            elif currentPosition == "A":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_kl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto boardArray
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_kd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
            # If we are looking at a black king
            elif currentPosition == "a":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("Assets/Chess_tile_kd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("Assets/Chess_tile_kl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto boardArray

        pygame.display.update()  # Update the display board when complete


    def eventHandler(self):
        # Read pygame events
        for event in pygame.event.get():
            # If user hits exit
            if event.type == pygame.QUIT:
                self.inPlay = False  # Set exit variable to false and exit loop
                break

            # If we press the mouse down
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(self.click)  # Play click sound
                # If we are currently inside the board
                if pygame.mouse.get_pos()[0] < 8*self.squareSize and pygame.mouse.get_pos()[1] < 8*self.squareSize:
                    self.mouseInitialX = pygame.mouse.get_pos()[0]  # Store clicked x position to mouseInitialX
                    self.mouseInitialY = pygame.mouse.get_pos()[1]  # Store clicked y position to mouseInitialY

            # If we release the mouse
            if event.type == pygame.MOUSEBUTTONUP:
                # If we are currently inside the board
                if pygame.mouse.get_pos()[0] < 8*self.squareSize and pygame.mouse.get_pos()[1] < 8*self.squareSize:
                    self.mouseFinalX = pygame.mouse.get_pos()[0]  # Store released x position to mouseFinalX
                    self.mouseFinalY = pygame.mouse.get_pos()[1]  # Store released y position to mouseFinalY
                    self.computeMove()  # Compute the move player has made

    def computeMove(self):
        # We now have to translate the coordinates in a way the board will understand
        # If we have a pawn promotion
        rowInitial = self.mouseInitialY//self.squareSize
        columnInitial = self.mouseInitialX//self.squareSize
        rowFinal = self.mouseFinalY//self.squareSize
        columnFinal = self.mouseFinalX//self.squareSize

        # IF player is performing a promotion move
        if rowFinal == 0 and rowInitial == 1 and self.chessboard.boardArray[rowInitial][columnInitial] == "P":
            # Allow player to choose which peice to promote
            promotionPeice = self.promote_piece()
            # Send move to promote peice
            self.playerMove += str(columnInitial) + str(columnFinal) + str(self.chessboard.boardArray[rowFinal][columnFinal])+ promotionPeice + "P"

        # IF player is performing a castling move
        elif rowFinal == 7 and (columnInitial == 0 or columnInitial == 7) and self.chessboard.boardArray[rowInitial][columnInitial] == "R" and self.chessboard.boardArray[rowFinal][columnFinal] == "A":
            # Set current move as the current move player has made

            if columnInitial == 0:
                self.playerMove += str(columnInitial) + str(columnFinal-1) + str(columnFinal) + "R" + "C"
            elif columnInitial == 7:
                self.playerMove += str(columnInitial) + str(columnFinal+1) + str(columnFinal) + "R" + "C"

        # Otherwise we have a regular Move
        else:
            # Set current move as the current move player has made
            self.playerMove += str(rowInitial) + str(columnInitial) + str(rowFinal) + str(columnFinal) + str(self.chessboard.boardArray[rowFinal][(columnFinal)])

        # If the move we make is a valid move
        if self.playerMove in self.chessboard.generateMoveList():
            self.chessboard.computeMove(self.playerMove)  # Make the move on the board
            self.drawComponent()  # Visually update board
            if self.chessboard.kingissafe() is not False:
                self.status = ""
                self.draw_status()
            # It's now the computer's turn to make a move. Call computerMoves
            self.computerMoves()
        # Set current move back to empty to generate next move
        self.playerMove = ""
        self.computerMove = ""

    def computerMoves(self):
        '''
        Function for computer to conduct it's move using the alphaBeta function
        '''
        # Display that it is the computers turn
        if self.computerColor == "W":
            self.turn = "White's Turn"
            self.draw_turn()
        else:
            self.turn = "Black's Turn"
            self.draw_turn()

        self.chessboard.changePerspective()  # change to the computer's perspective
        self.computerMove = self.chessboard.alphaBeta(self.chessboard.MAXDEPTH, float("inf"), -float("inf"), "", 0)
        # If computer cannot make a move
        # Player wins
        if self.computerMove is None:
            self.status = "CHECKMATE!"
            self.draw_status()
            time.sleep(15)
            self.inPlay = False
        # Otherwise compute move
        else:
            self.chessboard.computeMove(self.computerMove)  # Allow computer to make move using alphaBeta

        self.chessboard.changePerspective()  # Change back to the player's persepctive
        self.drawComponent()  # Visually update board

        # If we have hit a checkmate or a stalemate
        # If checkmate
        if len(self.chessboard.generateMoveList()) == 0:
            if self.chessboard.kingissafe() is False:
                self.status = "CHECKMATE!"
                self.draw_status()
                time.sleep(15)  # 15 Second delay (usually to verify if checkmate is legitimate)
                self.inPlay = False
            # Otherwise if stalemate
            else:
                self.status = "STALEMATE!"
                self.draw_status()
                time.sleep(15)  # 15 Second delay (usually to verify if checkmate is legitimate)
                self.inPlay = False

        # Print check message if player is in check
        if self.chessboard.kingissafe() is False:
            self.status = "Check!"
            self.draw_status()

        # Display that it is the players turn
        if self.playerColor == "W":
            self.turn = "White's Turn"
            self.draw_turn()
        else:
            self.turn = "Black's Turn"
            self.draw_turn()

    def playGame(self):
        self.surface.fill((0, 0, 0))  # initially Fill screen with black
        # Prompt user to select what colour they want to play as
        while(self.playerColor != "W" and self.playerColor != "B"):
            self.colorSelect()

        self.surface.fill((0, 0, 0))  # Fill screen with black

        self.drawComponent()  # Call drawComponent to initially draw the board
        self.draw_forfeit()

        # Set computerColor based on color user selects
        if self.playerColor == "W":
            self.computerColor = "B"
        else:
            self.computerColor = "W"

        # If player is white, prompt player to go first
        if self.playerColor == "W":
            self.turn = "White's Turn"

        else:
            # Otherwise it is computers turn
            self.turn = "White's Turn"
            self.computerMoves() # Computer makes first move
            self.turn = "Black's Turn"
        # Call the event handler until user chooses to exit game
        while self.inPlay:
            self.eventHandler()  # Call eventHandler for players input
            self.draw_turn()



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
        pygame.draw.rect(self.surface, (0, 0, 0), [self.DISPLAY_W + 25, self.DISPLAY_H / 2 + 60, 600, 100])
        self.draw_text(self.status, self.textSize, self.DISPLAY_W + 270, self.DISPLAY_H / 2 + 80)
        pygame.display.update()

    def draw_forfeit(self):
        self.draw_text("Forfeit?", self.textSize, self.DISPLAY_W + 270, self.DISPLAY_H / 2 + 160)
        pygame.display.update()