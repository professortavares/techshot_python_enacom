from dataclasses import dataclass
import enafood.entidades.principal as prinp

@dataclass
class HistoricoDoPedido:
    data: str
    evento: str
    pedido: any
