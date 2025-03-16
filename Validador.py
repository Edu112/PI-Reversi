class Validador:

    
    def __init__(self, validMove):
        self.validMove = validMove


    def PossibleMove(self, Tabuleiro, index):

        if index in range(0,64) or Tabuleiro.initial_state[index] == "_":           
            return True
        

        return False
    

        

    


