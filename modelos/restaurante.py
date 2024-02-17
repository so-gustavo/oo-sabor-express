class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self) #isso faz um append do próprio restaurante para a lista de restaurantes

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls): #função que substitui a parte de printar as informaçoes para cada um dos restaurantes no final do código
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        return 'Verdadeiro' if self._ativo else 'Falso'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_serto = Restaurante('Sertó', 'Comida Mineira')
restaurante_serto.alternar_estado()
restaurante_caracol = Restaurante('Caracol Bar', 'Bar')