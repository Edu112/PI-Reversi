from Tabuleiro import Tabuleiro
from Validador import Validador 
from Jogador import Jogador
from AgenteInteligente import AgenteInteligente
from No import No
import numpy as np 

# Variáveis globais do jogo
tabuleiro = Tabuleiro()
validador = Validador()
jogador1 = Jogador("Eduardo", "x", [27,36])
jogador2 = Jogador("Andre", "o", [28,35])
agent = AgenteInteligente("Inteligência Artifical", "x", [27,36])
jogadores = [agent, jogador2]
end_game = False
winner = ""
rounds = 0
passedTurn = True

def utilidade(Jogador1, Jogador2):

    points_player1 = len(Jogador1.pieces)
    points_player2 = len(Jogador2.pieces)

    return points_player1 - points_player2

    
# Variáveis globais dos nós
caminhos = [] # lista de nós
tabuleiro_as_list = tabuleiro.initial_state.tolist()
pontuacao_atual = utilidade(jogador1, jogador2)
no_initial = No(tabuleiro_as_list, pontuacao_atual)
caminhos.append(no_initial)


tabuleiro.ShowBoard()

def positions_to_invert(jogada_player, symbol_player):

    positions_to_invert = []

    invert_vertical_up = tabuleiro.PossiblePositionToInvertVerticallyUp(jogada_player,symbol_player)
    invert_vertical_down = tabuleiro.PossiblePositionToInvertVerticallyDown(jogada_player,symbol_player)
    invert_horizontal_right = tabuleiro.PossiblePositionToInvertHorizontallyRight(jogada_player,symbol_player)
    invert_horizontal_left = tabuleiro.PossiblePositionToInvertHorizontallyLeft(jogada_player,symbol_player)
    invert_diagonal_left_up = tabuleiro.PossiblePositionToInvertDiagonalLeftUp(jogada_player,symbol_player)
    invert_diagonal_left_down = tabuleiro.PossiblePositionToInvertDiagonalLeftDown(jogada_player,symbol_player)
    invert_diagonal_right_up = tabuleiro.PossiblePositionToInvertDiagonalRightUp(jogada_player,symbol_player)
    invert_diagonal_right_down = tabuleiro.PossiblePositionToInvertDiagonalRightDown(jogada_player,symbol_player)

    positions_to_invert = invert_vertical_down + invert_vertical_up + invert_horizontal_right +  invert_horizontal_left + invert_diagonal_left_up + invert_diagonal_left_down + invert_diagonal_right_up + invert_diagonal_right_down
    return positions_to_invert  

def check_positions_to_invert(jogada_player, symbol_player):

    positions_to_invert = []

    invert_vertical_up = tabuleiro.CheckPossiblePlayToInvertVerticallyUp(jogada_player,symbol_player)
    invert_vertical_down = tabuleiro.CheckPossiblePlayToInvertVerticallyDown(jogada_player,symbol_player)
    invert_horizontal_right = tabuleiro.CheckPossiblePlayToInvertHorizontallyRight(jogada_player,symbol_player)
    invert_horizontal_left = tabuleiro.CheckPossiblePlayToInvertHorizontallyLeft(jogada_player,symbol_player)
    invert_diagonal_left_up = tabuleiro.CheckPossiblePlayToInvertDiagonalLeftUp(jogada_player,symbol_player)
    invert_diagonal_left_down = tabuleiro.CheckPossiblePlayToInvertDiagonalLeftDown(jogada_player,symbol_player)
    invert_diagonal_right_up = tabuleiro.CheckPossiblePlayToInvertDiagonalRightUp(jogada_player,symbol_player)
    invert_diagonal_right_down = tabuleiro.CheckPossiblePlayToInvertDiagonalRightDown(jogada_player,symbol_player)

    positions_to_invert = invert_vertical_down + invert_vertical_up + invert_horizontal_right +  invert_horizontal_left + invert_diagonal_left_up + invert_diagonal_left_down + invert_diagonal_right_up + invert_diagonal_right_down
    return positions_to_invert  

def agent_invertible_pieces_per_direction(from_this_index):

    invert_vertical_up = tabuleiro.CheckPossiblePlayToInvertVerticallyUp(from_this_index, agent.symbol)
    invert_vertical_down = tabuleiro.CheckPossiblePlayToInvertVerticallyDown(from_this_index,agent.symbol)
    invert_horizontal_right = tabuleiro.CheckPossiblePlayToInvertHorizontallyRight(from_this_index,agent.symbol)
    invert_horizontal_left = tabuleiro.CheckPossiblePlayToInvertHorizontallyLeft(from_this_index,agent.symbol)
    invert_diagonal_left_up = tabuleiro.CheckPossiblePlayToInvertDiagonalLeftUp(from_this_index,agent.symbol)
    invert_diagonal_left_down = tabuleiro.CheckPossiblePlayToInvertDiagonalLeftDown(from_this_index,agent.symbol)
    invert_diagonal_right_up = tabuleiro.CheckPossiblePlayToInvertDiagonalRightUp(from_this_index,agent.symbol)
    invert_diagonal_right_down = tabuleiro.CheckPossiblePlayToInvertDiagonalRightDown(from_this_index,agent.symbol)

    invertible_pieces_per_direction = [invert_vertical_up, invert_vertical_down, invert_horizontal_right, invert_horizontal_left, invert_diagonal_left_up, invert_diagonal_left_down, invert_diagonal_right_up, invert_diagonal_right_down]
    return invertible_pieces_per_direction

def is_there_position_to_invert_from_this_index(Jogador, jogada): 
    
    pti = positions_to_invert(jogada, Jogador.symbol)

    if len(pti) != 0:
        return True
    
    return False

def is_there_position_to_invert_in_the_game(Jogador): 

    for i in range(0, len(Jogador.pieces)):

        check_positions_to_invert(Jogador.pieces[i], Jogador.symbol) 
        if True in tabuleiro.list_possible_play: # verifica se tem jogadas possiveis para qualquer sentido
            return True
        
    return False

def who_winner(points_player1, points_player2): 
    # Descobre o ganhador 
    global winner

    if points_player1 > points_player2 :
        winner = jogador1.name
    elif points_player2 > points_player1 :
        winner = jogador2.name
    else:
        winner = "empate"

    return    

def change_end_game():

    global end_game
    global winner
    total_pieces = agent.pieces + jogador2.pieces
    points_agent = len(agent.pieces)
    points_player2 = len(jogador2.pieces)

    if len(total_pieces) == 64:
        end_game = True
        who_winner(points_agent, points_player2)
        return

    if (points_agent == 0):
        end_game = True
        winner = "jogador1"
        return
    
    if(points_agent == 0):
        end_game = True 
        winner == "jogador2"
        return
    
    check_plays_agent = is_there_position_to_invert_in_the_game(agent)
    check_plays_jogador2 = is_there_position_to_invert_in_the_game(jogador2)

    if not check_plays_agent and not check_plays_jogador2:
        end_game = True
        who_winner(points_agent, points_player2)
        return 
    
def play_game(Jogador):
    global passedTurn
    global rounds
    tabuleiro.list_possible_play = []
    jogada_player = 0

    if isinstance(Jogador, AgenteInteligente):
        agent.qtd_invertible_pieces = 0
        for i in range(len(agent.pieces)):
            aippd = agent_invertible_pieces_per_direction(agent.pieces[i]) # aippd (Abreviação)
            agent.heuristica(aippd)

        jogada_player = agent.index_to_play

    else:
        try:
            jogada_player = Jogador.UserInput()
        except ValueError:
            print("Você não digitou um número válido.")
            return
    
    possible_move = validador.PossibleMove(tabuleiro, jogada_player) 
    possible_invert = is_there_position_to_invert_from_this_index(Jogador,jogada_player)

    if possible_move and possible_invert: 
        print(f"Jogada válida {jogada_player}\n")

        opponent_pieces = positions_to_invert(jogada_player, Jogador.symbol) 

        if Jogador.symbol == "x":
            agent.pieces.append(jogada_player)
            agent.pieces = agent.pieces + opponent_pieces
            jogador2.pieces = list(set(jogador2.pieces) - set(opponent_pieces))    
        else:
            jogador2.pieces.append(jogada_player)
            jogador2.pieces = jogador2.pieces + opponent_pieces
            agent.pieces = list(set(agent.pieces) - set(opponent_pieces))
    
        agent.pieces = list(set(agent.pieces))
        jogador2.pieces = list(set(jogador2.pieces))
        
        if opponent_pieces != []:
            tabuleiro.initial_state[jogada_player] = Jogador.symbol  # Coloca a peça do jogador no tabuleiro

        for i in opponent_pieces:
            tabuleiro.initial_state[i] = Jogador.symbol
        
        tabuleiro_as_list = tabuleiro.initial_state.tolist()
        pontuacao_atual = utilidade(jogador1, jogador2)
        new_no = No(tabuleiro_as_list, pontuacao_atual)
        caminhos.append(new_no)

        rounds += 1 # Faz sentido depois que apenas um jogador joga nós incrementarmos round?
        passedTurn = True
    else:
        print(f"Jogada inválida. {jogada_player} Jogue novamente \n")
        passedTurn = False
    tabuleiro.ShowBoard()

def verify_winner():
    
    if winner == "empate":
        print("\nA partida acabou empatada!")
    else:
        print(f"\n{winner} venceu o jogo!")

def game_loop(jogadores):
    
    while not end_game: 
        if passedTurn :
            roundOfPlayer = jogadores[rounds % 2]     
        play_game(roundOfPlayer)
        change_end_game()
        
    verify_winner()
    return

game_loop(jogadores)

