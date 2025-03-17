from Tabuleiro import Tabuleiro
from Validador import Validador 
from Jogador import Jogador



tabuleiro = Tabuleiro()
validador = Validador(True)
jogador1 = Jogador("Eduardo", "x", [27,36])
jogador2 = Jogador("Andre", "o", [28,35])
jogadores = [jogador1,jogador2]
endGame = False
winner = ""
rounds = 0


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

    if symbolPlayer == "x":
        jogador1.pieces.append(jogadaPlayer)
        jogador1.pieces = jogador1.pieces + positionToInvert
        jogador2.pieces = list(set(jogador2.pieces) - set(positionToInvert))    
    else :
        jogador2.pieces.append(jogadaPlayer)
        jogador2.pieces = jogador2.pieces + positionToInvert
        jogador1.pieces = list(set(jogador1.pieces) - set(positionToInvert)) 
       
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




def CheckPlay(Jogador, jogada):  # verifica uma jogada possivel
    aux = PositionToInvert(jogada,Jogador.symbol)
    if len(aux) != 0:
        validador.validMove = True
        return 
    validador.validMove = False
    return 




def CheckPlays(Jogador,pieces):  #verifica a jogadas possiveis 
    for i in range(0, len(pieces), 1):
        aux = PositionToInvert(pieces[i],Jogador.symbol) 
        if len(aux) != 0:                #checa se a lista de movimentos possiveis esta vazia
            return True
    return False


def WhoWinner(amountP1,amountP2):   # Descobre o ganhador 
    if amountP1 > amountP2 :
        winner = "jogador1"
    elif amountP2 > amountP1 :
        winner = "jogador2"
    else:
        winner = "empate"
    return    




def ChangeEndGame():
    global endGame
    global winner
    totalPieces = jogador1.pieces + jogador2.pieces
    amountPiecesJogador1 = len(jogador1.pieces)
    amountPiecesJogador2 = len(jogador2.pieces)
    if len(totalPieces) == 64:
        endGame = True
        WhoWinner(amountPiecesJogador1,amountPiecesJogador2)
        return

    if (amountPiecesJogador2 == 0):
        endGame = True
        winner = "jogador1"
        return
    elif(amountPiecesJogador1 == 0):
        endGame = True 
        winner == "jogador2"
        return
    
    checkNoPlaysJogador1 = CheckPlays(jogador1,jogador1.pieces)
    checkNoPlaysJogador2 = CheckPlays(jogador2,jogador2.pieces)

    if checkNoPlaysJogador1 and checkNoPlaysJogador2:
        endGame = True
        WhoWinner(amountPiecesJogador1,amountPiecesJogador2)
        return
    return 
    


def PlayGame(Jogador):
    global rounds
    jogadaPlayer = Jogador.UserInput()  
    PossibleMove = validador.PossibleMove(tabuleiro, jogadaPlayer) 
    CheckPlay(Jogador,jogadaPlayer)
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
        rounds += 1
    else:
        print("Jogada inválida. Jogue novamente\n")
        
    tabuleiro.ShowBoard()




def GameLoop(jogadores):
    
    while not endGame:  
        roundOfPlayer = jogadores[rounds % 2]     
        PlayGame(roundOfPlayer)
        ChangeEndGame()


    return



GameLoop(jogadores)
if winner != "empate":
    print("Vitória: " +winner+" venceu")
else:
    print(winner)
