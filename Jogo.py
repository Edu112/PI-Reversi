from Tabuleiro import Tabuleiro
from Validador import Validador 
from Jogador import Jogador
from AgenteInteligente import AgenteInteligente
from No import No
import numpy as np 
import copy # Importante para fazer cópias profundas dos estados do jogo
import Minimax

class Jogo:
    def __init__(self, tabuleiro, jogador1, jogador2): 
        self.tabuleiro = tabuleiro # instância de Tabuleiro
        self.validador = Validador() # Pode ser instanciado aqui se não mudar entre jogos
        self.jogador1 = jogador1 # Será o Agente Inteligente
        self.jogador2 = jogador2 # Será o jogador humano
        self.jogadores = [self.jogador1, self.jogador2] # Lista de jogadores do jogo atual
        self.end_game = False
        self.winner = ""
        self.rounds = 0
        self.passedTurn = True ## Está correto começar como True?
        self.turno_max = None
        self.jogos_validos = []    
        self.roundOfPlayer = self.jogador1

    def calcular_utilidade(self):

        agent_mini_max = self.jogadores[0]
        jogador = self.jogadores[1]
        points_agent = len(agent_mini_max.pieces)
        points_jogador = len(jogador.pieces)

        return points_agent - points_jogador
    
    def gerar_jogadas_validas(self):

        agent = self.jogador1 if self.roundOfPlayer == self.jogador1 else self.jogador2
        jogadas_validas = []

        for i in range(64):
            if self.tabuleiro.initial_state[i] != "_":
                continue  # Posição já ocupada

            direcoes = [
                self.tabuleiro.CheckPossiblePlayToInvertVerticallyUp,
                self.tabuleiro.CheckPossiblePlayToInvertVerticallyDown,
                self.tabuleiro.CheckPossiblePlayToInvertHorizontallyRight,
                self.tabuleiro.CheckPossiblePlayToInvertHorizontallyLeft,
                self.tabuleiro.CheckPossiblePlayToInvertDiagonalLeftUp,
                self.tabuleiro.CheckPossiblePlayToInvertDiagonalLeftDown,
                self.tabuleiro.CheckPossiblePlayToInvertDiagonalRightUp,
                self.tabuleiro.CheckPossiblePlayToInvertDiagonalRightDown,
            ]

            for direcao in direcoes:
                if direcao(i, agent.symbol):  # se retorna lista não-vazia
                    jogadas_validas.append(i)
                    break

        return jogadas_validas


    def jogar(self, proximaJogada):
        if proximaJogada is None:
            return []
        agent = self.jogador1
        if self.roundOfPlayer == self.jogador1:
            opponent_pieces = self.positions_to_invert(proximaJogada, self.jogador2.symbol)
        else:
            opponent_pieces = self.positions_to_invert(proximaJogada, self.jogador1.symbol)
        # Copiar o tabuleiro
        new_tabuleiro = copy.deepcopy(self.tabuleiro)
        new_tabuleiro.initial_state[proximaJogada] = agent.symbol
        # Trocar jogadores
        novo_jogador1 = copy.deepcopy(self.jogador2)
        novo_jogador2 = copy.deepcopy(self.jogador1)

        if self.roundOfPlayer.symbol == "x":
            agent.pieces.append(proximaJogada)
            agent.pieces = agent.pieces + opponent_pieces
            self.jogador2.pieces = list(set(self.jogador2.pieces) - set(opponent_pieces))    
        else:
            self.jogador2.pieces.append(proximaJogada)
            self.jogador2.pieces = self.jogador2.pieces + opponent_pieces
            agent.pieces = list(set(agent.pieces) - set(opponent_pieces))
    

        # Criar novo estado de jogo
        novo_jogo = Jogo(new_tabuleiro, novo_jogador1, novo_jogador2)
        novo_jogo.rounds = self.rounds + 1
        # novo_jogo.turno_max = not self.turno_max #Desconfio que não precise disso

        # Verifica se o jogo terminou nesse novo estado
        fim, vencedor = self.verificar_fim_do_jogo(new_tabuleiro, novo_jogador1, novo_jogador2)
        novo_jogo.end_game = fim
        novo_jogo.winner = vencedor

        return novo_jogo
    

    def verificar_fim_do_jogo(self, tabuleiro, jogador1, jogador2):
        # Verifica se ambos os jogadores não têm mais jogadas válidas
        if not self.is_there_position_to_invert_in_the_game(jogador1) and not self.is_there_position_to_invert_in_the_game(jogador2):
            points_agent = len(jogador1.pieces)
            points_player2 = len(jogador2.pieces)
            vencedor = self.who_winner(points_agent, points_player2, retorno=True)
            return True, vencedor
        return False, ""
    def positions_to_invert(self, jogada_player, symbol_player):

        positions_to_invert = []

        invert_vertical_up = self.tabuleiro.PossiblePositionToInvertVerticallyUp(jogada_player,symbol_player)
        invert_vertical_down = self.tabuleiro.PossiblePositionToInvertVerticallyDown(jogada_player,symbol_player)
        invert_horizontal_right = self.tabuleiro.PossiblePositionToInvertHorizontallyRight(jogada_player,symbol_player)
        invert_horizontal_left = self.tabuleiro.PossiblePositionToInvertHorizontallyLeft(jogada_player,symbol_player)
        invert_diagonal_left_up = self.tabuleiro.PossiblePositionToInvertDiagonalLeftUp(jogada_player,symbol_player)
        invert_diagonal_left_down = self.tabuleiro.PossiblePositionToInvertDiagonalLeftDown(jogada_player,symbol_player)
        invert_diagonal_right_up = self.tabuleiro.PossiblePositionToInvertDiagonalRightUp(jogada_player,symbol_player)
        invert_diagonal_right_down = self.tabuleiro.PossiblePositionToInvertDiagonalRightDown(jogada_player,symbol_player)

        positions_to_invert = invert_vertical_down + invert_vertical_up + invert_horizontal_right +  invert_horizontal_left + invert_diagonal_left_up + invert_diagonal_left_down + invert_diagonal_right_up + invert_diagonal_right_down
        return positions_to_invert 

    def check_positions_to_invert(self, jogada_player, symbol_player):

        positions_to_invert = []

        invert_vertical_up = self.tabuleiro.CheckPossiblePlayToInvertVerticallyUp(jogada_player,symbol_player)
        invert_vertical_down = self.tabuleiro.CheckPossiblePlayToInvertVerticallyDown(jogada_player,symbol_player)
        invert_horizontal_right = self.tabuleiro.CheckPossiblePlayToInvertHorizontallyRight(jogada_player,symbol_player)
        invert_horizontal_left = self.tabuleiro.CheckPossiblePlayToInvertHorizontallyLeft(jogada_player,symbol_player)
        invert_diagonal_left_up = self.tabuleiro.CheckPossiblePlayToInvertDiagonalLeftUp(jogada_player,symbol_player)
        invert_diagonal_left_down = self.tabuleiro.CheckPossiblePlayToInvertDiagonalLeftDown(jogada_player,symbol_player)
        invert_diagonal_right_up = self.tabuleiro.CheckPossiblePlayToInvertDiagonalRightUp(jogada_player,symbol_player)
        invert_diagonal_right_down = self.tabuleiro.CheckPossiblePlayToInvertDiagonalRightDown(jogada_player,symbol_player)

        positions_to_invert = invert_vertical_down + invert_vertical_up + invert_horizontal_right +  invert_horizontal_left + invert_diagonal_left_up + invert_diagonal_left_down + invert_diagonal_right_up + invert_diagonal_right_down
        return positions_to_invert  

    def agent_invertible_pieces_per_direction(self, from_this_index):

        agent = self.jogador1

        invert_vertical_up = self.tabuleiro.CheckPossiblePlayToInvertVerticallyUp(from_this_index, agent.symbol)
        invert_vertical_down = self.tabuleiro.CheckPossiblePlayToInvertVerticallyDown(from_this_index,agent.symbol)
        invert_horizontal_right = self.tabuleiro.CheckPossiblePlayToInvertHorizontallyRight(from_this_index,agent.symbol)
        invert_horizontal_left = self.tabuleiro.CheckPossiblePlayToInvertHorizontallyLeft(from_this_index,agent.symbol)
        invert_diagonal_left_up = self.tabuleiro.CheckPossiblePlayToInvertDiagonalLeftUp(from_this_index,agent.symbol)
        invert_diagonal_left_down = self.tabuleiro.CheckPossiblePlayToInvertDiagonalLeftDown(from_this_index,agent.symbol)
        invert_diagonal_right_up = self.tabuleiro.CheckPossiblePlayToInvertDiagonalRightUp(from_this_index,agent.symbol)
        invert_diagonal_right_down = self.tabuleiro.CheckPossiblePlayToInvertDiagonalRightDown(from_this_index,agent.symbol)
     


        invertible_pieces_per_direction = [invert_vertical_up, invert_vertical_down, invert_horizontal_right, invert_horizontal_left, invert_diagonal_left_up, invert_diagonal_left_down, invert_diagonal_right_up, invert_diagonal_right_down]
        return invertible_pieces_per_direction

    def is_there_position_to_invert_from_this_index(self, Jogador, jogada): 
        
        pti = self.positions_to_invert(jogada, Jogador.symbol)

        if len(pti) != 0:
            return True
        
        return False

    def is_there_position_to_invert_in_the_game(self, Jogador): 
        for i in range(len(Jogador.pieces)):
            self.tabuleiro.list_possible_play = []  # <--- LIMPA A LISTA
            self.check_positions_to_invert(Jogador.pieces[i], Jogador.symbol)

            if True in self.tabuleiro.list_possible_play:
                return True

        return False

    def who_winner(self, points_player1, points_player2, retorno=False): 
        if points_player1 > points_player2:
            self.winner = self.jogador1.name
        elif points_player2 > points_player1:
            self.winner = self.jogador2.name
        else:
            self.winner = "empate"

        if retorno:
            return self.winner


    def change_end_game(self):

        agent = self.jogador1
        total_pieces = agent.pieces + self.jogador2.pieces
        points_agent = len(agent.pieces)
        points_player2 = len(self.jogador2.pieces)

        if len(total_pieces) == 64:
            self.end_game = True
            self.who_winner(points_agent, points_player2)
            return
        
        if points_agent == 0:
            self.end_game = True
            self.winner = "jogador2"
            return

        if points_player2 == 0:
            self.end_game = True
            self.winner = "jogador1"
            return
        
        check_plays_agent = self.is_there_position_to_invert_in_the_game(agent)
        check_plays_jogador2 = self.is_there_position_to_invert_in_the_game(self.jogador2)

        if not check_plays_agent and not check_plays_jogador2:
            self.end_game = True
            self.who_winner(points_agent, points_player2)
            return 
        
    def play_game(self, Jogador):
        agent = self.jogador1
        self.tabuleiro.list_possible_play = []
        jogada_player = 0

        if self.roundOfPlayer == self.jogador1:

            self.turno_max = True
            agent.qtd_invertible_pieces = 0

            self.jogos_validos = self.gerar_jogadas_validas()
            jogada_player = Minimax.melhor_jogada_agente(self)

        else:
            self.jogos_validos = self.gerar_jogadas_validas()
            try:
                jogada_player = Jogador.UserInput()
            except ValueError:
                print("Você não digitou um número válido.")
                return
                
        possible_move = self.validador.PossibleMove(self.tabuleiro, jogada_player) 
        possible_invert = self.is_there_position_to_invert_from_this_index(Jogador,jogada_player)

        if possible_move and possible_invert: 
            print(f"Jogada válida {jogada_player}\n")

            opponent_pieces = self.positions_to_invert(jogada_player, Jogador.symbol) 

            if Jogador.symbol == "x":
                agent.pieces.append(jogada_player)
                agent.pieces = agent.pieces + opponent_pieces
                self.jogador2.pieces = list(set(self.jogador2.pieces) - set(opponent_pieces))    
            else:
                self.jogador2.pieces.append(jogada_player)
                self.jogador2.pieces = self.jogador2.pieces + opponent_pieces
                agent.pieces = list(set(agent.pieces) - set(opponent_pieces))
        
            agent.pieces = list(set(agent.pieces))
            self.jogador2.pieces = list(set(self.jogador2.pieces))
            
            if opponent_pieces != []:
                self.tabuleiro.initial_state[jogada_player] = Jogador.symbol  # Coloca a peça do jogador no tabuleiro

            for i in opponent_pieces:
                self.tabuleiro.initial_state[i] = Jogador.symbol

            self.rounds += 1 # Faz sentido depois que apenas um jogador joga nós incrementarmos round?
            self.passedTurn = True
        else:
            print(f"Jogada inválida. {jogada_player} Jogue novamente {Jogador.symbol} \n")
            self.passedTurn = False
        self.tabuleiro.ShowBoard()


    def verify_winner(self):
        
        if self.winner == "empate":
            print("\nA partida acabou empatada!")
        else:
            print(f"\n{self.winner} venceu o jogo!")

    def game_loop(self):
        self.tabuleiro.ShowBoard()
        while not self.end_game: 
            if self.passedTurn :
                self.roundOfPlayer = self.jogadores[self.rounds % 2]     
            self.play_game(self.roundOfPlayer)
            self.change_end_game()
            
        self.verify_winner()
        return