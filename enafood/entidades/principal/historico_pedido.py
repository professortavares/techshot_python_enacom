from dataclasses import dataclass
from enafood.entidades.principal.pedido import Pedido

@dataclass
class HistoricoDoPedido:
    data: str
    evento: str
    pedido: Pedido