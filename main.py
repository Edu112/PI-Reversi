import numpy as np 
class Tabuleiro:
    def __init__(self):
        self.initial_state = np.array([
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "x" , "o" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "o" , "x" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
            "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
        ]
        )

    def ShowBoard(self):
        print(self.initial_state.reshape(8, 8))
    
    def IsFilled(self,index):
        if self.initial_state[index] != "_":
            return True
        return False
        

    def UserInput(self,Jogador):
        position = int(input("Vez do "+Jogador.name+"\n Posição: "))
        if position not in range(0,64):           
            return print("Posição não está entre 0 e 64")
            
        elif not self.IsFilled(position):
            self.initial_state[position] = Jogador.symbol
        self.ShowBoard()


    def ValidMove(self,Jogador):
        return True
       

class Jogador:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol






jogador1 = Jogador("jogador1","x")
jogador2 = Jogador("jogador2","o")
jogo = Tabuleiro()
jogo.UserInput(jogador1)
