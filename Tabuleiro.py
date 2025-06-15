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
        i = jogadaPlayer - 8
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

        if jogadaPlayer < 16:  # Se a posição for menos que 16, não há posições acima que possam ser invertidas
            return []

        i = jogadaPlayer - 8

        while self.initial_state[i] != symbolPlayer : #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePlays) > 0:
                    self.list_possible_play.append(True)
                    return possiblePlays
                else:
                    self.list_possible_play.append(False)
                    break
            possiblePlays.append(i)
            if jogadaPlayer < 8:
                break
            i = i - 8
        return []
    
    def CheckPossiblePlayToInvertVerticallyDown(self, jogadaPlayer, symbolPlayer):

        possiblePlays = []  

        if jogadaPlayer > 47:  # Se a posição for maior que 47, não há posições abaixo
            return []

        i = jogadaPlayer + 8

        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                if len(possiblePlays) > 0:
                    self.list_possible_play.append(True)
                    return possiblePlays
                else:
                    self.list_possible_play.append(False)
                    break
            possiblePlays.append(i)
            if jogadaPlayer > 55:
                break            
            i = i + 8
        return []

    def CheckPossiblePlayToInvertHorizontallyRight(self, jogadaPlayer, symbolPlayer):

        possiblePlays = []  

        if jogadaPlayer in {6, 7, 14, 15, 22, 23, 30, 31, 38, 39, 46, 47, 54, 55, 62, 63} : #não há posições para serem invertidas à direita
            return []

        i = jogadaPlayer + 1

        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                if len(possiblePlays) > 0:
                    self.list_possible_play.append(True)
                    return possiblePlays
                else:
                    self.list_possible_play.append(False)
                    break
            possiblePlays.append(i)
            if jogadaPlayer in {7, 15, 23,31,39,47,55,63} :
                break
            i = i + 1
        return []
    
    def CheckPossiblePlayToInvertHorizontallyLeft(self, jogadaPlayer, symbolPlayer):

        possiblePlays = []  

        if jogadaPlayer in {0, 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 56, 57} : #não há posições para esquerda
            return []

        i = jogadaPlayer - 1

        while self.initial_state[i] != symbolPlayer:
            if self.initial_state[i] == "_":
                if len(possiblePlays) > 0:
                    self.list_possible_play.append(True)
                    return possiblePlays
                else:
                    self.list_possible_play.append(False)
                    break
            possiblePlays.append(i)
            if jogadaPlayer in {0, 8, 16,24,32,40,48,56} :
                break
            i = i - 1
        return []

    def CheckPossiblePlayToInvertDiagonalLeftUp(self, jogadaPlayer, symbolPlayer):

        possiblePlays = []  

        if jogadaPlayer < 18 or jogadaPlayer in {24, 25, 32, 33, 40, 41, 48, 49, 56, 57}:
            return []

        i = jogadaPlayer - 9

        while self.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePlays) > 0:
                    self.list_possible_play.append(True)
                    return possiblePlays
                else:
                    self.list_possible_play.append(False)
                    break
            possiblePlays.append(i)
            if jogadaPlayer  in {0, 1, 2,3,4,5,6,7,8,16,24,32,40,48,56}:
                break
            i = i - 9
        return []
    
    def CheckPossiblePlayToInvertDiagonalLeftDown(self, jogadaPlayer, symbolPlayer):

        possiblePlays = []  

        if jogadaPlayer > 47 or jogadaPlayer in {0, 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41}:  
            return []

        i = jogadaPlayer + 9

        while self.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePlays) > 0:
                    self.list_possible_play.append(True)
                    return possiblePlays
                else:
                    self.list_possible_play.append(False)
                    break
            possiblePlays.append(i)
            if jogadaPlayer  in {7, 15, 23,31,39,47,55,63,56,57 ,58,59 ,60, 61 ,62, 63 }:
                break
            i = i + 9
        return []
    
    def CheckPossiblePlayToInvertDiagonalRightUp(self, jogadaPlayer, symbolPlayer):

        possiblePlays = []  

        if jogadaPlayer < 16 or jogadaPlayer in {22, 23, 30, 31, 38, 39, 46, 47, 54, 55, 62, 63}:  # Se a posição for menos que 8, não há posições acima
            return []

        i = jogadaPlayer - 7

        while self.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePlays) > 0:
                    self.list_possible_play.append(True)
                    return possiblePlays
                else:
                    self.list_possible_play.append(False)
                    break
            possiblePlays.append(i)
            if jogadaPlayer  in {0, 1, 2,3,4,5,6,7,15, 23,31,39,47,55,63 }:
                break
            i = i - 7
        return []

    def CheckPossiblePlayToInvertDiagonalRightDown(self, jogadaPlayer, symbolPlayer):

        possiblePlays = []  

        if jogadaPlayer > 45 or jogadaPlayer in {6, 7, 14, 15, 22, 23, 30, 31, 38, 39}:  # Se a posição for menos que 8, não há posições acima
            return []

        i = jogadaPlayer + 7

        while self.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
            if self.initial_state[i] == "_":
                if len(possiblePlays) > 0:
                    self.list_possible_play.append(True)
                    return possiblePlays
                else:
                    self.list_possible_play.append(False)
                    break
            possiblePlays.append(i)
            if jogadaPlayer  in {7,15,23,31,39,47,55,56,57, 58, 59 ,60, 61 ,62, 63}:
                break
            i = i + 7
        return [] 


    def generateASuccessor():
        return