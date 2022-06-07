from dataclasses import dataclass
from enafood.entidades.principal.produto_no_pedido import ProdutoNoPedido
from enafood.entidades.principal.pagamento import Pagamento
from enafood.entidades.principal.historico_pedido import HistoricoDoPedido
from enafood.entidades.principal.cliente import Cliente
from enafood.entidades.principal.status_pedido import StatusPedido

@dataclass
class Pedido:
    data: str
    valor_entrega:float
    produtos: list[ProdutoNoPedido]
    pagamento: Pagamento
    historico: list[HistoricoDoPedido]
    cliente: Cliente
    status: StatusPedido

    # todo: colocar um status para o pedido
    # todo: colocar função para calcular valor total