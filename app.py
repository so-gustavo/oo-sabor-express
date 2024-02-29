from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_omotebako = Restaurante('Omotebako', 'Izakaya')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_baiao_de_dois = Prato('Baião de Dois', 59.0, 'Com feijão fradinho, carne seca, queijo coalho e especiarias nordestinas')
prato_baiao_de_dois.aplicar_desconto()
restaurante_omotebako.adicionar_no_cardapio(bebida_suco)
restaurante_omotebako.adicionar_no_cardapio(prato_baiao_de_dois)

def main():
    restaurante_omotebako.exibir_cardapio

if __name__ == '__main__':
    main()