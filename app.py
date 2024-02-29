from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_omotebako = Restaurante('Omotebako', 'Izakaya')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_baiao_de_dois = Prato('Baião de Dois', 59.0, 'Com feijão fradinho, carne seca, queijo coalho e especiarias nordestinas')
prato_baiao_de_dois.aplicar_desconto()
sobremesa_petit_gateau = Sobremesa('Petit Gateau', 6.0, 'Bolo', 'Médio')
sobremesa_petit_gateau.aplicar_desconto()
restaurante_omotebako.adicionar_no_cardapio(bebida_suco)
restaurante_omotebako.adicionar_no_cardapio(prato_baiao_de_dois)
restaurante_omotebako.adicionar_no_cardapio(sobremesa_petit_gateau)

def main():
    restaurante_omotebako.exibir_cardapio

if __name__ == '__main__':
    main()