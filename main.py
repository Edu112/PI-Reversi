from Jogo import Jogo
from Tabuleiro import Tabuleiro
from Jogador import Jogador


tabuleiro = Tabuleiro()
jogador1 = Jogador("Agente", "x",[27,36])
jogador2 = Jogador("Humano", "o",[28,35])

jogadores = [jogador1, jogador2]

jogo = Jogo(tabuleiro, jogador1, jogador2)

jogo.game_loop()