class restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_serto = restaurante('Sertó', 'Comida Mineira')
restaurante_caracol = restaurante('Caracol Bar', 'Bar')

restaurantes = [restaurante_serto, restaurante_caracol]

print(restaurante_serto)
print(restaurante_caracol)
