from dataclasses import dataclass
from enafood.entidades.principal.status_pedido import StatusPedido
from enafood.excecoes.excecao_alteracao_status_invalida import ExcecaoAlteracaoDeStatusInvalida
from enafood.excecoes.excecao_pedido_vazio import ExcecaoPedidoVazio

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

    def conferir_pedido(self):
        """
        Altera o status do pedido para Em Conferencia
        :return:
        """

        # Aqui eu faço a validação se o pedido está vazio
        if self.produtos is None or len(self.produtos) == 0:
            raise ExcecaoPedidoVazio()

        self.alterar_status_pedido(StatusPedido.EM_CONFERENCIA)

    def alterar_status_pedido(self, novo_status):
        """
        Altera o status do pedido
        :param novo_status: StatusPedido - novo status do pedido
        :return: None
        """

        # status_atual -> [status possíveis]
        mapeamento_status = {
            StatusPedido.EM_COMPRA: [StatusPedido.EM_CONFERENCIA],
            StatusPedido.EM_CONFERENCIA: [StatusPedido.EM_COMPRA, StatusPedido.EM_PAGAMENTO],
            StatusPedido.EM_PAGAMENTO: [StatusPedido.CARTAO_VALIDO, StatusPedido.CARTAO_INVALIDO],
            StatusPedido.CARTAO_INVALIDO: [StatusPedido.EM_PAGAMENTO],
            StatusPedido.CARTAO_VALIDO: [StatusPedido.CARTAO_ATIVO],
            StatusPedido.CARTAO_ATIVO: [StatusPedido.PAGAMENTO_APROVADO],
            StatusPedido.PAGAMENTO_APROVADO: [StatusPedido.AGUARDANDO_ENTREGA],
            StatusPedido.AGUARDANDO_ENTREGA: [StatusPedido.NO_CAMINHO_PARA_ENTREGA],
            StatusPedido.NO_CAMINHO_PARA_ENTREGA: [StatusPedido.ENTREGA_REALIZADA]
        }

        # validação se o workflow é válido
        lista_status_possiveis = mapeamento_status[self.status]
        if novo_status not in lista_status_possiveis:
            raise ExcecaoAlteracaoDeStatusInvalida(status_pedido_atual=self.status, status_pedido_novo=novo_status)

        # se estiver tudo certo, então altera o status
        self.status = novo_status
