from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_omotebako = Restaurante('Omotebako', 'Izakaya')
bebida_suco = Bebida('Negroni', 22.0, 'único')
baiao_de_dois = Prato('Baião de Dois', 59.0, 'Com feijão fradinho, carne seca, queijo coalho e especiarias nordestinas')

def main():
    print(bebida_suco)
    print(baiao_de_dois)

if __name__ == '__main__':
    main()