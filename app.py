from modelos.restaurante import Restaurante

restaurante_omotebako = Restaurante('Omotebako', 'Izakaya')

restaurante_serto = Restaurante('Sertó', 'Comida Mineira')
restaurante_serto.alternar_estado()
restaurante_serto.receber_avaliacao('Sawyer', 5)
restaurante_serto.receber_avaliacao('Joey', 4)
restaurante_serto.receber_avaliacao('Isis', 4)

restaurante_caracol = Restaurante('Caracol Bar', 'Bar')
restaurante_omotebako.alternar_estado()

def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()