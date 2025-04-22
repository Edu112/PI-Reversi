from Jogador import Jogador

class AgenteInteligente(Jogador): # Herda de Jogador

    def __init__(self, name, symbol, pieces):
        self.name = name
        self.symbol = symbol
        self.pieces = pieces
        self.qtd_invertible_pieces = 0
        self.index_to_play = 0

    def heuristica(self, invertible_pieces_per_direction):
        qtd_invertible_pieces_per_direction = []
        
        for pieces in invertible_pieces_per_direction:
            qtd_invertible_pieces_per_direction.append(len(pieces))

        greater_quantity = max(qtd_invertible_pieces_per_direction)

        if self.qtd_invertible_pieces < greater_quantity:
            self.qtd_invertible_pieces = greater_quantity

            if qtd_invertible_pieces_per_direction.index(greater_quantity) == 0: # direction = "up"
                less_index = len(invertible_pieces_per_direction[0]) - 1
                self.index_to_play = invertible_pieces_per_direction[0][less_index] - 8

            elif qtd_invertible_pieces_per_direction.index(greater_quantity) == 1: # direction = "down"
                less_index = len(invertible_pieces_per_direction[1]) - 1
                self.index_to_play = invertible_pieces_per_direction[1][less_index] + 8

            elif qtd_invertible_pieces_per_direction.index(greater_quantity) == 2: # direction = "horizontal right"

                less_index = len(invertible_pieces_per_direction[2]) - 1
                self.index_to_play = invertible_pieces_per_direction[2][less_index] + 1


            elif qtd_invertible_pieces_per_direction.index(greater_quantity) == 3: # direction = "horizontal left"
                less_index = len(invertible_pieces_per_direction[3]) - 1
                self.index_to_play = invertible_pieces_per_direction[3][less_index] - 1


            elif qtd_invertible_pieces_per_direction.index(greater_quantity) == 4: # direction = "diagonal left up"
                less_index = len(invertible_pieces_per_direction[4]) - 1                
                self.index_to_play = invertible_pieces_per_direction[4][less_index] - 9


            elif qtd_invertible_pieces_per_direction.index(greater_quantity) == 5: # direction = "diagonal left down"
                less_index = len(invertible_pieces_per_direction[5]) - 1
                self.index_to_play = invertible_pieces_per_direction[5][less_index] + 7

            elif qtd_invertible_pieces_per_direction.index(greater_quantity) == 6: # direction = "diagonal right up"
                less_index = len(invertible_pieces_per_direction[6]) - 1
                self.index_to_play = invertible_pieces_per_direction[6][less_index] - 7

            else: # direction = "diagonal right down"
                less_index = len(invertible_pieces_per_direction[7]) - 1
                self.index_to_play = invertible_pieces_per_direction[7][less_index] + 9 

            
