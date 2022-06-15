from peices import *


class Ratings:

    def __init__(self, Board):
        self.rating = 0
        self.material = 0
        self.chessboard = Board

    def evaluateRating(self, moveCount, depth):

        self.material = self.rateMaterial()
        self.rating += self.material
        self.rating += self.rateAttack()
        self.rating += self.rateMoveability(moveCount, depth, self.material)

        self.chessboard.changePerspective()

        self.material = self.rateMaterial()
        self.rating -= self.material

        self.rating -= self.rateAttack()
        self.rating -= self.rateMoveability(moveCount, depth, self.material)

        self.chessboard.changePerspective()

        return -(self.rating + depth * 60)

    def rateMaterial(self):
        materialRating = 0
        bishopCounter = 0

        for index in range(self.chessboard.TOTALPIECES):
            CaseTest = self.chessboard.boardArray[index // 8][index % 8]

            if CaseTest == "P":
                materialRating += 100

            elif CaseTest == "R":
                materialRating += 600

            elif CaseTest == "K":
                materialRating += 400

            elif CaseTest == "B":
                bishopCounter += 1

            elif CaseTest == "Q":
                materialRating += 1200

        if bishopCounter >= 2:
            materialRating += 200 * bishopCounter

        elif bishopCounter == 1:
            materialRating += 150

        return materialRating

    def rateAttack(self):
        attackRating = 0

        temporyKingPosition = self.chessboard.kingPosition_White

        for i in range(self.chessboard.TOTALPIECES):
            CaseTest = self.chessboard.boardArray[i // 8][i % 8]

            if CaseTest == "P":
                self.kingPosition_White = i

                if self.chessboard.kingissafe() is False:
                    attackRating -= 30

            elif CaseTest == "R":
                self.kingPosition_White = i

                if self.chessboard.kingissafe() is False:
                    attackRating -= 250

            elif CaseTest == "K":
                self.kingPosition_White = i

                if self.chessboard.kingissafe() is False:
                    attackRating -= 150

            elif CaseTest == "B":
                self.kingPosition_White = i

                if self.chessboard.kingissafe() is False:
                    attackRating -= 150

            elif CaseTest == "Q":
                self.kingPosition_White = i

                if self.chessboard.kingissafe() is False:
                    attackRating -= 450

        self.chessboard.kingPosition_White = temporyKingPosition

        if (self.chessboard.kingissafe() is False):
            attackRating -= 500
        return attackRating

    def rateMoveability(self, moveCount, depth, material):
        moveabilityRating = moveCount

        if moveCount == 0:

            if self.chessboard.kingissafe() is False:
                moveabilityRating += -(150000 * depth)


            else:
                moveabilityRating += -(100000 * depth)

        return moveabilityRating
