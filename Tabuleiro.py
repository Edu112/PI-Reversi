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
        ])

    def ShowBoard(self):
        print(self.initial_state.reshape(8, 8))


    def generateASuccessor():
        return

    