from dataclasses import dataclass
from enafood.entidades.principal.status_pedido import StatusPedido
from enafood.excecoes.excecao_alteracao_status_invalida import ExcecaoAlteracaoDeStatusInvalida

@dataclass
class Pedido:
    data: str
    valor_entrega:float
    produtos: list[any]
    pagamento: any=None
    historico: list[any]=None
    cliente: any=None
    #TODO: débito técnico: criar uma propriedade para este atributo
    status: StatusPedido=StatusPedido.EM_COMPRA

    # Débito técnico
    # TODO: rever a obrigatoriedade dos campos

    def calcular_valor_total(self):
        """
        Calcula o valor total do pedido
        :return: float - preco unitário * quantidade
        """
        valor_total = 0.0
        for produto_no_pedido in self.produtos:
            valor_total += produto_no_pedido.calcular_valor_total()

        return valor_total + self.valor_entrega

    def alterar_status_pedido(self, novo_status):
        """
        Altera o status do pedido
        :param novo_status: StatusPedido - novo status do pedido
        :return: None
        """

        # fluxo para o status EM_COMPRA
        if self.status == StatusPedido.EM_COMPRA:
            if novo_status != StatusPedido.EM_CONFERENCIA:
                raise ExcecaoAlteracaoDeStatusInvalida(status_pedido_atual=self.status, status_pedido_novo=novo_status)
        # fluxo para o status EM_CONFERENCIA
        elif self.status == StatusPedido.EM_CONFERENCIA:
            if novo_status != StatusPedido.EM_COMPRA:
                raise ExcecaoAlteracaoDeStatusInvalida(status_pedido_atual=self.status, status_pedido_novo=novo_status)

        self.status = novo_status