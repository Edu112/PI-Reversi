import numpy as np 

class Tabuleiro:

    def __init__(self):
        self.initial_state = np.array([
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "x" , "o" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "o" , "x" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
        ])
        self.list_possible_play = []
        self.jogadas_validas_tabuleiro = None

    def ShowBoard(self):
        print(self.initial_state.reshape(8, 8))

    def PossiblePositionToInvertVerticallyUp(self, jogadaPlayer, symbolPlayer):
        possiblePositionToInvert = []
        i = jogadaPlayer - 8
        if jogadaPlayer is None:
            return []
        while i >= 0:
            if self.initial_state[i] == "_":
                return []
            if self.initial_state[i] == symbolPlayer:
                return possiblePositionToInvert if possiblePositionToInvert else []
            possiblePositionToInvert.append(i)
            i -= 8
        return []


    def PossiblePositionToInvertVerticallyDown(self, jogadaPlayer, symbolPlayer):
        possiblePositionToInvert = []
        i = jogadaPlayer + 8
        if jogadaPlayer is None:
            return []
        while i <= 63:
            if self.initial_state[i] == "_":
                return []
            if self.initial_state[i] == symbolPlayer:
                return possiblePositionToInvert if possiblePositionToInvert else []
            possiblePositionToInvert.append(i)
            i += 8
        return []


    def PossiblePositionToInvertHorizontallyRight(self, jogadaPlayer, symbolPlayer):
        possiblePositionToInvert = []
        row = jogadaPlayer // 8
        i = jogadaPlayer + 1
        if jogadaPlayer is None:
            return []
        while i % 8 != 0:
            if self.initial_state[i] == "_":
                return []
            if self.initial_state[i] == symbolPlayer:
                return possiblePositionToInvert if possiblePositionToInvert else []
            possiblePositionToInvert.append(i)
            i += 1
        return []


    def PossiblePositionToInvertHorizontallyLeft(self, jogadaPlayer, symbolPlayer):
        possiblePositionToInvert = []
        i = jogadaPlayer - 1
        if jogadaPlayer is None:
            return []
        while i >= 0 and i // 8 == jogadaPlayer // 8:
            if self.initial_state[i] == "_":
                return []
            if self.initial_state[i] == symbolPlayer:
                return possiblePositionToInvert if possiblePositionToInvert else []
            possiblePositionToInvert.append(i)
            i -= 1
        return []

    def PossiblePositionToInvertDiagonalLeftUp(self, jogadaPlayer, symbolPlayer):
        possiblePositionToInvert = []
        i = jogadaPlayer - 9
        if jogadaPlayer is None:
            return []
        while i >= 0 and (i % 8) < (jogadaPlayer % 8):
            if self.initial_state[i] == "_":
                return []
            if self.initial_state[i] == symbolPlayer:
                return possiblePositionToInvert if possiblePositionToInvert else []
            possiblePositionToInvert.append(i)
            i -= 9
        return []

    def PossiblePositionToInvertDiagonalRightDown(self, jogadaPlayer, symbolPlayer):
        possiblePositionToInvert = []
        i = jogadaPlayer + 9
        if jogadaPlayer is None:
            return []
        while i <= 63 and (i % 8) > (jogadaPlayer % 8):
            if self.initial_state[i] == "_":
                return []
            if self.initial_state[i] == symbolPlayer:
                return possiblePositionToInvert if possiblePositionToInvert else []
            possiblePositionToInvert.append(i)
            i += 9
        return []


    def PossiblePositionToInvertDiagonalLeftDown(self, jogadaPlayer, symbolPlayer):
        possiblePositionToInvert = []  
        i = jogadaPlayer + 7
        if jogadaPlayer is None:
            return []
        while i <= 63 and (i % 8) < (jogadaPlayer % 8):
            if self.initial_state[i] == "_":
                return []
            if self.initial_state[i] == symbolPlayer:
                return possiblePositionToInvert if possiblePositionToInvert else []
            possiblePositionToInvert.append(i)
            i += 7
        return []


    def PossiblePositionToInvertDiagonalRightUp(self, jogadaPlayer, symbolPlayer):
        possiblePositionToInvert = []
        i = jogadaPlayer - 7
        if jogadaPlayer is None:
            return []
        while i >= 0 and (i % 8) > (jogadaPlayer % 8):
            if self.initial_state[i] == "_":
                return []
            if self.initial_state[i] == symbolPlayer:
                return possiblePositionToInvert if possiblePositionToInvert else []
            possiblePositionToInvert.append(i)
            i -= 7
        return []



#checar jogadas possiveis
    def CheckPossiblePlayToInvertVerticallyUp(self, jogadaPlayer, symbolPlayer):
        possiblePlays = []
        if jogadaPlayer < 16:
            self.list_possible_play.append(False)
            return []

        i = jogadaPlayer - 8
        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                self.list_possible_play.append(False)
                return []
            possiblePlays.append(i)
            if i < 8:
                self.list_possible_play.append(False)
                return []
            i -= 8

        if possiblePlays:
            self.list_possible_play.append(True)
            return possiblePlays
        else:
            self.list_possible_play.append(False)
            return []


    def CheckPossiblePlayToInvertVerticallyDown(self, jogadaPlayer, symbolPlayer):
        possiblePlays = []
        if jogadaPlayer > 47:
            self.list_possible_play.append(False)
            return []

        i = jogadaPlayer + 8
        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                self.list_possible_play.append(False)
                return []
            possiblePlays.append(i)
            if i > 55:
                self.list_possible_play.append(False)
                return []
            i += 8

        if possiblePlays:
            self.list_possible_play.append(True)
            return possiblePlays
        else:
            self.list_possible_play.append(False)
            return []

    def CheckPossiblePlayToInvertHorizontallyRight(self, jogadaPlayer, symbolPlayer):
        possiblePlays = []
        if jogadaPlayer % 8 >= 6:
            self.list_possible_play.append(False)
            return []

        i = jogadaPlayer + 1
        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                self.list_possible_play.append(False)
                return []
            possiblePlays.append(i)
            if i % 8 == 7:
                self.list_possible_play.append(False)
                return []
            i += 1

        if possiblePlays:
            self.list_possible_play.append(True)
            return possiblePlays
        else:
            self.list_possible_play.append(False)
            return []

    def CheckPossiblePlayToInvertHorizontallyLeft(self, jogadaPlayer, symbolPlayer):
        possiblePlays = []
        if jogadaPlayer % 8 <= 1:
            self.list_possible_play.append(False)
            return []

        i = jogadaPlayer - 1
        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                self.list_possible_play.append(False)
                return []
            possiblePlays.append(i)
            if i % 8 == 0:
                self.list_possible_play.append(False)
                return []
            i -= 1

        if possiblePlays:
            self.list_possible_play.append(True)
            return possiblePlays
        else:
            self.list_possible_play.append(False)
            return []

    def CheckPossiblePlayToInvertDiagonalLeftUp(self, jogadaPlayer, symbolPlayer):
        possiblePlays = []
        if jogadaPlayer < 9 or jogadaPlayer % 8 <= 0:
            self.list_possible_play.append(False)
            return []

        i = jogadaPlayer - 9
        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                self.list_possible_play.append(False)
                return []
            possiblePlays.append(i)
            if i < 9 or i % 8 == 0:
                self.list_possible_play.append(False)
                return []
            i -= 9

        if possiblePlays:
            self.list_possible_play.append(True)
            return possiblePlays
        else:
            self.list_possible_play.append(False)
            return []

    def CheckPossiblePlayToInvertDiagonalLeftDown(self, jogadaPlayer, symbolPlayer):
        possiblePlays = []
        if jogadaPlayer > 54 or jogadaPlayer % 8 <= 0:
            self.list_possible_play.append(False)
            return []

        i = jogadaPlayer + 9
        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                self.list_possible_play.append(False)
                return []
            possiblePlays.append(i)
            if i > 54 or i % 8 == 0:
                self.list_possible_play.append(False)
                return []
            i += 9

        if possiblePlays:
            self.list_possible_play.append(True)
            return possiblePlays
        else:
            self.list_possible_play.append(False)
            return []

    def CheckPossiblePlayToInvertDiagonalRightUp(self, jogadaPlayer, symbolPlayer):
        possiblePlays = []
        if jogadaPlayer < 7 or jogadaPlayer % 8 >= 7:
            self.list_possible_play.append(False)
            return []

        i = jogadaPlayer - 7
        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                self.list_possible_play.append(False)
                return []
            possiblePlays.append(i)
            if i < 7 or i % 8 == 7:
                self.list_possible_play.append(False)
                return []
            i -= 7

        if possiblePlays:
            self.list_possible_play.append(True)
            return possiblePlays
        else:
            self.list_possible_play.append(False)
            return []

    def CheckPossiblePlayToInvertDiagonalRightDown(self, jogadaPlayer, symbolPlayer):
        possiblePlays = []
        if jogadaPlayer > 55 or jogadaPlayer % 8 >= 7:
            self.list_possible_play.append(False)
            return []

        i = jogadaPlayer + 7
        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                self.list_possible_play.append(False)
                return []
            possiblePlays.append(i)
            if i > 55 or i % 8 == 7:
                self.list_possible_play.append(False)
                return []
            i += 7

        if possiblePlays:
            self.list_possible_play.append(True)
            return possiblePlays
        else:
            self.list_possible_play.append(False)
            return []




    def generateASuccessor():
        return