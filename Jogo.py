from Tabuleiro import Tabuleiro
from Validador import Validador
from Jogador import Jogador
from AgenteInteligente import AgenteInteligente
from No import No # Se No for usado dentro da classe, senão pode ser movido
import numpy as np
import copy # Importante para fazer cópias profundas dos estados do jogo
import minmax

class Jogo:
    def __init__(self, tabuleiro, jogador1_obj, jogador2_obj): # Nomes mais claros para evitar confusão com globais
        self.tabuleiro = tabuleiro # Agora é uma instância de Tabuleiro
        self.validador = Validador() # Pode ser instanciado aqui se não mudar entre jogos
        self.jogador1 = jogador1_obj # Será o Agente Inteligente
        self.jogador2 = jogador2_obj # Será o jogador humano
        self.jogadores = [self.jogador1, self.jogador2] # Lista de jogadores do jogo atual
        self.end_game = False
        self.winner = ""
        self.rounds = 0
        self.passedTurn = True
        self.turno_max = None
        self.jogos_validos = []

    def calcular_utilidade(self):

        agent_mini_max = self.jogadores[0]
        jogador = self.jogadores[1]
        points_agent = len(agent_mini_max.pieces)
        points_jogador = len(jogador.pieces)

        return points_agent - points_jogador

    def jogar(self, proximaJogada):
        agent = self.jogador1
        opponent_pieces = self.positions_to_invert(proximaJogada, Jogador.symbol)
        # Copiar o tabuleiro
        new_tabuleiro = copy.deepcopy(self.tabuleiro)
        new_tabuleiro.initial_state[proximaJogada] = self.jogador1.symbol
        # Trocar jogadores
        novo_jogador1 = copy.deepcopy(self.jogador2)
        novo_jogador2 = copy.deepcopy(self.jogador1)

        if Jogador.symbol == "x":
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
        novo_jogo.turno_max = not self.turno_max

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


    

    def ShowBoardGame(self):
        self.tabuleiro.ShowBoard()

    

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

        invert_vertical_up = self.tabuleiro.CheckPossiblePlayToInvertVerticallyUp(from_this_index, agent.symbol) # Lista de indices que o agente pode jogar
        invert_vertical_down = self.tabuleiro.CheckPossiblePlayToInvertVerticallyDown(from_this_index,agent.symbol)
        invert_horizontal_right = self.tabuleiro.CheckPossiblePlayToInvertHorizontallyRight(from_this_index,agent.symbol)
        invert_horizontal_left = self.tabuleiro.CheckPossiblePlayToInvertHorizontallyLeft(from_this_index,agent.symbol)
        invert_diagonal_left_up = self.tabuleiro.CheckPossiblePlayToInvertDiagonalLeftUp(from_this_index,agent.symbol)
        invert_diagonal_left_down = self.tabuleiro.CheckPossiblePlayToInvertDiagonalLeftDown(from_this_index,agent.symbol)
        invert_diagonal_right_up = self.tabuleiro.CheckPossiblePlayToInvertDiagonalRightUp(from_this_index,agent.symbol)
        invert_diagonal_right_down = self.tabuleiro.CheckPossiblePlayToInvertDiagonalRightDown(from_this_index,agent.symbol)

        self.jogos_validos = invert_vertical_up + invert_vertical_down + invert_horizontal_right + invert_horizontal_left + invert_diagonal_left_up + invert_diagonal_left_down + invert_diagonal_right_up + invert_diagonal_right_down

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

    def who_winner(self, points_player1, points_player2): 
        # Descobre o ganhador 

        if points_player1 > points_player2 :
            self.winner = self.jogador1.name
        elif points_player2 > points_player1 :
            self.winner = self.jogador2.name
        else:
            self.winner = "empate"

        return    

    def change_end_game(self):

        agent = self.jogador1
        total_pieces = agent.pieces + self.jogador2.pieces
        points_agent = len(agent.pieces)
        points_player2 = len(self.jogador2.pieces)

        if len(total_pieces) == 64:
            self.end_game = True
            self.who_winner(points_agent, points_player2)
            return

        if (points_agent == 0):
            self.end_game = True
            self.winner = "jogador1"
            return
        
        if(points_agent == 0):
            self.end_game = True 
            self.winner == "jogador2"
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

        if isinstance(Jogador, AgenteInteligente):
            self.turno_max = True
            agent.qtd_invertible_pieces = 0
            for i in range(len(agent.pieces)):
                aippd = self.agent_invertible_pieces_per_direction(agent.pieces[i]) # aippd (Abreviação)
                agent.heuristica(aippd)

               #### 
            self.turno_max = not self.turno_max
            jogada_player = minmax.melhor_jogada_agente(self)
            self.jogos_validos = []

        else:
            for i in range(len(Jogador.pieces)):
                self.jogos_validos += self.check_positions_to_invert(Jogador.pieces[i],Jogador.symbol)

                ####
            self.turno_max = not self.turno_max
            minmax.melhor_jogada_agente(self)
            self.jogos_validos = []
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
            
            tabuleiro_as_list = self.tabuleiro.initial_state.tolist()
            pontuacao_atual = self.calcular_utilidade()

            self.rounds += 1 # Faz sentido depois que apenas um jogador joga nós incrementarmos round?
            self.passedTurn = True
        else:
            print(f"Jogada inválida. {jogada_player} Jogue novamente \n")
            self.passedTurn = False
        self.tabuleiro.ShowBoard()

    def verify_winner(self):
        
        if self.winner == "empate":
            print("\nA partida acabou empatada!")
        else:
            print(f"\n{self.winner} venceu o jogo!")

    def game_loop(self,jogadores):
        self.tabuleiro.ShowBoard()
        while not self.end_game: 
            if self.passedTurn :
                roundOfPlayer = jogadores[self.rounds % 2]     
            self.play_game(roundOfPlayer)
            self.change_end_game()
            
        self.verify_winner()
        return

    def RodarJogo(self):
        self.game_loop(self.jogadores)


