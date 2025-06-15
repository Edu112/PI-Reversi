from Tabuleiro import Tabuleiro
from AgenteInteligente import AgenteInteligente

# Variáveis globais do jogo
tabuleiro = Tabuleiro()
agent = AgenteInteligente("Inteligência Artifical", "x", [27,36])

class Reversi:

    def positions_to_invert(self, jogada_player, symbol_player):

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

    def check_positions_to_invert(self, jogada_player, symbol_player):

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

    def agent_invertible_pieces_per_direction(self, from_this_index):

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