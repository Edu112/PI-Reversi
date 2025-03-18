class No:
    def __init__(self, estado, pontuacao):
        self.estado = estado
        self.pontuacao = pontuacao

    '''   
    def __init__(self, estado, no_pai=None, vertice=None):
        self.estado = estado
        self.no_pai = no_pai
        self.vertice = vertice

    def no_caminho(no):
        caminho = [no.estado]
        while no.no_pai is not None:
            no = no.no_pai
            caminho.append(no.estado)
        caminho.reverse()
        return caminho

    def vertice_caminho(no):
        caminho = []
        while no.no_pai is not None:
            no = no.no_pai
            if no.vertice is not None: caminho.append(no.vertice)
        caminho.reverse()
        return caminho
        '''
