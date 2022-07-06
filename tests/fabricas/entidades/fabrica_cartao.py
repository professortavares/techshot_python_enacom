from enafood.entidades.principal.cartao import Cartao
from tests.fabricas.fabrica_abstrata import FabricaAbstrata


class FabricaCartao (FabricaAbstrata):

    def fabricar_objeto_basico(self):
        """
        Cria uma instância básica de cartão,
        não contém nenhum pagamento.
        :return: Cartao
        """
        cartao = Cartao(pedido=None,
                        numero="1234567890123456",
                        nome_titular="João",
                        data_validade="01/20",
                        cvv="123",
                        eh_valido=True,
                        eh_ativo=True)
        return cartao
