from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_omotebako = Restaurante('Omotebako', 'Izakaya')
bebida_suco = Bebida('Negroni', 22.0, 'único')
prato_baiao_de_dois = Prato('Baião de Dois', 59.0, 'Com feijão fradinho, carne seca, queijo coalho e especiarias nordestinas')
restaurante_omotebako.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_omotebako.adicionar_prato_no_cardapio(prato_baiao_de_dois)

def main():
    print(bebida_suco)
    print(prato_baiao_de_dois)

if __name__ == '__main__':
    main()