# Codificação de Estado

Lista
_ =  vazio; 
x = jogador1;
o = jogador2;

-------------------------------------------------------------------------------------------------------------------

# Estado de Inicilização

```python
estadoInicial = [
    "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
    "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
    "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
    "_" , "_" , "_" , "x" , "o" , "_" , "_" , "_" ,
    "_" , "_" , "_" , "o" , "x" , "_" , "_" , "_" ,
    "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
    "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" ,
    "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , 
]

indexVisual = [
    "00" , "01" , "02" , "03" , "04" , "05" , "06" , "07" ,
    "08" , "09" , "10" , "11" , "12" , "13" , "14" , "15" ,
    "16" , "17" , "18" , "19" , "20" , "21" , "22" , "23" ,
    "24" , "25" , "26" , "x " , " o" , "29" , "30" , "31" ,
    "32" , "33" , "34" , " o" , "x " , "37" , "38" , "39" ,
    "40" , "41" , "42" , "43" , "44" , "45" , "46" , "47" ,
    "48" , "49" , "50" , "51" , "52" , "53" , "54" , "55" ,
    "56" , "57" , "58" , "59" , "60" , "61" , "62" , "63" , 
]


```
-------------------------------------------------------------------------------------------------------------------
# Estado de Aceitação

Quando o jogador não tem mais jogadas possíveis.

ou seja: 

- Todas as casas estiverem preenchidas.

- Nenhum dos dois jogadores tiver jogadas possíveis (não conseguir comer nenhuma peça do adversário ).  

- O jogador não ter mais peças no tabuleiro.

-------------------------------------------------------------------------------------------------------------------
# Codificação da posição

Peça->Posição do Tabuleiro
**Exemplo**

- x->43

- o->44

-------------------------------------------------------------------------------------------------------------------
# Função de Utilidade

Função que calcula uma pontuação a favor de agente a partir de estados.

Cada jogo tem sua funcao de utilidade para os estados.

Obs: Eu não sei como fazer a nossa própria função de utilidade. (ainda)

função de utilidade --> número de peças do agente - número de peças do oponente.
 Exemplo (inicio do jogo): 2 - 2 = 0 . 
 Exemplo (situação aonde o agente está melhor na partida): 20 - 10 = 10
 Exemplo (situação aonde o agente está pior na partida): 5 - 30 = -25









-------------------------------------------------------------------------------------------------------------

# Validação dos movimentos

A partir de uma jogada "x" ou "o" na casa [n], percorremos todas as posições da direção de [n] na vertical, para cima e para baixo; se encontrarmos peças do adversário entre dois "x" ou "o", guardamos as posições das peças adversárias. Após isso, faremos o mesmo método percorrendo todas as posições na horizontal e nas duas diagonais. Ao final, invertemos todas as peças que guardamos.



-------------------------------------------------------------------------------------------------------

# Visual para o Jogador

Colocar o index em jogadas válidas.

---------------------------------------------------------------------------------------------------------------------
# Maper o tabuleiro

Lista x = Peças de x

Lista o = Peças de o


dict jogadasPossiviesX = {
    index = array de jogadas possiveis
}

dict jogadasPossiviesO ={
    index = array de jogadas possiveis
}

# Validar lista de peças

Toda vez que a peça y comer z 

tirar da lista z e colocar na lista y


# Validar jogadas possiveis 

Ideia a curto prazo:

Fazer um metodo que pega todas peças do jogador e ve se tem jogadas possiveis 

esse loop para quando ele achar a primeira jogada possivel 

se nao achar jogadas possiveis, passará a vez.
 



Ideia a longo prazo :

pegar todas as peças que viraram e tirar do dict do oponente

e todas as peças que viraram colocar em jogadas possiveis do jogador 



