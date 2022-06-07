from dataclasses import dataclass
from enafood.entidades.principal.pedido import Pedido

@dataclass
class Pagamento:
    pedido: Pedido