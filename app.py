from modelos.restaurante import Restaurante

restaurante_omotebako = Restaurante('Omotebako', 'Izakaya')

restaurante_serto = Restaurante('Sertó', 'Comida Mineira')
restaurante_serto.alternar_estado()
restaurante_serto.receber_avaliacao('Sawyer', 10)
restaurante_serto.receber_avaliacao('Joey', 8)
restaurante_serto.receber_avaliacao('Isis', 6)

restaurante_caracol = Restaurante('Caracol Bar', 'Bar')
restaurante_omotebako.alternar_estado()

def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()