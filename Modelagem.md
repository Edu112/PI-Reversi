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
    "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" ,
    "8" , "9" , "10" , "11" , "12" , "13" , "14" , "15" ,
    "16" , "17" , "18" , "19" , "20" , "21" , "22" , "23" ,
    "24" , "25" , "26" , "x" , "o" , "29" , "30" , "31" ,
    "32" , "33" , "34" , "o" , "x" , "37" , "38" , "39" ,
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