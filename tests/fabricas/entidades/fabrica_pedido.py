from tests.fabricas.fabrica_abstrata import FabricaAbstrata
from tests.fabricas.entidades.fabrica_produto import FabricaProduto
from enafood.entidades.principal.pedido import Pedido

class FabricaPedido(FabricaAbstrata):

    def fabricar_objeto_basico(self):
        """
        Cria uma instância básica de pedido,
        não contém nenhum produto.
        :return: Pedido
        """
        pedido = Pedido(data="01/01/2020",
                        valor_entrega=0.0,
                        produtos=[])
        return pedido

    def fabricar_pedido_com_1_produto(self):
        """
        Cria uma instância básica de pedido,
        contém 1 produto.
        :return: Pedido
        """
        produto = FabricaProduto().fabricar_objeto_basico()
        pedido = self.fabricar_objeto_basico()
        pedido.valor_entrega = 10.0
        # 2 produtos no pedido de valor total de R$ 10.00 cada
        pedido.adicionar_produto(produto, 2)
        return pedido

    def fabricar_pedido_status_em_conferencia(self):
        """
        Cria uma instância básica de pedido,
        contém 1 produto,
        status do pedido é EM_CONFERENCIA.
        :return: Pedido
        """
        pedido = self.fabricar_pedido_com_1_produto()
        pedido.conferir_pedido()
        return pedido