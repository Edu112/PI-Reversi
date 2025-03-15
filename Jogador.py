class Jogador:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def UserInput(self):
        position = int(input("Vez do "+self.name+"\n Posição: "))
        return position