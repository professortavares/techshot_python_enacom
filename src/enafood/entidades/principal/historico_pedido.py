from dataclasses import dataclass
from src.enafood.entidades.principal.pedido import Pedido

class HistoricoDoPedido:
    data: str
    evento: str
    pedido: Pedido