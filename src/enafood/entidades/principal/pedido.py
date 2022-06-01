from dataclasses import dataclass
from src.enafood.entidades.principal.produto_no_pedido import ProdutoNoPedido
from src.enafood.entidades.principal.pagamento import Pagamento
from src.enafood.entidades.principal.historico_pedido import HistoricoPedido
from src.enafood.entidades.principal.cliente import Cliente
from src.enafood.entidades.principal.status_pedido import StatusPedido

@dataclass
class Pedido:
    data: str
    valor_entrega:float
    produtos: list[ProdutoNoPedido]
    pagamento: Pagamento
    historico: list[HistoricoPedido]
    cliente: Cliente
    status: StatusPedido

    # todo: colocar um status para o pedido
    # todo: colocar função para calcular valor total