from modelos.restaurante import Restaurante

restaurante_omotebako = Restaurante('Omotebako', 'Izakaya')
restaurante_omotebako.alternar_estado()

def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()