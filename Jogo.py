from Tabuleiro import Tabuleiro
from Validador import Validador 
from Jogador import Jogador

tabuleiro = Tabuleiro()
validador = Validador()
jogador1 = Jogador("Eduardo", "x")
jogador2 = Jogador("Andre", "o")
fimDoJogo = False

tabuleiro.ShowBoard()

def PositionToInvert(possiblePositionToInvert, symbolPlayer, oppositeSymbol):

    positionToInvert = []  

    lessIndex = len(possiblePositionToInvert) - 1  
    for i in range(lessIndex, -1, -1):
        ppti = possiblePositionToInvert[i]  #ppti: Abreviação de possiblePositionToInvert

        if tabuleiro.initial_state[ppti] == symbolPlayer:  
            for j in range(i - 1, -1, -1):  
                ppti = possiblePositionToInvert[j] # Abreviação de possiblePositionToInvert

                if tabuleiro.initial_state[ppti] != oppositeSymbol:  
                    return []
                positionToInvert.append(ppti)  # Adiciona as posições que podem ser invertidas

            return positionToInvert  # Retorna a lista de posições a serem invertidas
    return []  

def PossiblePositionToInvertVerticallyUp(jogadaPlayer, symbolPlayer):

    possiblePositionToInvert = []  

    if jogadaPlayer < 8:  # Se a posição for menos que 8, não há posições acima
        return []
    
    if symbolPlayer == "x":
        oppositeSymbol = "o"
    else:
        oppositeSymbol = "x"

    for i in range(jogadaPlayer - 8, -1, -8): # i começa sendo a posição acima da escolhida pelo jogador, enquanto i > -1, decrementamos de 8 em 8. 
        possiblePositionToInvert.append(i)

    return PositionToInvert(possiblePositionToInvert, symbolPlayer, oppositeSymbol)

def PlayGame(Jogador):
    jogadaPlayer = Jogador.UserInput()  
    jogadaValida = validador.ValidMove(tabuleiro, jogadaPlayer) 

    if jogadaValida:
        print("Jogada válida\n")

        ppti = PossiblePositionToInvertVerticallyUp(jogadaPlayer, Jogador.symbol) 
        if ppti != []:  # Se houver posições válidas para inverter
            tabuleiro.initial_state[jogadaPlayer] = Jogador.symbol  # Coloca a peça do jogador no tabuleiro

            # Chama a função para inverter as peças que estão nas posições do array ppti_up
            for i in ppti:
                tabuleiro.initial_state[i] = Jogador.symbol  

        print(ppti)  # Indice das posições trocadas
        print("\n")
    else:
        print("Jogada inválida. Escolha uma casa entre 0 e 63 que não esteja ocupada!\n")

    tabuleiro.ShowBoard()  # Exibe o estado do tabuleiro


PlayGame(jogador1)
PlayGame(jogador2)
PlayGame(jogador1)
