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

    def ShowBoard(self):
        print(self.initial_state.reshape(8, 8))

    def PossiblePositionToInvertVerticallyUp(self, jogadaPlayer, symbolPlayer):
        
        possiblePositionToInvert = []  

        if jogadaPlayer < 16:  # Se a posição for menos que 16, não há posições acima que possam ser invertidas
            return []

        i = jogadaPlayer - 8

        while self.initial_state[i] != symbolPlayer: #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePositionToInvert) > 0:
                    self.list_possible_play.append(True) 
                else:
                    self.list_possible_play.append(False)
                return []
            possiblePositionToInvert.append(i)
            i = i - 8
        return possiblePositionToInvert 

    def PossiblePositionToInvertVerticallyDown(self, jogadaPlayer, symbolPlayer):

        possiblePositionToInvert = []  

        if jogadaPlayer > 47:  # Se a posição for maior que 47, não há posições abaixo
            return []

        i = jogadaPlayer + 8

        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                if len(possiblePositionToInvert) > 0:
                    self.list_possible_play.append(True) 
                else:
                    self.list_possible_play.append(False)
                return []
            possiblePositionToInvert.append(i)
            i = i + 8
        return possiblePositionToInvert

    def PossiblePositionToInvertHorizontallyRight(self, jogadaPlayer, symbolPlayer):

        possiblePositionToInvert = []  

        if jogadaPlayer in {6, 7, 14, 15, 22, 23, 30, 31, 38, 39, 46, 47, 54, 55, 62, 63} : #não há posições para serem invertidas à direita
            return []

        i = jogadaPlayer + 1

        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                if len(possiblePositionToInvert) > 0:
                    self.list_possible_play.append(True) 
                else:
                    self.list_possible_play.append(False)
                return []
            possiblePositionToInvert.append(i)
            i = i + 1
        return possiblePositionToInvert

    def PossiblePositionToInvertHorizontallyLeft(self, jogadaPlayer, symbolPlayer):

        possiblePositionToInvert = []  

        if jogadaPlayer in {0, 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 56, 57} : #não há posições para esquerda
            return []

        i = jogadaPlayer - 1

        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                if len(possiblePositionToInvert) > 0:
                    self.list_possible_play.append(True) 
                else:
                    self.list_possible_play.append(False)
                return []
            possiblePositionToInvert.append(i)
            i = i - 1
        return possiblePositionToInvert

    def PossiblePositionToInvertDiagonalLeftUp(self, jogadaPlayer, symbolPlayer):

        possiblePositionToInvert = []  

        if jogadaPlayer < 18 or jogadaPlayer in {24, 25, 32, 33, 40, 41, 48, 49, 56, 57}:
            return []

        i = jogadaPlayer - 9

        while self.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePositionToInvert) > 0:
                    self.list_possible_play.append(True) 
                else:
                    self.list_possible_play.append(False)
                return []
            possiblePositionToInvert.append(i)
            i = i - 9
        return possiblePositionToInvert

    def PossiblePositionToInvertDiagonalLeftDown(self, jogadaPlayer, symbolPlayer):

        possiblePositionToInvert = []  

        if jogadaPlayer > 47 or jogadaPlayer in {0, 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41}:  
            return []

        i = jogadaPlayer + 9

        while self.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePositionToInvert) > 0:
                    self.list_possible_play.append(True) 
                else:
                    self.list_possible_play.append(False)
                return []
            possiblePositionToInvert.append(i)
            i = i + 9
        return possiblePositionToInvert

    def PossiblePositionToInvertDiagonalRightUp(self, jogadaPlayer, symbolPlayer):

        possiblePositionToInvert = []  

        if jogadaPlayer < 16 or jogadaPlayer in {22, 23, 30, 31, 38, 39, 46, 47, 54, 55, 62, 63}:  # Se a posição for menos que 8, não há posições acima
            return []

        i = jogadaPlayer - 7

        while self.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePositionToInvert) > 0:
                    self.list_possible_play.append(True) 
                else:
                    self.list_possible_play.append(False)
                return []
            possiblePositionToInvert.append(i)
            i = i - 7
        return possiblePositionToInvert

    def PossiblePositionToInvertDiagonalRightDown(self, jogadaPlayer, symbolPlayer):

        possiblePositionToInvert = []  

        if jogadaPlayer > 45 or jogadaPlayer in {6, 7, 14, 15, 22, 23, 30, 31, 38, 39}:  # Se a posição for menos que 8, não há posições acima
            return []

        i = jogadaPlayer + 7

        while self.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePositionToInvert) > 0:
                    self.list_possible_play.append(True) 
                else:
                    self.list_possible_play.append(False)
                return []
            possiblePositionToInvert.append(i)
            i = i + 7
        return possiblePositionToInvert 


    def generateASuccessor():
        return

    