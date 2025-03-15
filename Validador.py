class Validador:

    def ValidMove(self, Tabuleiro, index):

        if index not in range(0,64) or Tabuleiro.initial_state[index] != "_":           
            return False
        

        return True
    

        

    


