class Jogador:
    
    def __init__(self, name, symbol, pieces, possiblePlay):
        self.name = name
        self.symbol = symbol
        self.pieces = pieces
        self.possiblePlay = possiblePlay

    def UserInput(self):
        position = int(input("Vez do "+self.name+" ("+ self.symbol+") " +"\n Posição: "))
        return position