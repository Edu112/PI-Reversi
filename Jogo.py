from Tabuleiro import Tabuleiro
from Validador import Validador 
from Jogador import Jogador

tabuleiro = Tabuleiro()
validador = Validador(True)
jogador1 = Jogador("Eduardo", "x")
jogador2 = Jogador("Andre", "o")
fimDoJogo = False

tabuleiro.ShowBoard()

def PositionToInvert(jogadaPlayer, symbolPlayer):
    positionToInvert = []
    invertVerticallDown = PossiblePositionToInvertVerticallyDown(jogadaPlayer,symbolPlayer) 
    invertVerticallUp = PossiblePositionToInvertVerticallyUp(jogadaPlayer,symbolPlayer)
    invertHorizontallyRight = PossiblePositionToInvertHorizontallyRight(jogadaPlayer,symbolPlayer)
    invertHorizontallyLeft = PossiblePositionToInvertHorizontallyLeft(jogadaPlayer,symbolPlayer)
    invertDiagonalLeftUp = PossiblePositionToInvertDiagonalLeftUp(jogadaPlayer,symbolPlayer)
    invertDiagonalLeftDown = PossiblePositionToInvertDiagonalLeftDown(jogadaPlayer,symbolPlayer)
    invertDiagonalRightUp = PossiblePositionToInvertDiagonalRightUp(jogadaPlayer,symbolPlayer)    
    invertDiagonalRightDown = PossiblePositionToInvertDiagonalRightDown(jogadaPlayer,symbolPlayer) 

    positionToInvert = invertVerticallDown + invertVerticallUp + invertHorizontallyRight +  invertHorizontallyLeft + invertDiagonalLeftUp + invertDiagonalLeftDown + invertDiagonalRightUp + invertDiagonalRightDown

    return positionToInvert  


def PossiblePositionToInvertVerticallyUp(jogadaPlayer, symbolPlayer):

    possiblePositionToInvert = []  

    if jogadaPlayer < 8:  # Se a posição for menos que 8, não há posições acima
        return []


    i = jogadaPlayer - 8

    while tabuleiro.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
        if tabuleiro.initial_state[i] == "_":
            return []
        possiblePositionToInvert.append(i)
        i = i - 8
    return possiblePositionToInvert

def PossiblePositionToInvertVerticallyDown(jogadaPlayer, symbolPlayer):

    possiblePositionToInvert = []  

    if jogadaPlayer > 55:  # Se a posição for maior que 55, não há posições acima
        return []


    i = jogadaPlayer + 8

    while tabuleiro.initial_state[i] != symbolPlayer:
        if tabuleiro.initial_state[i] == "_":
            return []
        possiblePositionToInvert.append(i)
        i = i + 8
    return possiblePositionToInvert

def PossiblePositionToInvertHorizontallyRight(jogadaPlayer, symbolPlayer):

    possiblePositionToInvert = []  

    if jogadaPlayer in {7, 15, 23,31,39,47,55,63} : #não há posições para direita
        return []


    i = jogadaPlayer + 1

    while tabuleiro.initial_state[i] != symbolPlayer:
        if tabuleiro.initial_state[i] == "_":
            return []
        possiblePositionToInvert.append(i)
        i = i + 1
    return possiblePositionToInvert

def PossiblePositionToInvertHorizontallyLeft(jogadaPlayer, symbolPlayer):

    possiblePositionToInvert = []  

    if jogadaPlayer in {0, 8, 16,24,32,40,48,56} : #não há posições para direita
        return []


    i = jogadaPlayer - 1

    while tabuleiro.initial_state[i] != symbolPlayer:
        if tabuleiro.initial_state[i] == "_":
            return []
        possiblePositionToInvert.append(i)
        i = i - 1
    return possiblePositionToInvert

def PossiblePositionToInvertDiagonalLeftUp(jogadaPlayer, symbolPlayer):

    possiblePositionToInvert = []  

    if jogadaPlayer  in {0, 1, 2,3,4,5,6,7,8,16,24,32,40,48,56}:  # Se a posição for menos que 8, não há posições acima
        return []


    i = jogadaPlayer - 9

    while tabuleiro.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
        if tabuleiro.initial_state[i] == "_":
            return []
        possiblePositionToInvert.append(i)
        i = i - 9
    return possiblePositionToInvert


def PossiblePositionToInvertDiagonalLeftDown(jogadaPlayer, symbolPlayer):

    possiblePositionToInvert = []  

    if jogadaPlayer  in {7, 15, 23,31,39,47,55,63,56,57 ,58,59 ,60, 61 ,62, 63 }:  # Se a posição for menos que 8, não há posições acima
        return []


    i = jogadaPlayer + 9

    while tabuleiro.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
        if tabuleiro.initial_state[i] == "_":
            return []
        possiblePositionToInvert.append(i)
        i = i + 9
    return possiblePositionToInvert

def PossiblePositionToInvertDiagonalRightUp(jogadaPlayer, symbolPlayer):

    possiblePositionToInvert = []  

    if jogadaPlayer  in {0, 1, 2,3,4,5,6,7,15, 23,31,39,47,55,63 }:  # Se a posição for menos que 8, não há posições acima
        return []


    i = jogadaPlayer - 7

    while tabuleiro.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
        if tabuleiro.initial_state[i] == "_":
            return []
        possiblePositionToInvert.append(i)
        i = i - 7
    return possiblePositionToInvert


def PossiblePositionToInvertDiagonalRightDown(jogadaPlayer, symbolPlayer):

    possiblePositionToInvert = []  

    if jogadaPlayer  in {7,15, 23,31,39,47,55,56,57 ,58,59 ,60, 61 ,62, 63}:  # Se a posição for menos que 8, não há posições acima
        return []


    i = jogadaPlayer + 7

    while tabuleiro.initial_state[i] != symbolPlayer:     #loop para cima até encontrar o simbolo do player
        if tabuleiro.initial_state[i] == "_":
            return []
        possiblePositionToInvert.append(i)
        i = i + 7
    return possiblePositionToInvert





def PlayGame(Jogador):
    jogadaPlayer = Jogador.UserInput()  
    PossibleMove = validador.PossibleMove(tabuleiro, jogadaPlayer) 
    PossibleInvert = validador.validMove

    if PossibleMove and PossibleInvert: 
        print("Jogada válida\n")

        ppti = PositionToInvert(jogadaPlayer, Jogador.symbol) 
        if ppti != []:  # Se houver posições válidas para inverter
            tabuleiro.initial_state[jogadaPlayer] = Jogador.symbol  # Coloca a peça do jogador no tabuleiro

            # Chama a função para inverter as peças que estão nas posições do array ppti_up
            for i in ppti:
                tabuleiro.initial_state[i] = Jogador.symbol  

        print(ppti)  # Indice das posições trocadas
        print("\n")
    else:
        print("Jogada inválida.\n")

    tabuleiro.ShowBoard()  # Exibe o estado do tabuleiro


PlayGame(jogador1)
PlayGame(jogador2)
PlayGame(jogador1)
